(() => {
  const API_BASE = "https://nesi-docs-rag.nesi-cloudflare.workers.dev";
  const TOKEN_KEY = "chatApiKey";
  const FAB_SEEN_KEY = "chatFabSeen";
  const HISTORY_KEY = "chatHistory";
  const SUPPORT_MAILTO = "mailto:support@nesi.org.nz?subject=SupportRequest";
  // Turns kept (and sent to the API as context). 12 = 6 question/answer pairs.
  const HISTORY_LIMIT = 12;
  // Give up if nothing arrives from the API for this long.
  const IDLE_TIMEOUT_MS = 60000;
  // How close to the bottom (px) counts as "following" the conversation.
  const STICK_THRESHOLD_PX = 40;

  const storage = {
    get(key) {
      try { return localStorage.getItem(key); } catch { return null; }
    },
    set(key, value) {
      try { localStorage.setItem(key, value); } catch {}
    },
    remove(key) {
      try { localStorage.removeItem(key); } catch {}
    }
  };

  const getToken = () => storage.get(TOKEN_KEY) || "";

  // Each entry: { role: "user" | "assistant", content, sources? }.
  // Only role and content are sent to the API.
  let history = [];
  let sending = false;
  let codeBlockSeq = 0;

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }

  const ESCAPE_MAP = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };

  const escapeHtml = (s) =>
    String(s ?? "").replace(/[&<>"']/g, c => ESCAPE_MAP[c]);

  const safeUrl = (u) =>
    /^https?:\/\//i.test(u || "") ? u : "#";

  // The API returns production URLs. Point them at the site being viewed
  // (mkdocs serve, a preview build, ...) so Material's instant navigation
  // handles them as internal links instead of loading production.
  const PROD_SITE_URL = "https://docs.nesi.org.nz/";
  const localUrl = (u) =>
    u.startsWith(PROD_SITE_URL) ? (window.__md_scope?.href || PROD_SITE_URL) + u.slice(PROD_SITE_URL.length) : u;

  const escapedUrl = (u) => escapeHtml(localUrl(safeUrl(u)));

  const svgIcon = (path) =>
    `<svg viewBox="0 -960 960 960" fill="currentColor" aria-hidden="true"><path d="${path}"/></svg>`;

  const ROBOT_ICON = svgIcon("M160-360q-50 0-85-35t-35-85q0-50 35-85t85-35v-80q0-33 23.5-56.5T240-760h120q0-50 35-85t85-35q50 0 85 35t35 85h120q33 0 56.5 23.5T800-680v80q50 0 85 35t35 85q0 50-35 85t-85 35v160q0 33-23.5 56.5T720-120H240q-33 0-56.5-23.5T160-200v-160Zm242.5-97.5Q420-475 420-500t-17.5-42.5Q385-560 360-560t-42.5 17.5Q300-525 300-500t17.5 42.5Q335-440 360-440t42.5-17.5Zm240 0Q660-475 660-500t-17.5-42.5Q625-560 600-560t-42.5 17.5Q540-525 540-500t17.5 42.5Q575-440 600-440t42.5-17.5ZM320-280h320v-80H320v80Zm-80 80h480v-480H240v480Zm240-240Z");
  const MAXIMIZE_ICON = svgIcon("M120-120v-320h80v184l504-504H520v-80h320v320h-80v-184L256-200h184v80H120Z");
  const MINIMIZE_ICON = svgIcon("m136-80-56-56 264-264H160v-80h320v320h-80v-184L136-80Zm344-400v-320h80v184l264-264 56 56-264 264h184v80H480Z");
  const CLEAR_ICON = svgIcon("M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z");
  const CLOSE_ICON = svgIcon("m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z");

  const CODE_BLOCK_RE = /```\w*\n([\s\S]*?)```/g;
  const INLINE_CODE_RE = /`([^`]+)`/g;
  const BOLD_RE = /\*\*([^*]+)\*\*/g;
  // Runs on escaped text, so the URL is already HTML-safe; only the scheme needs checking.
  const LINK_RE = /\[([^\]]+)\]\(((?:https?:\/\/|mailto:)[^)\s]+)\)/g;
  const CITATION_RE = /\[(\d+)\]/g;
  const UL_ITEM_RE = /^\s*[-*] (.+)$/;
  const OL_ITEM_RE = /^\s*(\d+)[.)] (.+)$/;
  const CODE_LINE_RE = /^\s*\0(\d+)\0\s*$/;
  const CODE_PLACEHOLDER_RE = /\0(\d+)\0/g;
  const INLINE_PLACEHOLDER_RE = /\x01(\d+)\x01/g;

  const fab = document.createElement("button");
  fab.id = "chat-fab";
  fab.className = "chat-fab";
  fab.setAttribute("aria-label", "Ask DinAI, our docs AI assistant");
  fab.setAttribute("aria-expanded", "false");
  fab.innerHTML = `<span class="chat-fab-icon">${ROBOT_ICON}</span>`;

  const win = document.createElement("div");
  win.id = "chat-window";
  win.className = "chat-window";
  win.setAttribute("role", "dialog");
  win.setAttribute("aria-label", "Ask DinAI, our docs AI assistant");
  win.innerHTML = `
    <div class="chat-header">
      <span class="chat-header-title">DinAI</span>
      <button id="chat-clear" class="chat-header-btn" aria-label="Clear chat" title="Clear chat">${CLEAR_ICON}</button>
      <button id="chat-expand" class="chat-header-btn" aria-label="Maximise chat" title="Maximise chat" aria-pressed="false">${MAXIMIZE_ICON}</button>
      <button id="chat-close" class="chat-header-btn" aria-label="Close chat" title="Close chat">${CLOSE_ICON}</button>
    </div>
    <div class="chat-disclaimer">
      <p>This chat uses an AI model, double-check output.<br class="chat-disclaimer-break">
      <a href="${SUPPORT_MAILTO}">Contact Support</a>
      if you have feedback.</p>
    </div>
    <div id="chat-messages"
         class="chat-messages"
         role="log"
         aria-live="polite"
         aria-busy="false"></div>
    <div class="chat-input-row">
      <textarea
        id="chat-input"
        rows="1"
        aria-label="Ask a question"
        placeholder="Ask about our HPC Mahuika"></textarea>
      <button id="chat-send" aria-label="Send">&#10148;</button>
    </div>
  `;

  const input = win.querySelector("#chat-input");
  const sendBtn = win.querySelector("#chat-send");
  const messages = win.querySelector("#chat-messages");
  const expandBtn = win.querySelector("#chat-expand");
  const clearBtn = win.querySelector("#chat-clear");
  const closeBtn = win.querySelector("#chat-close");

  /* ------------------------------ rendering ------------------------------ */

  function renderInline(text, sources) {
    return text
      .replace(BOLD_RE, "<strong>$1</strong>")
      .replace(LINK_RE, (_, label, url) => `<a href="${localUrl(url)}">${label}</a>`)
      .replace(CITATION_RE, (_, n) => {
        const src = sources?.[n - 1];
        if (!src) return `[${n}]`;

        return `<sup class="chat-cite"><a href="${escapedUrl(src.url)}" title="${escapeHtml(src.title || "")}">[${n}]</a></sup>`;
      });
  }

  // Groups lines into paragraphs and lists. A list stays open across blank
  // lines (models often space out numbered steps), and an indented code block
  // directly after a list item is kept inside that item.
  function renderBlocks(text, sources) {
    const out = [];
    let para = [];
    let list = null;

    const flushPara = () => {
      if (para.length) out.push(`<p>${para.join("<br>")}</p>`);
      para = [];
    };
    const flushList = () => {
      if (!list) return;
      const start = list.tag === "ol" && list.start !== 1 ? ` start="${list.start}"` : "";
      out.push(`<${list.tag}${start}>${list.items.map(i => `<li>${i}</li>`).join("")}</${list.tag}>`);
      list = null;
    };

    for (const line of text.split("\n")) {
      const ul = line.match(UL_ITEM_RE);
      const ol = line.match(OL_ITEM_RE);

      if (ul || ol) {
        const tag = ul ? "ul" : "ol";
        flushPara();
        if (list && list.tag !== tag) flushList();
        if (!list) list = { tag, start: ol ? Number(ol[1]) : 1, items: [] };
        list.items.push(renderInline(ul ? ul[1] : ol[2], sources));
      } else if (CODE_LINE_RE.test(line)) {
        flushPara();
        if (list && /^\s/.test(line)) {
          list.items[list.items.length - 1] += line.trim();
        } else {
          flushList();
          out.push(line.trim());
        }
      } else if (!line.trim()) {
        flushPara();
      } else {
        flushList();
        para.push(renderInline(line, sources));
      }
    }
    flushPara();
    flushList();

    return out.join("");
  }

  function render(md, sources) {
    let html = escapeHtml(md);

    const blocks = [];
    const inline = [];

    html = html.replace(CODE_BLOCK_RE, (_, code) => {
      // Strip the shared indent of blocks nested under list items, so copied code is clean.
      const lines = code.replace(/\s+$/, "").split("\n");
      const indent = Math.min(...lines.filter(l => l.trim()).map(l => l.match(/^ */)[0].length), Infinity);
      blocks.push(lines.map(l => l.slice(indent === Infinity ? 0 : indent)).join("\n"));
      return `\0${blocks.length - 1}\0`;
    });

    // Keep inline code out of the bold/link/citation rules.
    html = html.replace(INLINE_CODE_RE, (_, code) => {
      inline.push(code);
      return `\x01${inline.length - 1}\x01`;
    });

    html = renderBlocks(html, sources)
      .replace(INLINE_PLACEHOLDER_RE, (_, i) => `<code>${inline[i]}</code>`)
      .replace(CODE_PLACEHOLDER_RE, (_, i) => {
        const id = `chat-code-${codeBlockSeq++}`;
        return `<div class="chat-code-block"><pre><code id="${id}">${blocks[i]}</code></pre>` +
          `<button class="chat-copy-btn" data-copy-target="${id}" aria-label="Copy code" title="Copy code"></button></div>`;
      });

    return html;
  }

  // `indices` are 0-based positions in `sources`; each keeps its original [n].
  function renderSources(sources, indices) {
    const details = document.createElement("details");
    details.className = "chat-sources";

    details.innerHTML =
      `<summary>${indices.length} source${indices.length === 1 ? "" : "s"}</summary>` +
      indices
        .map(i => {
          const s = sources[i];
          return `<a href="${escapedUrl(s.url)}">[${i + 1}] ${escapeHtml(s.title)} — ${escapeHtml(s.heading)}</a>`;
        })
        .join("");

    return details;
  }

  // Which sources to list under each bubble of an answer: the ones that bubble
  // cites, plus any source no bubble cites on the last one. A single-bubble
  // answer therefore lists every source.
  function sourcesPerPart(parts, sources) {
    if (!sources?.length) return parts.map(() => []);

    const cited = parts.map(part => {
      const text = part.replace(CODE_BLOCK_RE, "").replace(INLINE_CODE_RE, "");
      const found = new Set();
      for (const [, n] of text.matchAll(CITATION_RE)) {
        if (sources[n - 1]) found.add(n - 1);
      }
      return found;
    });

    const uncited = sources.map((_, i) => i).filter(i => !cited.some(set => set.has(i)));
    uncited.forEach(i => cited.at(-1).add(i));

    return cited.map(set => [...set].sort((a, b) => a - b));
  }

  function appendSources(el, sources, indices) {
    if (indices?.length) el.append(renderSources(sources, indices));
  }

  function appendMessage(role, content, sources, sourceIndices) {
    const el = document.createElement("div");
    if (role === "user") {
      el.className = "chat-msg chat-msg-user";
      el.textContent = content;
    } else {
      el.className = "chat-msg chat-msg-bot";
      el.innerHTML = render(content, sources);
      appendSources(el, sources, sourceIndices);
    }
    messages.append(el);
    return el;
  }

  /* ------------------------------- history ------------------------------- */

  function saveHistory() {
    storage.set(HISTORY_KEY, JSON.stringify(history));
  }

  function loadHistory() {
    try {
      const saved = JSON.parse(storage.get(HISTORY_KEY) || "[]");
      if (!Array.isArray(saved)) return;
      history = saved
        .filter(m => (m?.role === "user" || m?.role === "assistant") && typeof m.content === "string")
        .slice(-HISTORY_LIMIT);
    } catch {
      history = [];
    }
    for (const m of history) {
      // Multi-part answers (see "break" in streamChat) restore as separate bubbles.
      const parts = Array.isArray(m.parts) ? m.parts : [m.content];
      const perPart = sourcesPerPart(parts, m.sources);
      parts.forEach((part, i) => appendMessage(m.role, part, m.sources, perPart[i]));
    }
  }

  function clearHistory() {
    if (sending) return;
    history = [];
    storage.remove(HISTORY_KEY);
    messages.replaceChildren();
    input.focus();
  }

  /* ------------------------------ scrolling ------------------------------ */

  const isNearBottom = () =>
    messages.scrollHeight - messages.scrollTop - messages.clientHeight < STICK_THRESHOLD_PX;

  const scrollToBottom = () => {
    messages.scrollTop = messages.scrollHeight;
  };

  // Runs `update`, then keeps the view at the bottom only if it was already there.
  function keepScrolled(update) {
    const stick = isNearBottom();
    update();
    if (stick) scrollToBottom();
  }

  /* ------------------------------- network ------------------------------- */

  function friendlyError(err) {
    if (err.name === "AbortError") {
      return "The answer took too long to arrive. Try again, or rephrase your question.";
    }
    if (err.status === 429) {
      return "You're sending questions too quickly. Wait a minute, then try again.";
    }
    if (err.name === "TypeError") {
      return "Couldn't reach the chat service. Check your connection and try again.";
    }
    return "Something went wrong getting an answer. Try again shortly.";
  }

  // onBreak: the server sends a "break" event between parts of an answer (the
  // short answer, a code block, the "More:" docs link) so each can be shown as
  // its own bubble. Older/other servers just never send it.
  async function streamChat(question, onToken, onBreak) {
    const controller = new AbortController();
    let timer;
    const resetTimer = () => {
      clearTimeout(timer);
      timer = setTimeout(() => controller.abort(), IDLE_TIMEOUT_MS);
    };

    try {
      resetTimer();
      const res = await fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...(getToken() && { Authorization: `Bearer ${getToken()}` })
        },
        body: JSON.stringify({
          question,
          history: history.map(({ role, content }) => ({ role, content }))
        }),
        signal: controller.signal
      });

      if (!res.ok) {
        const { error } = await res.json().catch(() => ({}));
        throw Object.assign(new Error(error || `HTTP ${res.status}`), { status: res.status });
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      let buffer = "";
      let sources = [];

      while (true) {
        resetTimer();
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split("\n");
        buffer = lines.pop() ?? "";

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;

          let ev;
          try {
            ev = JSON.parse(line.slice(6));
          } catch {
            continue;
          }

          switch (ev.type) {
            case "sources":
              sources = ev.sources || [];
              break;

            case "token":
              onToken(ev.text, sources);
              break;

            case "break":
              onBreak?.();
              break;
          }
        }
      }

      return sources;
    } finally {
      clearTimeout(timer);
    }
  }

  /* ------------------------------- commands ------------------------------- */
  // Inputs that control the chat window instead of going to the API.
  // Matched against the whole input only, so "how do I clear my scratch?"
  // is still a question.

  const COMMANDS = [
    {
      names: ["clear", "clc", "cls", "reset", "clear chat", "new chat"],
      run: () => clearHistory()
    },
    {
      names: ["exit", "quit", "close", "q", "wq", "bye", "logout", "close chat"],
      run: () => setOpen(false)
    },
    {
      names: ["fullscreen", "full screen", "maximise", "maximize", "max", "expand", "bigger"],
      run: () => setExpanded(true)
    },
    {
      names: ["minimise", "minimize", "min", "shrink", "smaller", "exit fullscreen", "exit full screen", "restore"],
      run: () => setExpanded(false)
    }
  ];

  const COMMAND_MAP = new Map(
    COMMANDS.flatMap(c => c.names.map(n => [n, c]))
  );

  // Ignores case, a leading "/", "\" or ":" (as in /clear, :q) and trailing punctuation.
  const normaliseCommand = (text) =>
    text.toLowerCase().replace(/^[/\\:]+/, "").replace(/[!.?]+$/, "").replace(/\s+/g, " ").trim();

  // Returns true if the input was a command and has been handled.
  function runCommand(text) {
    const name = normaliseCommand(text);
    const command = COMMAND_MAP.get(name);
    if (!command) return false;
    // Clearing mid-answer would orphan the streaming message; treat it as a question-in-waiting.
    if (sending && command.names.includes("clear")) return false;

    command.run();
    gtag("event", "rag_chat_command", { command: command.names[0] });
    return true;
  }

  function setSending(on) {
    sending = on;
    sendBtn.disabled = on;
    clearBtn.disabled = on;
    messages.setAttribute("aria-busy", String(on));
  }

  async function send() {
    const question = input.value.trim();
    if (!question) return;

    const isCommand = runCommand(question);
    if (!isCommand && sending) return;

    input.value = "";
    input.style.height = "auto";
    if (isCommand) return;

    setSending(true);
    appendMessage("user", question);

    let botMsg = appendMessage("assistant", "");
    botMsg.innerHTML = '<span class="chat-thinking">Reading the docs…</span>';
    scrollToBottom();

    // One entry per bubble. A "break" event only marks that the next token
    // starts a new bubble, so a trailing break never leaves an empty one.
    const parts = [""];
    const bubbles = [botMsg];
    let breakPending = false;

    try {
      const sources = await streamChat(
        question,
        (text, src) => keepScrolled(() => {
          if (breakPending) {
            breakPending = false;
            parts.push("");
            botMsg = appendMessage("assistant", "");
            bubbles.push(botMsg);
          }
          parts[parts.length - 1] += text;
          botMsg.innerHTML = render(parts.at(-1), src);
        }),
        () => { breakPending = Boolean(parts.at(-1).trim()); }
      );

      const perPart = sourcesPerPart(parts, sources);
      keepScrolled(() => bubbles.forEach((el, i) => appendSources(el, sources, perPart[i])));

      // `content` (all parts joined) is what goes back to the API as history;
      // `parts` is only used to restore the bubbles on reload.
      const trimmed = parts.map(p => p.trim());
      const answer = trimmed.filter(Boolean).join("\n\n");
      history.push(
        { role: "user", content: question },
        { role: "assistant", content: answer, sources, ...(parts.length > 1 && { parts: trimmed }) }
      );
      history.splice(0, Math.max(0, history.length - HISTORY_LIMIT));
      saveHistory();

      gtag("event", "rag_chat", {
        question_length: question.length,
        answer_length: answer.length,
        answer_parts: parts.length,
        source_count: sources.length
      });
    } catch (err) {
      console.error("DinAI chat error:", err);

      const note =
        `<p class="chat-error">${escapeHtml(friendlyError(err))} ` +
        `If it keeps happening, <a href="${SUPPORT_MAILTO}">contact Support</a>.</p>`;

      if (parts.at(-1).trim()) {
        botMsg.insertAdjacentHTML("beforeend", note);
      } else {
        botMsg.innerHTML = note;
      }

      gtag("event", "rag_chat_error", {
        status: err.status || (err.name === "AbortError" ? "timeout" : "network"),
        partial_answer: parts.some(p => p.trim())
      });
    } finally {
      setSending(false);
      input.focus();
    }
  }

  /* -------------------------------- window -------------------------------- */

  function setExpanded(expanded) {
    const label = expanded ? "Minimise chat" : "Maximise chat";
    win.classList.toggle("chat-window--expanded", expanded);
    expandBtn.innerHTML = expanded ? MINIMIZE_ICON : MAXIMIZE_ICON;
    expandBtn.setAttribute("aria-label", label);
    expandBtn.setAttribute("title", label);
    expandBtn.setAttribute("aria-pressed", String(expanded));
  }

  function setOpen(open) {
    win.classList.toggle("chat-open", open);
    fab.setAttribute("aria-expanded", String(open));

    if (open) {
      scrollToBottom();
      input.focus();
    } else {
      fab.focus();
    }
  }

  messages.addEventListener("click", (e) => {
    const copyBtn = e.target.closest(".chat-copy-btn");
    if (copyBtn && navigator.clipboard) {
      const code = document.getElementById(copyBtn.dataset.copyTarget);
      if (!code) return;

      navigator.clipboard.writeText(code.textContent).then(() => {
        copyBtn.classList.add("chat-copy-btn--done");
        setTimeout(() => copyBtn.classList.remove("chat-copy-btn--done"), 1200);
      });
    }
  });

  sendBtn.addEventListener("click", send);
  clearBtn.addEventListener("click", clearHistory);
  closeBtn.addEventListener("click", () => setOpen(false));

  expandBtn.addEventListener("click", () => {
    setExpanded(!win.classList.contains("chat-window--expanded"));
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  });

  input.addEventListener("input", () => {
    input.style.height = "auto";
    input.style.height = `${input.scrollHeight}px`;
  });

  fab.addEventListener("click", () => {
    fab.classList.remove("chat-fab--pulse");
    setOpen(!win.classList.contains("chat-open"));
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && win.classList.contains("chat-open")) setOpen(false);
  });

  loadHistory();

  document$.subscribe(() => {
    if (!document.body.contains(fab)) {
      document.body.append(win, fab);

      if (!storage.get(FAB_SEEN_KEY)) {
        fab.classList.add("chat-fab--pulse");
        storage.set(FAB_SEEN_KEY, "1");
      }
    }
  });
})();
