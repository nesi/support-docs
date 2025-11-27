const CALENDAR_ID = "c_hen6rr02et39kat2hmuamidots@group.calendar.google.com";


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

async function showCalendarBanner() {
    const text = await fetch("docs/assets/training_calendar.ics")
        .then(r => r.ok ? r.text() : "");
    if (!text) { console.warn("failed to load calendar ") };

    // Get all VEVENT blocks in the simplest way

    for (const t in text.matchAll(/DTSTART.*:(\d+)/)) {
        if (!t) continue;

        d = new Date(t);
        // Parse date of event.
        // const d = new Date(
        //     `${start.slice(0, 4)}-${start.slice(4, 6)}-${start.slice(6, 8)}T${start.slice(9, 11) || "00"}:${start.slice(11, 13) || "00"}:${start.slice(13, 15) || "00"}`
        // );

        // if today
        if (now.getUTCDate() == d.getUTCDate()) {
            // if not finished.
            if (new Date(now + 3600000) < d) {
                // if not started
                if (now < d) {
                    console.log("Office hours later today");
                    addBanner(`Office Hours later today ${d.toLocaleTimeString()} <a href="https://nesi.zoom.us/j/83987449505?pwd=TzlYTk9pdGJXZFZVSUxhUFUyeFYrUT09">Join Zoom Meeting Now</a>`);

                } else {
                    console.log("Office hours NOW");
                    addBanner(`Office hours on now. <a href="https://nesi.zoom.us/j/83987449505?pwd=TzlYTk9pdGJXZFZVSUxhUFUyeFYrUT09">Join Zoom Meeting Now</a>`);
                }
            }

        }
        // If not in future skip.
        if (now.getUTCDate() > d.getUTCDate()) { 
            //console.log("no office hours today");
            continue;
            //#break; 
        }
    }
}

function addBanner(msg) {
    const banner = document.createElement("div");
    banner.id = "calendar-banner";
    banner.innerHTML = msg;

    const btn = document.createElement("button");
    btn.textContent = "×";
    btn.onclick = () => banner.remove();

    banner.appendChild(btn);
    document.body.prepend(banner);
}

showCalendarBanner();
