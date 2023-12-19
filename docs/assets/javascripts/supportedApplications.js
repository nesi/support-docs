jQuery(document).ready(function() {

    params = new URL(document.location).searchParams;
    search_string = params.get("search");
    cluster_tags = (params.get("cluster") ?? "").split(",");
    domain_tags = (params.get("domain") ?? "").split(",");    
    
    cluster_tags.forEach((tag)=>addTag(tag, "cluster"));
    domain_tags.forEach((tag)=>addTag(tag, "domain"));

    if (search_string){
        $('#srchbar')[0].value = search_string;
    }
    srchFunc();
})


/* <button type="button" class="close" data-dismiss="alert" aria-label="Close">
<span aria-hidden="true">&times;</span>
</button> */
//<span class="badge badge-domain badge-domain-${domain}">${domain_spaces}</span>`


function addTag(tag, type){
    $(`#srchbar-badge-party-${type}s`).append(() => {
        return `<span class="badge badge-closeable badge-${type} badge-${type}-${tag}">${tag.charAt(0).toUpperCase() + tag.replace('_', ' ').slice(1)}<button type="button" onclick="${type}ToggleFilter(\'${tag}\')" data-dismiss="alert" aria-label="Close"></button></span>`;
    })
    params.set(type, params.get(type).split(",").append(tag).toString())
}

function removeTag(tag, type){
    $(`#srchbar-badge-party-${type}s > .badge-${type}-${tag}`).remove()
    params.set(type, params.get(type).split(",").filter(e => e !== tag).toString())
}

function domainToggleFilter(domain) {
    if ($(`#srchbar-badge-party-domains > .badge-domain-${domain}`).length < 1) {
        addTag(domain, "domain");
    } else {
        removeTag(domain, "domain");
    }
    filterSearch(); // just to avoid multiple uneeded calls at start.
}

function clusterToggleFilter(cluster) {
    if ($(`#srchbar-badge-party-domains > .badge-cluster-${cluster}`).length < 1) {
        addTag(cluster, "cluster");
    } else {
        removeTag(cluster, "cluster");
    }
    filterSearch(); // just to avoid multiple uneeded calls at start.
}

//Removes badge from srcbar and re-filter
// function removeClusterFilter(self) {
//     let name = $(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_');
//     params.set("cluster", params.get("cluster").split(",").filter(e => e !== name).toString())
//     $(self).parent().remove();
//     filterSearch();
// }

// function removeDomainFilter(self) {
//     let name = $(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_');
//     params.set("domain", params.get("domain").split(",").filter(e => e !== name).toString());
//     $(self).parent().remove();
//     filterSearch();
// }

function srchFunc(event) {


    // Function called whenever search field edited.
    // Consider replacing with Fuse, if fuzzy or faster search needed.
    // Check if search string matches canon domain.

    filterSearch()
}

//Goes through each app and shows/hides accordingly.
function filterSearch() {
    //Make array of cannonical domain filters
    // $($(`#srchbar-badge-party-domains`)[0].children).each(function () {
    //     domain_array.push($(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_'))
    // })
    // $($(`#srchbar-badge-party-clusters`)[0].children).each(function () {
    //     cluster_array.push($(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_'))
    // })

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

    $('.list-group-item-application').each(function() { // Get list members.
        element = $(this)
        comptxt = (element.text() ?? "").toLowerCase(); // Flatten content
        $(element).removeClass('hide_search'); //Show all element    
        // If element matches all contitions, leave visible and skip to next element
        if (matchClasses(element, domain_tags) && matchClasses(element, cluster_tags) && (comptxt.indexOf(search_string) > -1)) {
            console.log(`${element} is visible`);
            return true
        }
        element.addClass('hide_search'); //Hides element
    });
    //Stop propigation of clicks to their parent elements.
    $(".badge-largeinator").click(function(event) {
        event.stopPropagation();
    });
}