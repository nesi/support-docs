const BACKUP_MEETING_LINK = "https://reannz.zoom.us/j/84237671321?pwd=rLLqWtE2bwmKaD1yjJ1bp3CPhlfaw8.1";

function changeVersion(app, version, warn = false) {
    // Sets the module load example to use the selected version
    const appLower = app.toLowerCase();
    const versionEl = document.getElementById(`mod_${appLower}_${version}`);
    const warnEl = document.getElementById(`mod_${appLower}_warn`);

    document.getElementById(`mod_${appLower}_code`).innerHTML = `module load ${app}/${version}`
    document.querySelectorAll(`.md-tags-ver-${appLower}>.md-tag-ver-shown`).forEach((e) => e.classList.remove("md-tag-ver-shown"))
    versionEl.classList.add("md-tag-ver-shown")
    if (warn) {
        warnEl.style.display = "block";
        warnEl.querySelector("p.warning-text").innerHTML = versionEl.title;
    } else {
        warnEl.style.display = "none";
    }
}

function toggle(id) {
    var item = document.getElementById(id);
    if (item) {
        if (item.classList.contains("hidden")) {
            item.classList.remove("hidden")
        }
        else {
            item.classList.add("hidden")
        }
    }
}

// Shared by showOfficeBanner (this file) and displayOfficeHoursCalendar
// (officeHours.js) so both pull the same calendar data the same way.
// Returns the parsed vevent list, or null if the fetch/parse failed.
async function fetchCalendarEvents() {
    const text = await fetch("/assets/training_calendar.ics")
        .then(r => r.ok ? r.text() : "");
    if (!text) {
        console.warn("failed to load calendar");
        return null;
    }
    try {
        const jcal = ICAL.parse(text);
        const comp = new ICAL.Component(jcal);
        return comp.getAllSubcomponents('vevent');
    } catch (error) {
        console.warn("ICAL parsing failed", error);
        return null;
    }
}

async function showOfficeBanner() {
    if (document.getElementById("calendar-banner")) return;

    const vevents = await fetchCalendarEvents();
    if (!vevents) return;

    const now = new Date();
    for (const vevent of vevents) {
        const dtstart = vevent.getFirstPropertyValue('dtstart');
        const date = dtstart.toJSDate();
        // if today
        if (now.toDateString() == date.toDateString()) {
            // if not finished.
            if (now.getTime() < date.getTime() + 3600000) {
                // if not started
                if (now < date) {
                    addBanner(`<p><a href="https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/">Weekly Online Office Hour</a> on today, starting ${date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}. Drop in for any queries.`, "calendar-banner");
                } else {
                    addBanner(`<p><a href="https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/">Weekly Online Office Hour</a> on now.     <a href="${BACKUP_MEETING_LINK}">Join Zoom Meeting Now</a> for any queries.</p>`, "calendar-banner");
                }
            }
            break;
        }
    }
}


// Builds the same markup as Material's announcement bar (overrides/main.html),
// so both kinds of banner share the .md-banner styles in theme.css.
function addBanner(msg, id) {
    const banner = document.createElement("aside");
    banner.id = id;
    banner.classList.add("md-banner");

    const inner = document.createElement("div");
    inner.classList.add("md-banner__inner", "md-grid", "md-typeset");

    const btn = document.createElement("button");
    btn.classList.add("md-banner__button", "md-icon");
    btn.setAttribute("aria-label", "Close");
    btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>';
    btn.onclick = () => banner.remove();

    inner.appendChild(btn);
    inner.insertAdjacentHTML("beforeend", msg);
    banner.appendChild(inner);

    // Above the announcement bar, but after the skip link, so that stays the first thing keyboard users reach.
    const announce = document.querySelector("[data-md-component=announce]");
    if (announce) {
        announce.before(banner);
    } else {
        document.body.prepend(banner);
    }
}

// Support both full page load and Material's instant (SPA-style) navigation.
// document$ already emits for the initial page load, so calling showOfficeBanner()
// directly as well as subscribing it would run it twice on first load, appending
// two banners (its "already exists" guard runs before the async fetch resolves,
// so both calls pass it before either has appended anything).
if (typeof document$ !== 'undefined') {
    document$.subscribe(showOfficeBanner);
} else {
    showOfficeBanner();
}

// The status.nesi.org.nz (Statuspage) embed leaves its iframe both
// aria-hidden and tabindex="0" while collapsed, so keyboard users can
// tab into a widget screen readers can't see. Keep it out of the tab
// order whenever it's hidden; leave it alone once the widget opens
// (aria-hidden gets removed) and sets its own tabindex.
function fixStatuspageIframeFocus(iframe) {
    if (iframe.getAttribute("aria-hidden") === "true" && iframe.getAttribute("tabindex") !== "-1") {
        iframe.setAttribute("tabindex", "-1");
    }
}

// Fix whatever's already there (the embed script runs before this file).
document.querySelectorAll("iframe").forEach(fixStatuspageIframeFocus);

new MutationObserver((mutations) => {
    for (const mutation of mutations) {
        if (mutation.target.tagName === "IFRAME") {
            fixStatuspageIframeFocus(mutation.target);
        } else {
            mutation.addedNodes.forEach((node) => {
                if (node.tagName === "IFRAME") {
                    fixStatuspageIframeFocus(node);
                }
            });
        }
    }
}).observe(document.body, {
    attributeFilter: ["aria-hidden", "tabindex"],
    childList: true,
    subtree: true,
});

