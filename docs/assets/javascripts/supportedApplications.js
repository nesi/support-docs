const DOMAIN_WHITELIST = [
  "astronomy", "biology", "chemistry", "data_analytics",
  "earth_science", "engineering", "language", "machine_learning",
  "mathematics", "medical_science", "physics", "social_science",
  "visualisation", "climate_science", "workflow_management"
];


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

  badge.textContent =
    state.domain.charAt(0).toUpperCase() +
    state.domain.replace("_", " ").slice(1);

  const close = document.createElement("span");
  
  close.textContent = "✖"

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

    const text = item.textContent.toLowerCase();

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

document.addEventListener("DOMContentLoaded", () => {
  const params = new URLSearchParams(window.location.search);

  state.search = params.get("search") ?? "";
  state.domain = params.get("domain");

  // Validate domain from URL
  if (!DOMAIN_WHITELIST.includes(state.domain)) {
    state.domain = null;
  }

  const searchInput = document.getElementById("__search-aux");
  searchInput.value = state.search;
  searchInput.addEventListener("input", onkeyup);

  // // Badge close handling
  // document.addEventListener("click", event => {

  //   //event.stopPropagation();
  // });

  // Prevent bubbling from badge container
  document.querySelectorAll(".badge-largeinator").forEach(el => {
    el.addEventListener("click", event => 
    {
      event.stopPropagation();
      console.log(event);
      const badge = event.target.closest(".badge-largeinator");
      console.log(badge.dataset.domain);
      if (!badge) return;
      toggleDomain(badge.dataset.domain);
    }, true);
  });

  render();
});

/* ============================================================================
 * Public API (for existing onclick hooks)
 * ========================================================================== */

window.domainToggleFilter = toggleDomain;
