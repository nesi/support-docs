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

  const ESCAPE_MAP = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  };

  const escapeHtml = (s) =>
    String(s ?? "").replace(/[&<>"']/g, c => ESCAPE_MAP[c]);

  const safeUrl = (u) =>
    /^https?:\/\//i.test(u || "") ? u : "#";

  const escapedUrl = (u) => escapeHtml(safeUrl(u));

  const svgIcon = (path) =>
    `<svg viewBox="0 -960 960 960" fill="currentColor" aria-hidden="true"><path d="${path}"/></svg>`;

  const ROBOT_ICON = svgIcon("M160-360q-50 0-85-35t-35-85q0-50 35-85t85-35v-80q0-33 23.5-56.5T240-760h120q0-50 35-85t85-35q50 0 85 35t35 85h120q33 0 56.5 23.5T800-680v80q50 0 85 35t35 85q0 50-35 85t-85 35v160q0 33-23.5 56.5T720-120H240q-33 0-56.5-23.5T160-200v-160Zm242.5-97.5Q420-475 420-500t-17.5-42.5Q385-560 360-560t-42.5 17.5Q300-525 300-500t17.5 42.5Q335-440 360-440t42.5-17.5Zm240 0Q660-475 660-500t-17.5-42.5Q625-560 600-560t-42.5 17.5Q540-525 540-500t17.5 42.5Q575-440 600-440t42.5-17.5ZM320-280h320v-80H320v80Zm-80 80h480v-480H240v480Zm240-240Z");
  const MAXIMIZE_ICON = svgIcon("M120-120v-320h80v184l504-504H520v-80h320v320h-80v-184L256-200h184v80H120Z");
  const MINIMIZE_ICON = svgIcon("m136-80-56-56 264-264H160v-80h320v320h-80v-184L136-80Zm344-400v-320h80v184l264-264 56 56-264 264h184v80H480Z");
  const NEW_CHAT_ICON = svgIcon("M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z");
  const CLOSE_ICON = svgIcon("m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z");

  const CODE_BLOCK_RE = /```(\w*)\n([\s\S]*?)```/g;
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
      <button id="chat-new" class="chat-header-btn" aria-label="New chat" title="New chat">${NEW_CHAT_ICON}</button>
      <button id="chat-expand" class="chat-header-btn" aria-label="Maximise chat" title="Maximise chat" aria-pressed="false">${MAXIMIZE_ICON}</button>
      <button id="chat-close" class="chat-header-btn" aria-label="Close chat" title="Close chat">${CLOSE_ICON}</button>
    </div>
    <div class="chat-disclaimer">
      <p>This chat uses an AI model, double-check output.<br class="chat-disclaimer-break">
      <a href="${SUPPORT_MAILTO}" target="_blank">Contact Support</a>
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
  const newBtn = win.querySelector("#chat-new");
  const closeBtn = win.querySelector("#chat-close");

  /* ------------------------------ rendering ------------------------------ */

  function renderInline(text, sources) {
    return text
      .replace(BOLD_RE, "<strong>$1</strong>")
      .replace(LINK_RE, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(CITATION_RE, (_, n) => {
        const src = sources?.[n - 1];
        if (!src) return `[${n}]`;

        return `<sup class="chat-cite" data-url="${escapedUrl(src.url)}" title="${escapeHtml(src.title || "")}">[${n}]</sup>`;
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

    html = html.replace(CODE_BLOCK_RE, (_, _lang, code) => {
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

  function renderSources(sources) {
    const details = document.createElement("details");
    details.className = "chat-sources";

    details.innerHTML =
      `<summary>${sources.length} sources</summary>` +
      sources
        .map(
          (s, i) =>
            `<a href="${escapedUrl(s.url)}" target="_blank" rel="noopener">[${i + 1}] ${escapeHtml(s.title)} — ${escapeHtml(s.heading)}</a>`
        )
        .join("");

    return details;
  }

  function appendMessage(role, content, sources) {
    const el = document.createElement("div");
    if (role === "user") {
      el.className = "chat-msg chat-msg-user";
      el.textContent = content;
    } else {
      el.className = "chat-msg chat-msg-bot";
      el.innerHTML = render(content, sources);
      if (sources?.length) el.append(renderSources(sources));
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
    for (const m of history) appendMessage(m.role, m.content, m.sources);
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

  /* ------------------------------- network ------------------------------- */

  class ChatError extends Error {
    constructor(message, status) {
      super(message);
      this.status = status;
    }
  }

  function friendlyError(err) {
    if (err.name === "AbortError") {
      return "The answer took too long to arrive. Try again, or rephrase your question.";
    }
    if (err.status === 429) {
      return "You're sending questions too quickly. Wait a minute, then try again.";
    }
    if (err instanceof TypeError) {
      return "Couldn't reach the chat service. Check your connection and try again.";
    }
    return "Something went wrong getting an answer. Try again shortly.";
  }

  async function streamChat(question, onToken) {
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
        throw new ChatError(
          (await res.json().catch(() => ({}))).error || `HTTP ${res.status}`,
          res.status
        );
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
          }
        }
      }

      return sources;
    } finally {
      clearTimeout(timer);
    }
  }

  async function send() {
    const question = input.value.trim();
    if (!question || sending) return;

    sending = true;
    sendBtn.disabled = true;
    newBtn.disabled = true;

    input.value = "";
    input.style.height = "auto";

    appendMessage("user", question);

    const botMsg = document.createElement("div");
    botMsg.className = "chat-msg chat-msg-bot";
    botMsg.innerHTML =
      '<span class="chat-thinking">Reading the docs…</span>';

    messages.append(botMsg);
    messages.setAttribute("aria-busy", "true");
    scrollToBottom();

    let answer = "";
    let sourceCount = 0;

    try {
      const sources = await streamChat(question, (text, src) => {
        const stick = isNearBottom();
        answer += text;
        botMsg.innerHTML = render(answer, src);
        if (stick) scrollToBottom();
      });
      sourceCount = sources.length;

      const stick = isNearBottom();
      if (sources.length) {
        botMsg.append(renderSources(sources));
      }
      if (stick) scrollToBottom();

      history.push(
        { role: "user", content: question },
        { role: "assistant", content: answer, sources }
      );
      history.splice(0, Math.max(0, history.length - HISTORY_LIMIT));
      saveHistory();

      gtag("event", "rag_chat", {
        question_length: question.length,
        answer_length: answer.length,
        source_count: sourceCount
      });

    } catch (err) {
      console.error("DinAI chat error:", err);

      const note =
        `<p class="chat-error">${escapeHtml(friendlyError(err))} ` +
        `If it keeps happening, <a href="${SUPPORT_MAILTO}" target="_blank">contact Support</a>.</p>`;

      if (answer) {
        botMsg.insertAdjacentHTML("beforeend", note);
      } else {
        botMsg.innerHTML = note;
      }

      gtag("event", "rag_chat_error", {
        status: err.status || (err.name === "AbortError" ? "timeout" : "network"),
        partial_answer: Boolean(answer)
      });
    } finally {
      messages.setAttribute("aria-busy", "false");
      sending = false;
      sendBtn.disabled = false;
      newBtn.disabled = false;
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
    const cite = e.target.closest(".chat-cite");
    if (cite) {
      window.open(cite.dataset.url, "_blank", "noopener");
      return;
    }

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
  newBtn.addEventListener("click", clearHistory);
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
    if (
      e.key === "Escape" &&
      win.classList.contains("chat-open")
    ) {
      setOpen(false);
    }
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
