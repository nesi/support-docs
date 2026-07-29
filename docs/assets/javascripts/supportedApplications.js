// Populated (below, on document$) from #mainList's data-domain-whitelist,
// which the supported_apps.html template derives from module-list.json -
// this way it can never drift out of sync with the domains apps actually have.
let DOMAIN_WHITELIST = [];


const state = {
  search: "",
  domain: null // string | null
};

function syncURL() {
  const params = new URLSearchParams();

  if (state.search) {
    params.set("search", state.search);
  }

  if (state.domain) {
    params.set("domain", state.domain);
  }

  history.pushState(null, "", `?${params.toString()}`);
}

function renderDomainBadge() {
  const container = document.getElementById("srchbar-badge-party-domains");
  if (!container) return;

  container.innerHTML = "";

  if (!state.domain) return;

  const badge = document.createElement("span");

  badge.className = `badge badge-closeable badge-domain badge-domain-${state.domain}`;
  badge.dataset.domain = state.domain;

  badge.textContent = state.domain.replace(/_/g, " ").replace(/^./, c => c.toUpperCase());

  const close = document.createElement("button");
  close.type = "button";
  close.className = "badge-close";
  close.setAttribute("aria-label", "Clear domain filter");
  close.textContent = "✖";
  close.addEventListener("click", event => {
    event.stopPropagation();
    state.domain = null;
    syncURL();
    render();
  });

  badge.appendChild(close);
  container.appendChild(badge);
}

function render() {
  renderDomainBadge();
  filterSearch();
}

/* ============================================================================
 * Filtering
 * ========================================================================== */

function filterSearch() {
  const items = document.querySelectorAll(".list-group-item-application");

  items.forEach(item => {
    let visible = true;

    const text = item.dataset.searchText ?? "";

    const itemDomains =
      item.dataset.domains?.split(",") ?? [];

    if (state.domain) {
      visible &&= itemDomains.includes(state.domain);
    }

    if (state.search) {
      visible &&= text.includes(state.search.toLowerCase());
    }

    item.classList.toggle("hide_search", !visible);
  });
}

/* ============================================================================
 * Lazy card bodies
 *
 * Each card's body (versions, links, licence info) ships as an inert
 * <template>, not live markup - with ~860 apps, rendering all of that
 * upfront made the page ~27k DOM nodes and multiple seconds to load, even
 * though almost all of it stays collapsed and invisible. The template's
 * content is cloned in only the first time a card is actually expanded.
 * ========================================================================== */

function initLazyCardBody(details) {
  details.addEventListener("toggle", () => {
    if (!details.open) return;

    const tpl = details.querySelector(".card-body-template");
    if (!tpl) return; // Already expanded once, or none present.

    details.appendChild(tpl.content.cloneNode(true));
    tpl.remove();
  });
}

function toggleDomain(domain) {
  if (!DOMAIN_WHITELIST.includes(domain)) return;

  // Clicking the active domain clears it
  // Clicking a different domain replaces it
  state.domain = state.domain === domain ? null : domain;

  syncURL();
  render();
}


// Debounce input
let searchDebounceTimer = null;

function onSearchInput(event) {
  clearTimeout(searchDebounceTimer);

  searchDebounceTimer = setTimeout(() => {
    state.search = event.target.value ?? "";
    syncURL();
    filterSearch();
  }, 150);
}

// document$ (not DOMContentLoaded) so this re-initializes on Material's
// instant/SPA-style navigation too - not just a full page load. Without this,
// arriving via a link from elsewhere on the site never runs setup, and every
// card stays hidden behind its default 'hide_search' class.
document$.subscribe(() => {
  const mainList = document.getElementById("mainList");
  if (!mainList) return; // Not on the applications page.

  DOMAIN_WHITELIST = (mainList.dataset.domainWhitelist || "").split(",").filter(Boolean);

  const params = new URLSearchParams(window.location.search);

  state.search = params.get("search") ?? "";
  state.domain = params.get("domain");

  // Validate domain from URL
  if (!DOMAIN_WHITELIST.includes(state.domain)) {
    state.domain = null;
  }

  const searchInput = document.getElementById("__search-aux");
  searchInput.value = state.search;
  searchInput.addEventListener("input", onSearchInput);

  // Prevent bubbling from badge container
  document.querySelectorAll(".badge-largeinator").forEach(el => {
    el.addEventListener("click", event => {
      const badge = event.target.closest(".badge-largeinator");
      if (!badge) return;
      toggleDomain(badge.dataset.domain);
    });
    el.addEventListener("toggle", event => {
      event.stopPropagation();
      event.preventDefault();
    })
  });

  document.querySelectorAll(".list-group-item-application").forEach(initLazyCardBody);

  render();
});

/* ============================================================================
 * Public API (for existing onclick hooks)
 * ========================================================================== */

window.domainToggleFilter = toggleDomain;
window.onSearchInput = onSearchInput;

