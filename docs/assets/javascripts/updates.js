// Merges several RSS feeds into the updates page, newest first.
// Filter with ?filter=tag1,tag2 (slugified category or channel names).
// Wrapped so its names don't clash with globals from other site scripts
// (supportedApplications.js, loaded on every page, defines its own render()).
(() => {

    // Items shown at first, and added by each "Show more". How many are shown is kept per URL in
    // sessionStorage, so coming back to the page shows the same items. (Not history.state:
    // Material's instant navigation overwrites it with the scroll position.)
    const PAGE_SIZE = 50;

    // Paths are relative to the site root (base_url), so the page also works on preview deploys.
    const LOCAL_FEEDS = ["software_updates.xml", "page_update.xml", "page_creation.xml"];
    const REMOTE_FEEDS = ["https://status.nesi.org.nz/history.rss"];

    // Feed descriptions may contain HTML (the status page uses it). Only these tags are kept.
    const ALLOWED_TAGS = new Set(["P", "BR", "SMALL", "STRONG", "B", "EM", "I", "VAR", "CODE", "UL", "OL", "LI", "A"]);

    let entries = [];
    let matching = [];  // entries passing the current filter
    let shown = 0;      // how many of them are on the page

    document.addEventListener("DOMContentLoaded", async () => {
        const feed = document.getElementById("md-feed");
        const baseUrl = new URL(feed.dataset.baseUrl.replace(/\/?$/, "/"), document.baseURI);
        const feeds = LOCAL_FEEDS.map(f => new URL(f, baseUrl).href).concat(REMOTE_FEEDS);

        document.getElementById("md-feed__inner").addEventListener("click", (event) => {
            const tag = event.target.closest("[data-tag]");
            if (tag) toggleTag(tag.dataset.tag);
        });
        document.getElementById("md-filter-tag-container").addEventListener("click", (event) => {
            const button = event.target.closest("[data-remove-tag]");
            if (button) toggleTag(button.dataset.removeTag);
        });
        document.getElementById("md-feed-more").addEventListener("click", showMore);
        window.addEventListener("popstate", render);

        entries = await mergeFeeds(feeds);
        render();
        // Material saves the scroll position as history.state.y, but restores it before the
        // items have loaded, so restore it again now they have.
        if (history.state?.y) window.scrollTo(0, history.state.y);
    });

    function storageKey() {
        return `updates-shown:${location.search}`;
    }

    function loadShown() {
        try {
            return parseInt(sessionStorage.getItem(storageKey()), 10) || PAGE_SIZE;
        } catch {
            return PAGE_SIZE;
        }
    }

    function saveShown() {
        try {
            sessionStorage.setItem(storageKey(), String(shown));
        } catch {
            // Storage blocked: the page still works, it just starts from PAGE_SIZE next time.
        }
    }

    function getFilter() {
        return (new URL(document.location).searchParams.get("filter") ?? "").split(",").filter(Boolean);
    }

    function setFilter(filter) {
        const url = new URL(document.location);
        if (filter.length) {
            url.searchParams.set("filter", filter.join());
        } else {
            url.searchParams.delete("filter");
        }
        history.pushState(null, "", url);
        try {
            sessionStorage.removeItem(storageKey());  // a new filter starts from the top
        } catch {
            // Storage blocked: nothing to clear.
        }
        render();
    }

    function toggleTag(tag) {
        const slug = slugify(tag);
        const filter = getFilter();
        setFilter(filter.includes(slug) ? filter.filter(x => x !== slug) : filter.concat(slug));
    }

    async function mergeFeeds(feeds) {
        // allSettled, so one unreachable feed doesn't drop the others.
        const results = await Promise.allSettled(feeds.map(readFeed));
        const merged = [];
        const seen = new Set();
        results.forEach((result, i) => {
            if (result.status === "rejected") {
                console.warn(`Skipping feed ${feeds[i]}: ${result.reason}`);
                return;
            }
            result.value.forEach(entry => {
                const key = `${entry.channel}|${entry.title}|${entry.date.getTime()}|${entry.categories.join()}`;
                if (!seen.has(key)) {
                    seen.add(key);
                    merged.push(entry);
                }
            });
        });
        return merged.sort((a, b) => b.date - a.date);
    }

    async function readFeed(feedUrl) {
        const response = await fetch(feedUrl);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const dom = new DOMParser().parseFromString(await response.text(), "text/xml");
        if (dom.querySelector("parsererror")) throw new Error("not valid XML");

        const channel = dom.querySelector("channel > title")?.textContent.trim() || "";
        const items = [];
        dom.querySelectorAll("item").forEach(item => {
            const date = new Date(item.querySelector("pubDate")?.textContent ?? "");
            if (isNaN(date)) return;
            items.push({
                date: date,
                channel: channel,
                channelUrl: feedUrl,
                link: item.querySelector("link")?.textContent.trim() || "",
                title: item.querySelector("title")?.textContent.trim() || "",
                description: item.querySelector("description")?.textContent || "",
                categories: Array.from(item.querySelectorAll("category"), c => c.textContent.trim())
                    .filter(Boolean).concat(channel ? [channel] : []),
            });
        });
        return items;
    }

    function render() {
        const filter = getFilter();

        const options = document.getElementById("md-filter__options");
        options.style.display = filter.length ? "" : "none";
        const badges = document.getElementById("md-filter-tag-container");
        badges.replaceChildren(...filter.map(makeBadge));

        matching = entries.filter(e => !filter.length || e.categories.some(c => filter.includes(slugify(c))));
        const visible = matching.slice(0, loadShown());
        shown = visible.length;
        document.getElementById("md-feed__inner").replaceChildren(...visible.map(makeEntry));
        document.querySelector(".md-throbber").style.display = "none";
        updateMore();
    }

    function showMore() {
        const items = matching.slice(shown, shown + PAGE_SIZE).map(makeEntry);
        document.getElementById("md-feed__inner").append(...items);
        shown += items.length;
        saveShown();
        updateMore();
        // Keyboard and screen reader users continue from the first new item.
        if (items.length) {
            items[0].tabIndex = -1;
            items[0].focus();
        }
    }

    function updateMore() {
        document.getElementById("md-feed-count").textContent = matching.length
            ? `Showing ${shown} of ${matching.length} updates`
            : "No updates match this filter.";
        const more = document.getElementById("md-feed-more");
        more.hidden = shown >= matching.length;
        more.textContent = `Show ${Math.min(PAGE_SIZE, matching.length - shown)} more`;
    }

    function makeBadge(slug) {
        const badge = el("span", "md-tag md-tag-closeable", slug);
        const close = el("button", "");
        close.type = "button";
        close.dataset.removeTag = slug;
        close.setAttribute("aria-label", `Remove filter ${slug}`);
        close.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg>`;
        badge.append(close);
        return badge;
    }

    function makeEntry(entry) {
        const item = el("div", "md-feed-item");

        let title = el("h3", "", entry.title);
        const link = safeUrl(entry.link);
        if (link) {
            const a = el("a", "md-feed-title");
            a.href = link;
            a.append(title);
            title = a;
        }
        item.append(title);

        if (entry.description.trim()) {
            const description = el("div", "md-feed-description");
            description.append(sanitize(entry.description));
            item.append(description);
        }

        const tags = el("nav", "md-tags");
        entry.categories.forEach(category => {
            const button = el("button", "md-tag md-tag-clickable", category);
            button.type = "button";
            button.dataset.tag = category;
            tags.append(button);
        });
        item.append(tags);

        const date = el("span", "md-icon md-feed-date");
        date.title = "Date";
        date.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21 13.1c-.1 0-.3.1-.4.2l-1 1 2.1 2.1 1-1c.2-.2.2-.6 0-.8l-1.3-1.3c-.1-.1-.2-.2-.4-.2m-1.9 1.8-6.1 6V23h2.1l6.1-6.1-2.1-2M12.5 7v5.2l4 2.4-1 1L11 13V7h1.5M11 21.9c-5.1-.5-9-4.8-9-9.9C2 6.5 6.5 2 12 2c5.3 0 9.6 4.1 10 9.3-.3-.1-.6-.2-1-.2s-.7.1-1 .2C19.6 7.2 16.2 4 12 4c-4.4 0-8 3.6-8 8 0 4.1 3.1 7.5 7.1 7.9l-.1.2v1.8Z"></path></svg>`;
        const source = el("a", "", entry.channel || entry.channelUrl);
        source.href = entry.channelUrl;
        source.target = "_blank";
        source.title = "Show RSS";
        const text = el("span", "", `${entry.date.toLocaleString()} via `);
        text.append(source);
        date.append(text);
        const footer = el("div", "");
        footer.append(date);
        item.append(footer);

        return item;
    }

    // Parse untrusted HTML without running it, then copy across only allowed tags
    // (and only http(s) links). Anything else is replaced by its text.
    function sanitize(html) {
        const parsed = new DOMParser().parseFromString(html, "text/html").body;
        const out = document.createDocumentFragment();
        const copy = (from, to) => {
            from.childNodes.forEach(node => {
                if (node.nodeType === Node.TEXT_NODE) {
                    to.append(node.textContent);
                } else if (node.nodeType === Node.ELEMENT_NODE && ALLOWED_TAGS.has(node.tagName)) {
                    const clean = document.createElement(node.tagName);
                    const href = node.tagName === "A" && safeUrl(node.getAttribute("href"));
                    if (href) clean.href = href;
                    copy(node, clean);
                    to.append(clean);
                } else if (node.nodeType === Node.ELEMENT_NODE && !["SCRIPT", "STYLE"].includes(node.tagName)) {
                    copy(node, to);
                }
            });
        };
        copy(parsed, out);
        return out;
    }

    function safeUrl(url) {
        try {
            const parsed = new URL(url, document.baseURI);
            return ["http:", "https:"].includes(parsed.protocol) ? parsed.href : "";
        } catch {
            return "";
        }
    }

    function el(tag, className, text) {
        const node = document.createElement(tag);
        if (className) node.className = className;
        if (text !== undefined) node.textContent = text;
        return node;
    }

    function slugify(str) {
        return str.trim().toLowerCase()
            .replace(/[^a-z0-9 -]/g, "")
            .replace(/\s+/g, "-")
            .replace(/-+/g, "-");
    }
})();
