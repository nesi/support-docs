async function displayOfficeHoursCalendar() {
    console.log("script added");
    const calendarDiv = document.getElementById('office-hours-calendar');
    const calendarP = document.getElementById('office-hours-calendar-message');
    const calendarButtons = document.getElementById('office-hours-buttons');

    if (!calendarDiv) return;

    const text = await fetch("/assets/training_calendar.ics")
        .then(r => r.ok ? r.text() : "");
    if (!text) {
        calendarP.innerHTML = 'Failed to load calendar.';
        return;
    }

    try {
        const jcal = ICAL.parse(text);
        const comp = new ICAL.Component(jcal);
        const events = comp.getAllSubcomponents('vevent').map(vevent => {
            const summary = vevent.getFirstPropertyValue('summary');
            const dtstart = vevent.getFirstPropertyValue('dtstart');
            const description = (vevent.getFirstPropertyValue('description') || '').replace(/\\n/g, '\n').replace(/\\,/g, ',');
            const urlMatch = description.match(/(https?:\/\/[^\s]+)/);
            const start = dtstart.toJSDate();
            return {
                title: summary,
                start,
                description,
                meetingLink: urlMatch ? urlMatch[1] : MEETING_LINK,
                day: start.toLocaleDateString('en-US', { weekday: 'long' }),
                date: start.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
                time: start.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })
            };
        });

        // Sort events by date
        events.sort((a, b) => a.start - b.start);
        // Filter to only events from today onwards
        const now = new Date();
        now.setHours(0,0,0,0); // Start of today
        const upcomingEvents = events.filter(event => event.start >= now);
        // Create table
        const tableWrap = document.createElement('div');
        tableWrap.className = 'md-typeset__table'
        const table = document.createElement('table');
        let rows = '';
        // Only next 6 upcoming events
        upcomingEvents.slice(0, 6).forEach(event => {
            rows += `
                <tr>
                    <td>${event.day}, ${event.date}</td>
                    <td>${event.time}</td>
                </tr>
            `;
        });
        table.innerHTML = `<tbody>${rows}</tbody>`;
        tableWrap.appendChild(table);
        calendarDiv.appendChild(tableWrap);
        calendarP.innerHTML = '';
        if (upcomingEvents.length > 0) {
            console.log(upcomingEvents[0]);
            calendarButtons.innerHTML=`<a href="webcal://assets/training_calendar.ics" download class="md-button md-button--addcal"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960"><path d="M680-80v-120H560v-80h120v-120h80v120h120v80H760v120h-80Zm-480-80q-33 0-56.5-23.5T120-240v-480q0-33 23.5-56.5T200-800h40v-80h80v80h240v-80h80v80h40q33 0 56.5 23.5T760-720v244q-20-3-40-3t-40 3v-84H200v320h280q0 20 3 40t11 40H200Zm0-480h480v-80H200v80Zm0 0v-80 80Z"/></svg>Add to Calendar</a></td><a href="${upcomingEvents[0].meetingLink}" class="md-button md-button--addcal"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#1f1f1f"><path d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h480q33 0 56.5 23.5T720-720v180l160-160v440L720-420v180q0 33-23.5 56.5T640-160H160Zm0-80h480v-480H160v480Zm0 0v-480 480Z"/></svg>Join Zoom Metting</a></td>`;
        } else {
            calendarButtons.innerHTML = 'No Upcoming Office Hours';
        }

        
    } catch (error) {
        console.error('Error parsing ICS:', error);
        calendarP.innerHTML = '<div class="admonition bug"><p class="admonition-title">Error loading Calendar.</p></div>';
    }
}
// Support both full page load and MkDocs AJAX navigation
window.addEventListener("load", displayOfficeHoursCalendar);
// For Material for MkDocs: listen for AJAX navigation events
if (typeof document$ !== 'undefined') {
    document$.subscribe(displayOfficeHoursCalendar);
}

