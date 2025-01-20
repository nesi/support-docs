window.onload = function() {
    update();
}

MAX_ENTRIES = 100;

async function update() {
    const feedList = document.getElementById("md-feed__inner");
    const rss_feeds = [
        `${window.location.origin}/software_updates.xml`,
        `${window.location.origin}/page_update.xml`,
        `${window.location.origin}/page_creation.xml`,
        "https://status.nesi.org.nz/history.rss"
    ];
    
    let allChannel = [];

    // Fetch and process all feeds
    try {
        await Promise.all(rss_feeds.map(async (feed) => {
            const response = await fetch(feed);
            if (!response.ok) {
                console.error(`Failed to fetch channel: ${feed}`);
                return;  // Skip this feed if there's an error
            }

            const xmlString = await response.text();
            const parser = new DOMParser();
            const dom = parser.parseFromString(xmlString, "text/xml");

            const channelName = dom.querySelector("channel > title")?.textContent || "";
            
            dom.querySelectorAll("item").forEach(item => {
                const pubDateText = item.querySelector("pubDate")?.textContent;

                // catClass = item.querySelectorAll("category").forEach(x=> {
                //     return { key: x.getAttribute("domain"), val: x.innerHTML }
                // });

                allChannel.push({
                    date: new Date(pubDateText),
                    channel: channelName,
                    link: item.querySelector("link")?.textContent || "",
                    channelUrl: feed,
                    title: item.querySelector("title")?.textContent || "", 
                    description: item.querySelector("description")?.textContent || "", 
                });
            });
        }));
    } catch (error) {
        console.error("Error fetching or parsing feeds: ", error);
    }

    // Sort feeds by publication date
    allChannel.sort((a, b) => b.date - a.date);

    let htmlContent = "";
    // Collect all innerHTML content before updating the DOM to minimize reflows
    allChannel.array.slice(0, MAX_ENTRIES).forEach(f => {
        try{  

            title = `<h3>${f.title}</h3>`;
            if (f.link){
                title = `<a class="md-feed-title" href="${f.link}">${title}</a>`
            }
            htmlContent += `
                <div class="md-feed-item">
                    ${title}
                    <div class="md-feed-description"><p>${f.description}</p></div>
                    <div>
                    <span class="md-icon md-feed-date" title="Date">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21 13.1c-.1 0-.3.1-.4.2l-1 1 2.1 2.1 1-1c.2-.2.2-.6 0-.8l-1.3-1.3c-.1-.1-.2-.2-.4-.2m-1.9 1.8-6.1 6V23h2.1l6.1-6.1-2.1-2M12.5 7v5.2l4 2.4-1 1L11 13V7h1.5M11 21.9c-5.1-.5-9-4.8-9-9.9C2 6.5 6.5 2 12 2c5.3 0 9.6 4.1 10 9.3-.3-.1-.6-.2-1-.2s-.7.1-1 .2C19.6 7.2 16.2 4 12 4c-4.4 0-8 3.6-8 8 0 4.1 3.1 7.5 7.1 7.9l-.1.2v1.8Z"></path></svg>
                    <span>${f.date.toLocaleDateString()} via <a target="_blank" href="${f.channelUrl}">${f.channel}</a></span>
                    </span>
                    </span>
                    </div>
                </div>`;
            console.log(f);

        }catch (error) {
                    console.error("Error fetching or parsing feeds: ", error);
    }
    });
    feedList.innerHTML = htmlContent;  // Update the DOM once with all content
}
