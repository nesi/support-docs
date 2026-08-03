(() => {
  const API_BASE = "https://nesi-docs-rag.nesi-cloudflare.workers.dev";
  const TOKEN_KEY = "chatApiKey";
  const getToken = () => localStorage.getItem(TOKEN_KEY) || "";

  const history = [];
  let sending = false;

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

  const fab = document.createElement("button");
  fab.id = "chat-fab";
  fab.className = "chat-fab";
  fab.setAttribute("aria-label", "Ask the docs assistant");
  fab.setAttribute("aria-expanded", "false");
  fab.innerHTML = '<span class="chat-fab-icon">&#128172;</span>';

  const win = document.createElement("div");
  win.id = "chat-window";
  win.className = "chat-window";
  win.setAttribute("role", "dialog");
  win.setAttribute("aria-label", "Ask Dini");
  win.innerHTML = `
    <div class="chat-header">
      <span>Ask Dini</span>
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

  function render(md, sources) {
    let html = escapeHtml(md);

    const blocks = [];

    html = html.replace(
      /```(\w*)\n([\s\S]*?)```/g,
      (_, lang, code) => {
        blocks.push(code);
        return `\0${blocks.length - 1}\0`;
      }
    );

    html = html
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/\[(\d+)\]/g, (_, n) => {
        const src = sources?.[n - 1];
        if (!src) return `[${n}]`;

        return `<sup class="chat-cite" data-url="${escapeHtml(safeUrl(src.url))}" title="${escapeHtml(src.title || "")}">[${n}]</sup>`;
      })
      .replace(/^[-*] (.+)$/gm, "<li>$1</li>")
      .replace(
        /(<li>[\s\S]*?<\/li>)(?!\s*<li>)/g,
        "<ul>$1</ul>"
      );

    html = html
      .split(/\n{2,}/)
      .map(p =>
        /^<(ul|pre)/.test(p.trim())
          ? p
          : `<p>${p.replace(/\n/g, "<br>")}</p>`
      )
      .join("");

    html = html.replace(
      /\0(\d+)\0/g,
      (_, i) => `<pre><code>${blocks[i]}</code></pre>`
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
            `<a href="${escapeHtml(safeUrl(s.url))}" target="_blank" rel="noopener">[${i + 1}] ${escapeHtml(s.title)} — ${escapeHtml(s.heading)}</a>`
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
      alert(
        `No API token found.\n\nRun:\nlocalStorage.setItem('${TOKEN_KEY}', '<token>')`
      );
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
      '<span class="chat-thinking">Searching the docs…</span>';

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
    }
  });

  sendBtn.addEventListener("click", send);

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

  // navigation.instant (SPA mode) swaps document.body on every page change
  // without re-running this script, so re-append on every document$ tick
  // rather than once on DOMContentLoaded — same pattern as mathjax.js.
  document$.subscribe(() => {
    if (!document.body.contains(fab)) document.body.append(win, fab);
  });
})();
