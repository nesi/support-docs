(() => {
  const API_BASE = "https://nesi-docs-rag.nesi-cloudflare.workers.dev";
  const TOKEN_KEY = "chatApiKey";
  const FAB_SEEN_KEY = "chatFabSeen";
  const HISTORY_KEY = "chatHistory";
  const getToken = () => localStorage.getItem(TOKEN_KEY) || "";

  const history = [];
  let sending = false;
  let codeBlockSeq = 0;

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

  const ROBOT_ICON =
    '<svg viewBox="0 -960 960 960" fill="currentColor" aria-hidden="true">' +
    '<path d="M160-360q-50 0-85-35t-35-85q0-50 35-85t85-35v-80q0-33 23.5-56.5T240-760h120q0-50 35-85t85-35q50 0 85 35t35 85h120q33 0 56.5 23.5T800-680v80q50 0 85 35t35 85q0 50-35 85t-85 35v160q0 33-23.5 56.5T720-120H240q-33 0-56.5-23.5T160-200v-160Zm242.5-97.5Q420-475 420-500t-17.5-42.5Q385-560 360-560t-42.5 17.5Q300-525 300-500t17.5 42.5Q335-440 360-440t42.5-17.5Zm240 0Q660-475 660-500t-17.5-42.5Q625-560 600-560t-42.5 17.5Q540-525 540-500t17.5 42.5Q575-440 600-440t42.5-17.5ZM320-280h320v-80H320v80Zm-80 80h480v-480H240v480Zm240-240Z"/>' +
    '</svg>';

  const MAXIMIZE_ICON =
    '<svg viewBox="0 -960 960 960" fill="currentColor" aria-hidden="true">' +
    '<path d="M120-120v-320h80v184l504-504H520v-80h320v320h-80v-184L256-200h184v80H120Z"/>' +
    '</svg>';
  const MINIMIZE_ICON =
    '<svg viewBox="0 -960 960 960" fill="currentColor" aria-hidden="true">' +
    '<path d="m136-80-56-56 264-264H160v-80h320v320h-80v-184L136-80Zm344-400v-320h80v184l264-264 56 56-264 264h184v80H480Z"/>' +
    '</svg>';
  const CODE_BLOCK_RE = /```(\w*)\n([\s\S]*?)```/g;
  const INLINE_CODE_RE = /`([^`]+)`/g;
  const BOLD_RE = /\*\*([^*]+)\*\*/g;
  const CITATION_RE = /\[(\d+)\]/g;
  const LIST_ITEM_RE = /^[-*] (.+)$/gm;
  const LIST_WRAP_RE = /(<li>[\s\S]*?<\/li>)(?!\s*<li>)/g;
  const PARAGRAPH_SPLIT_RE = /\n{2,}/;
  const BLOCK_TAG_RE = /^<(ul|pre)/;
  const NEWLINE_RE = /\n/g;
  const CODE_PLACEHOLDER_RE = /\0(\d+)\0/g;

  const fab = document.createElement("button");
  fab.id = "chat-fab";
  fab.className = "chat-fab";
  fab.setAttribute("aria-label", "Ask Dini, our docs AI assistant");
  fab.setAttribute("aria-expanded", "false");
  fab.innerHTML = `<span class="chat-fab-icon">${ROBOT_ICON}</span>`;

  const win = document.createElement("div");
  win.id = "chat-window";
  win.className = "chat-window";
  win.setAttribute("role", "dialog");
  win.setAttribute("aria-label", "Ask Dini, our docs AI assistant");
  win.innerHTML = `
    <div class="chat-header">
      <span class="chat-header-title">DinAI</span>
      <button id="chat-expand" class="chat-header-btn" aria-label="Maximise chat" aria-pressed="false">${MAXIMIZE_ICON}</button>
    </div>
    <div class="chat-disclaimer">
      <p>This chat uses a RAG model, double-check output.<br class="chat-disclaimer-break">
      <a href="mailto:support@nesi.org.nz?subject=SupportRequest" target="_blank">Contact Support</a>
      if you have feedback.</p>
    </div>
    <div id="chat-messages"
         class="chat-messages"
         role="log"
         aria-live="polite"></div>
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

  try {
    for (const m of JSON.parse(localStorage.getItem(HISTORY_KEY) || "[]")) {
      history.push(m);
      messages.insertAdjacentHTML(
        "beforeend",
        m.role === "user"
          ? `<div class="chat-msg chat-msg-user">${escapeHtml(m.content)}</div>`
          : `<div class="chat-msg chat-msg-bot">${render(m.content)}</div>`
      );
    }
    messages.scrollTop = messages.scrollHeight;
  } catch {}

  function render(md, sources) {
    let html = escapeHtml(md);

    const blocks = [];

    html = html.replace(
      CODE_BLOCK_RE,
      (_, lang, code) => {
        blocks.push(code);
        return `\0${blocks.length - 1}\0`;
      }
    );

    html = html
      .replace(INLINE_CODE_RE, "<code>$1</code>")
      .replace(BOLD_RE, "<strong>$1</strong>")
      .replace(CITATION_RE, (_, n) => {
        const src = sources?.[n - 1];
        if (!src) return `[${n}]`;

        return `<sup class="chat-cite" data-url="${escapedUrl(src.url)}" title="${escapeHtml(src.title || "")}">[${n}]</sup>`;
      })
      .replace(LIST_ITEM_RE, "<li>$1</li>")
      .replace(LIST_WRAP_RE, "<ul>$1</ul>");

    html = html
      .split(PARAGRAPH_SPLIT_RE)
      .map(p =>
        BLOCK_TAG_RE.test(p.trim())
          ? p
          : `<p>${p.replace(NEWLINE_RE, "<br>")}</p>`
      )
      .join("");

    html = html.replace(
      CODE_PLACEHOLDER_RE,
      (_, i) => {
        const id = `chat-code-${codeBlockSeq++}`;
        return `<div class="chat-code-block"><pre><code id="${id}">${blocks[i]}</code></pre>` +
          `<button class="chat-copy-btn" data-copy-target="${id}" aria-label="Copy code" title="Copy code"></button></div>`;
      }
    );

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
  async function streamChat(question, onToken) {
    const res = await fetch(`${API_BASE}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getToken()}`
      },
      body: JSON.stringify({ question, history })
    });

    if (!res.ok) {
      throw new Error(
        (await res.json().catch(() => ({}))).error ||
        `HTTP ${res.status}`
      );
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    let buffer = "";
    let sources = [];

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });

      const lines = buffer.split("\n");
      buffer = lines.pop() ?? "";

      for (const line of lines) {
        if (!line.startsWith("data: ")) continue;

        const ev = JSON.parse(line.slice(6));

        switch (ev.type) {
          case "sources":
            sources = ev.sources;
            break;

          case "token":
            onToken(ev.text, sources);
            break;
        }
      }
    }

    return sources;
  }

  async function send() {
    const question = input.value.trim();
    if (!question || sending) return;

    if (!getToken()) {
      return;
    }

    sending = true;
    sendBtn.disabled = true;

    input.value = "";
    input.style.height = "auto";

    messages.insertAdjacentHTML(
      "beforeend",
      `<div class="chat-msg chat-msg-user">${escapeHtml(question)}</div>`
    );

    const botMsg = document.createElement("div");
    botMsg.className = "chat-msg chat-msg-bot";
    botMsg.innerHTML =
      '<span class="chat-thinking">Reading the docs…</span>';

    messages.append(botMsg);
    messages.scrollTop = messages.scrollHeight;

    let answer = "";

    try {
      const sources = await streamChat(question, (text, src) => {
        answer += text;
        botMsg.innerHTML = render(answer, src);
        messages.scrollTop = messages.scrollHeight;
      });

      if (sources.length) {
        botMsg.append(renderSources(sources));
      }

      history.push(
        { role: "user", content: question },
        { role: "assistant", content: answer }
      );

      history.splice(0, Math.max(0, history.length - 12));

    } catch (err) {
      botMsg.innerHTML = `<p class="chat-error">Error: ${escapeHtml(err.message)}</p>`;
    } finally {
      sending = false;
      sendBtn.disabled = false;
      input.focus();
      messages.scrollTop = messages.scrollHeight;
    }
  }
  function setExpanded(expanded) {
    win.classList.toggle("chat-window--expanded", expanded);
    expandBtn.innerHTML = expanded ? MINIMIZE_ICON : MAXIMIZE_ICON;
    expandBtn.setAttribute("aria-label", expanded ? "Minimise chat" : "Maximise chat");
    expandBtn.setAttribute("aria-pressed", String(expanded));
  }

  function setOpen(open) {
    win.classList.toggle("chat-open", open);
    fab.setAttribute("aria-expanded", String(open));

    if (open) {
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

  document$.subscribe(() => {
    if (getToken()) {
      if (!document.body.contains(fab)) {
        document.body.append(win, fab);

        if (!localStorage.getItem(FAB_SEEN_KEY)) {
          fab.classList.add("chat-fab--pulse");
          localStorage.setItem(FAB_SEEN_KEY, "1");
        }
      }
    } else if (document.body.contains(fab)) {
      win.remove();
      fab.remove();
    }
  });
})();
