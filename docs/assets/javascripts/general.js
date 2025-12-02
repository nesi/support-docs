const CALENDAR_ID = "c_hen6rr02et39kat2hmuamidots@group.calendar.google.com";
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

async function showCalendarBanner() {
    const text = await fetch("/assets/training_calendar.ics")
        .then(r => r.ok ? r.text() : "");
    if (!text) { console.warn("failed to load calendar ") };


    const now = new Date();
    let allmatch = text.matchAll(/DTSTART:(\d+T\d+Z)/g);
    // Extract all dates.
    for (const t of allmatch) {
        if (!t) continue;
        let d = format8601(t[1]);
        // if today
        if (now.toDateString() == d.toDateString()) {
            // if not finished.
            if (now.getTime()  < d.getTime() + 3600000) {
                // if not started
                if (now < d) {
                    addBanner(`<p><a href="https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/">Weekly Online Office Hour</a> on today, starting ${d.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}. Drop in for any queries.`);

                } else {
                    addBanner(`<p><a href="https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/">Weekly Online Office Hour</a> on now.     <a href="${MEETING_LINK}">Join Zoom Meeting Now</a> for any queries.</p>`);
                }
            }
            break;
        }
    }
}

function addBanner(msg) {
    const banner = document.createElement("div");
    banner.id = "calendar-banner";
    banner.classList += "md-typeset"
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
        str.substring(6, 8) + 
        str.substring(8, 9) +
        str.substring(9, 11) + ':' + 
        str.substring(11, 13) + ':' +
        str.substring(13, 15) + 
        str.substring(15, 16);
    return new Date(dateStringFormatted);
}
showCalendarBanner();
