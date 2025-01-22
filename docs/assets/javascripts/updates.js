// window.onload = function() {
//     update();
// }

MAX_ENTRIES = 150;
$(document).ready(async function() {

    params = new URL(document.location).searchParams;
    // searchParams = params.get("search");
    filterParams = (params.get("filter") ?? "").split(",").filter(Boolean);

    filterParams.forEach((tag)=>addBadge(tag));
    await mergeFeed();
    filterSearch(); 
})

function filterSearch(){
    $(".md-throbber").show();
    let filterParams = (params.get("filter") ?? "").split(",").filter(Boolean)
    // only show nav element if filter in use.
    if (filterParams.length > 0){
        $("#md-filter__options").show();
    }else{
        $("#md-filter__options").hide();
    }
    let visibleCount = 0;
    $('#md-feed__inner').children().each(function(i) {
        if (visibleCount < MAX_ENTRIES && (filterParams.length < 1 || filterParams.some(x => $(this).hasClass(`md-category-${x}`)))) {
            $(this).show();
            visibleCount++;
        } else {
            $(this).hide();
        }
    });
    $(".md-throbber").hide();
}



function addBadge(tag){ 
    $(`#md-filter-tag-container`).append(() => {
    return `<span class="md-tag md-tag-closeable badge-${slugify(tag)}">${tag}<button type="button" onclick="removeTag(\'${tag}\')" data-dismiss="alert" aria-label="Close"><svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#5f6368"><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z"/></svg></button></span>`;
    })
}

function removeBadge(tag){
    $(`#md-filter-tag-container > .badge-${slugify(tag)}`).remove(); // Remove tag class from DOM
}

function addTag(tag){
    if ((params.get("filter") ?? "").split(",").includes(slugify(tag))){
        // if already contains tag. remove it instead.
        removeTag(tag);
        return
    }
    addBadge(tag);
    params.set('filter', (params.get('filter') ?? "").split(",").filter(Boolean).concat(slugify(tag)).join());
    history.pushState(null, '', window.location.pathname + '?' + params.toString());
    filterSearch();
}

function removeTag(tag){
    removeBadge(tag);
    const slugifiedTag = slugify(tag);
    params.set('filter', (params.get('filter') ?? "").split(",").filter(Boolean).filter(e => e !== slugifiedTag).join()); // Remove tag class from search string
    history.pushState(null, '', window.location.pathname + '?' + params.toString()); // push to search history for live update.
    filterSearch();
}


// Todo, make this aysnc.
async function mergeFeed() {
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
                    categories:  (Array.from(item.querySelectorAll("category"))).map(x=> x.innerHTML).concat([channelName]),
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

    // Collect all innerHTML content before updating the DOM to minimize reflows
    allChannel.forEach(f => {
        try{  
            title = `<h3>${f.title}</h3>`;
            let classes = "md-feed-item";
            f.categories.forEach(cat => classes+= " md-category-" + slugify(cat));
            if (f.link){
                title = `<a class="md-feed-title" href="${f.link}">${title}</a>`
            }
            let htmlContent = `
                <div class="${classes}" style='display:none'>
                    ${title}
                    <div class="md-feed-description"><p>${f.description}</p></div>
                    <nav class="md-tags">
                    ${f.categories.map(x => `<button onclick="addTag('${x}')" class=\"md-tag md-tag-clickable\">${x}</button>` ).join("")}
                    </nav>
                    <div>
                    <span class="md-icon md-feed-date" title="Date">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21 13.1c-.1 0-.3.1-.4.2l-1 1 2.1 2.1 1-1c.2-.2.2-.6 0-.8l-1.3-1.3c-.1-.1-.2-.2-.4-.2m-1.9 1.8-6.1 6V23h2.1l6.1-6.1-2.1-2M12.5 7v5.2l4 2.4-1 1L11 13V7h1.5M11 21.9c-5.1-.5-9-4.8-9-9.9C2 6.5 6.5 2 12 2c5.3 0 9.6 4.1 10 9.3-.3-.1-.6-.2-1-.2s-.7.1-1 .2C19.6 7.2 16.2 4 12 4c-4.4 0-8 3.6-8 8 0 4.1 3.1 7.5 7.1 7.9l-.1.2v1.8Z"></path></svg>
                    <span>${f.date.toLocaleString()} via <a title="Show RSS" target="_blank" href="${f.channelUrl}">${f.channel}</a></span>
                    </span>
                    </span>
                    </div>
                </div>`;
            $("#md-feed__inner").append(htmlContent);  // Update the DOM once with all content
        }catch (error) {
                    console.error("Error fetching or parsing feeds: ", error);
    }
    });
}

function slugify(str) {
    str = str.replace(/^\s+|\s+$/g, '');
    str = str.toLowerCase();
    str = str.replace(/[^a-z0-9 -]/g, '')
             .replace(/\s+/g, '-') 
             .replace(/-+/g, '-');
    return str;
}
