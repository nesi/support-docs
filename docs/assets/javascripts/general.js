const MEETING_LINK = "https://nesi.zoom.us/j/83987449505?pwd=TzlYTk9pdGJXZFZVSUxhUFUyeFYrUT09";

function changeVersion(app, version, warn = false) {
    // Sets the module load example to use the selected version
    document.getElementById("mod_" + app.toLowerCase() + "_code").innerHTML = `module load ${app}/${version}`
    document.querySelectorAll(".md-tags-ver-" + app.toLowerCase() + ">.md-tag-ver-shown").forEach((e) => e.classList.remove("md-tag-ver-shown"))
    document.getElementById("mod_" + app.toLowerCase() + "_" + version).classList.add("md-tag-ver-shown")
    if (warn) {
        document.getElementById("mod_" + app.toLowerCase() + "_warn").style.display = "block";
        document.getElementById("mod_" + app.toLowerCase() + "_warn").querySelector("p.warning-text").innerHTML = document.getElementById("mod_" + app.toLowerCase() + "_" + version).title;
    } else {
        document.getElementById("mod_" + app.toLowerCase() + "_warn").style.display = "none";
    }
    // ew. so gross
}

function toggle(id) {
    var item = document.getElementById(id);
    console.log(id);
    console.log(item);
    if (item) {
        if (item.classList.contains("hidden")) {
            item.classList.remove("hidden")
        }
        else {
            item.classList.add("hidden")
        }
    } else {
        console.log(item)
    }
}

async function showOfficeBanner() {
    const text = await fetch("/assets/training_calendar.ics")
        .then(r => r.ok ? r.text() : "");
    if (!text) { console.warn("failed to load calendar ") };

    const now = new Date();
    try {
        const jcal = ICAL.parse(text);
        const comp = new ICAL.Component(jcal);
        const vevents = comp.getAllSubcomponents('vevent');
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
                        addBanner(`<p><a href="https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/">Weekly Online Office Hour</a> on now.     <a href="${MEETING_LINK}">Join Zoom Meeting Now</a> for any queries.</p>`, "calendar-banner");
                    }
                }
                break;
            }
        }
    } catch (error) {
        console.warn("ICAL parsing failed", error);
    }
}


function addBanner(msg, id) {
    const banner = document.createElement("div");
    banner.id = id;
    banner.classList += "md-typeset ";
    banner.classList += "md-event-banner "
    banner.innerHTML = msg;

    const btn = document.createElement("button");
    btn.textContent = "×";
    btn.onclick = () => banner.remove();

    banner.appendChild(btn);
    document.body.prepend(banner);
}

// Formats ISO standard date string into Date object.
function format8601(str){
    const dateStringFormatted = 
        str.substring(0, 4) + '-' +
        str.substring(4, 6) + '-' +
        str.substring(6, 8) + 'T' +
        str.substring(9, 11) + ':' + 
        str.substring(11, 13) + ':' +
        str.substring(13, 15);
    return new Date(dateStringFormatted);
}

showOfficeBanner();

// Material's skip-link div (data-md-component="skip") sits directly under
// <body>, before any landmark, so its "Skip to content" link is unreachable
// via landmark navigation. Wrap it in a <nav> landmark without touching the
// theme's own template.
const skipLink = document.querySelector('[data-md-component="skip"]');
if (skipLink) {
    const nav = document.createElement("nav");
    nav.setAttribute("aria-label", "Skip links");
    skipLink.replaceWith(nav);
    nav.appendChild(skipLink);
}

// Several of Material's checkbox-toggle widgets (nested nav sections in
// overrides/partials/nav-item.html, search overlay/icon in
// overrides/partials/search.html) have more than one clickable opener for
// the same checkbox. Only one opener per checkbox may be a real <label for>
// (otherwise the field has multiple labels), so the rest carry a
// data-md-toggle-checkbox="<id>" attribute and are wired up here instead.
function toggleCheckboxTarget(target) {
    const checkbox = document.getElementById(target.getAttribute("data-md-toggle-checkbox"));
    if (checkbox) {
        checkbox.checked = !checkbox.checked;
        checkbox.dispatchEvent(new Event("change", { bubbles: true }));
    }
}
document.addEventListener("click", (event) => {
    const target = event.target.closest("[data-md-toggle-checkbox]");
    if (target) {
        toggleCheckboxTarget(target);
    }
});
document.addEventListener("keydown", (event) => {
    if (event.key !== "Enter" && event.key !== " ") {
        return;
    }
    const target = event.target.closest("[data-md-toggle-checkbox]");
    if (target) {
        event.preventDefault();
        toggleCheckboxTarget(target);
    }
});

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

// Remove me later
// showOfficeBanner().then(() => {
//     if (!document.getElementById("calendar-banner")){
//         addBanner(`<p>Registrations now open for <a href=https://www.eventbrite.co.nz/e/introduction-to-high-performance-computing-hpc-carpentry-tickets-1984247473608>Introduction to HPC Carpentry Workshop</a> on 24th March from 10am to 3pm.</p>`, 'workshop-banner');
//     }
// });

