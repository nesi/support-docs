// Copied from module list repo.
CLUSTER_WHITELIST=["mahuika", "maui", "maui_ancil"]
DOMAIN_WHITELIST=["astronomy","biology","chemistry", "data_analytics", "earth_science", "engineering", "language", "machine_learning", 
"mathematics","medical_science","physics","social_science","visualisation","climate_science","workflow_management"]

$(document).ready(function() {

    params = new URL(document.location).searchParams;
    search_string = params.get("search");
    cluster_tags = (params.get("cluster") ?? "").split(",").filter(Boolean);
    domain_tags = (params.get("domain") ?? "").split(",").filter(Boolean);  

    cluster_tags.forEach((tag)=>addBadge(tag, "cluster"));
    domain_tags.forEach((tag)=>addBadge(tag, "domain"));

    if (search_string){
        $('#__search-aux')[0].value = search_string;
    }
    filterSearch(); 
})

function addBadge(tag, filter_type){ 
    $(`#srchbar-badge-party-${filter_type}s`).append(() => {
    return `<span class="badge badge-closeable badge-${filter_type} badge-${filter_type}-${tag}">${tag.charAt(0).toUpperCase() + tag.replace('_', ' ').slice(1)}<button type="button" onclick="${filter_type}ToggleFilter(\'${tag}\')" data-dismiss="alert" aria-label="Close"></button></span>`;
})
}

function removeBadge(tag, filter_type){
    $(`#srchbar-badge-party-${filter_type}s > .badge-${filter_type}-${tag}`).remove(); // Remove tag class from DOM
}

function addTag(tag, filter_type){
    addBadge(tag, filter_type);
    params.set(filter_type, (params.get(filter_type) ?? "").split(",").filter(Boolean).concat(tag).join());
    history.pushState(null, '', window.location.pathname + '?' + params.toString());
}

function removeTag(tag, filter_type){
    removeBadge(tag, filter_type);
    params.set(filter_type, (params.get(filter_type) ?? "").split(",").filter(Boolean).filter(e => e !== tag).join()); // Remove tag class from search string
    history.pushState(null, '', window.location.pathname + '?' + params.toString()); // push to search history for live update.
}

function domainToggleFilter(domain) {
    if (DOMAIN_WHITELIST.includes(domain)){
        if ($(`#srchbar-badge-party-domains > .badge-domain-${domain}`).length < 1) {
            addTag(domain, "domain");
        } else {
            removeTag(domain, "domain");
        }
        filterSearch();
    }
}

function clusterToggleFilter(cluster) {
    if (CLUSTER_WHITELIST.includes(cluster)){
        if ($(`#srchbar-badge-party-clusters > .badge-cluster-${cluster}`).length < 1) {
            addTag(cluster, "cluster");
        } else {
            removeTag(cluster, "cluster");
        }
        filterSearch(); 
    }
}


function srchFunc(event) {
    // Function called whenever search field edited.
    // Consider replacing with Fuse, if fuzzy or faster search needed.
    // Check if search string matches canon domain.
    search_string = $('#__search-aux')[0].value;
    params.set("search", search_string);
    // Rather that add to url, edit history.
    history.pushState(null, '', window.location.pathname + '?' + params.toString());
    filterSearch()
}

//Goes through each app and shows/hides accordingly.
function filterSearch() {
    function matchClasses(element, inarray) {
        // Only doing this as extreme DRY
        if (inarray.length < 1) {
            return true
        }
        for (i = 0; i < inarray.length; i++) {
            if (element.hasClass(`list-group-item-application-${inarray[i]}`)) {
                return true
            }
        }
        return false
    }

    function matchSearch(comptxt){
        if (search_string){
            return (comptxt.indexOf(search_string) > -1)
        }
        return true
    }

    $('.list-group-item-application').each(function() { // Get list members.
        element = $(this)
        comptxt = (element.text() ?? "").toLowerCase(); // Flatten content
        $(element).removeClass('hide_search'); //Show all element    
        // If element matches all contitions, leave visible and skip to next element
        if (matchClasses(element, domain_tags) && matchClasses(element, cluster_tags) && matchSearch(comptxt)) {
            return true
        }
        element.addClass('hide_search'); //Hides element
    });
}
//Stop propigation of clicks to their parent elements.
$(".badge-largeinator").click(function(event) {
    event.stopPropagation();
})
