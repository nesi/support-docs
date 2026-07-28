/**
 * NeSI docs chat widget — floating button + slide-up window, backed by the
 * nesi-docs-rag Cloudflare Worker (https://github.com/nesi/nesi-docs-rag).
 *
 * Local-testing prototype: the Worker is cross-origin (CORS is wide open on
 * its side) and currently requires a shared API key, entered once and kept
 * in localStorage — get the key from whoever's running the RAG project, it
 * isn't checked in here. Swap API_BASE below once there's a settled
 * production URL/domain.
 */
(() => {
  const API_BASE = "https://nesi-docs-rag.nesi-cloudflare.workers.dev";
  const KEY_STORAGE = "nesiChatApiKey";

  const history = [];
  let sending = false;

  const fab = document.createElement("button");
  fab.id = "nesi-chat-fab";
  fab.className = "nesi-chat-fab";
  fab.setAttribute("aria-label", "Ask the docs assistant");
  fab.innerHTML = '<span class="nesi-chat-fab-icon">&#128172;</span>';

  const win = document.createElement("div");
  win.id = "nesi-chat-window";
  win.className = "nesi-chat-window";
  win.innerHTML = `
    <div class="nesi-chat-header">
      <span>NeSI Docs Assistant</span>
      <input id="nesi-chat-key" type="password" placeholder="API key" title="Shared testing API key">
    </div>
    <div class="nesi-chat-messages" id="nesi-chat-messages"></div>
    <div class="nesi-chat-input-row">
      <textarea id="nesi-chat-input" rows="1" placeholder="Ask about NeSI HPC, storage, Slurm…"></textarea>
      <button id="nesi-chat-send" aria-label="Send">&#10148;</button>
    </div>
  `;

  function el(cls, parent) { const d = document.createElement("div"); d.className = cls; parent.appendChild(d); return d; }

  // Tiny markdown renderer: escapes HTML first, then code blocks, inline code,
  // bold, [n] citations, lists, paragraphs. Enough for model output.
  function render(md, sources) {
    let h = md.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const blocks = [];
    h = h.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => { blocks.push(code); return `\x00${blocks.length - 1}\x00`; });
    h = h.replace(/`([^`]+)`/g, "<code>$1</code>")
         .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
         .replace(/\[(\d+)\]/g, (_, n) => {
           const s = sources && sources[n - 1];
           return s ? `<sup class="nesi-chat-cite" data-url="${s.url}" title="${(s.title || "").replace(/"/g, "&quot;")}">[${n}]</sup>` : `[${n}]`;
         })
         .replace(/^[-*] (.+)$/gm, "<li>$1</li>")
         .replace(/(<li>[\s\S]*?<\/li>)(?!\s*<li>)/g, "<ul>$1</ul>");
    h = h.split(/\n{2,}/).map((p) => /^<(ul|pre)/.test(p.trim()) ? p : `<p>${p.replace(/\n/g, "<br>")}</p>`).join("");
    h = h.replace(/\x00(\d+)\x00/g, (_, i) => `<pre><code>${blocks[i]}</code></pre>`);
    return h;
  }

  async function send() {
    const input = win.querySelector("#nesi-chat-input");
    const sendBtn = win.querySelector("#nesi-chat-send");
    const messages = win.querySelector("#nesi-chat-messages");
    const keyInput = win.querySelector("#nesi-chat-key");

    const question = input.value.trim();
    if (!question || sending) return;
    sending = true; sendBtn.disabled = true;
    input.value = ""; input.style.height = "auto";

    el("nesi-chat-msg nesi-chat-msg-user", messages).textContent = question;
    const botMsg = el("nesi-chat-msg nesi-chat-msg-bot", messages);
    botMsg.innerHTML = '<span class="nesi-chat-thinking">Searching the docs…</span>';
    messages.scrollTop = messages.scrollHeight;

    let answer = "", sources = [];
    try {
      const key = keyInput.value.trim();
      if (key) localStorage.setItem(KEY_STORAGE, key);
      const headers = { "Content-Type": "application/json" };
      if (key) headers["Authorization"] = "Bearer " + key;

      const res = await fetch(`${API_BASE}/api/chat`, { method: "POST", headers, body: JSON.stringify({ question, history }) });
      if (!res.ok) throw new Error((await res.json().catch(() => ({}))).error || `HTTP ${res.status}`);

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buf = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buf += decoder.decode(value, { stream: true });
        const lines = buf.split("\n"); buf = lines.pop();
        for (const line of lines) {
          if (!line.startsWith("data: ")) continue;
          const ev = JSON.parse(line.slice(6));
          if (ev.type === "sources") sources = ev.sources;
          if (ev.type === "token") { answer += ev.text; botMsg.innerHTML = render(answer, sources); messages.scrollTop = messages.scrollHeight; }
        }
      }
      if (sources.length) {
        const det = document.createElement("details");
        det.className = "nesi-chat-sources";
        det.innerHTML = `<summary>${sources.length} sources</summary>` + sources.map((s, i) =>
          `<a href="${s.url}" target="_blank" rel="noopener">[${i + 1}] ${s.title} — ${s.heading}</a>`).join("");
        botMsg.appendChild(det);
      }
      history.push({ role: "user", content: question }, { role: "assistant", content: answer });
      if (history.length > 12) history.splice(0, history.length - 12);
    } catch (err) {
      botMsg.innerHTML = `<p class="nesi-chat-error">Error: ${err.message}</p>`;
    } finally {
      sending = false; sendBtn.disabled = false;
      input.focus();
      messages.scrollTop = messages.scrollHeight;
    }
  }

  window.addEventListener("DOMContentLoaded", () => {
    document.body.appendChild(win);
    document.body.appendChild(fab);

    const keyInput = win.querySelector("#nesi-chat-key");
    keyInput.value = localStorage.getItem(KEY_STORAGE) || "";

    win.querySelector("#nesi-chat-messages").addEventListener("click", (e) => {
      if (e.target.matches(".nesi-chat-cite")) window.open(e.target.dataset.url, "_blank");
    });
    win.querySelector("#nesi-chat-send").addEventListener("click", send);
    win.querySelector("#nesi-chat-input").addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); send(); }
    });
    win.querySelector("#nesi-chat-input").addEventListener("input", (e) => {
      e.target.style.height = "auto"; e.target.style.height = e.target.scrollHeight + "px";
    });

    fab.addEventListener("click", () => {
      const open = win.classList.toggle("nesi-chat-open");
      if (open) win.querySelector("#nesi-chat-input").focus();
    });
  });
})();
