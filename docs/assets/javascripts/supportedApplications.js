jQuery(document).ready(function () {
    pageLoad();
})

function pageLoad(){
    canon_domains=[];
    //canon_domains = yaml.load(fs.readFileSync('domains.yml', 'utf8'));
    getSearch();
}

function getSearch() { // Check if search string speified in URL

    const searchString = window.location.search.substr(1); // Get from window

    if (searchString.length > 0) { // if valid
        $('#srchbar')[0].value = searchString; // add to searchbar
        srchFunc(); 
    }
}

/* <button type="button" class="close" data-dismiss="alert" aria-label="Close">
<span aria-hidden="true">&times;</span>
</button> */
//<span class="badge badge-domain badge-domain-${domain}">${domain_spaces}</span>`
function addDomainFilter(domain) {
    if ($(`#srchbar-badge-party-domains > .badge-domain-${domain}`).length < 1) {
        $('#srchbar-badge-party-domains').append(() => {
            return `<span class="badge badge-closeable badge-domain badge-domain-${domain}">${domain.replace('_', ' ')}<button type="button" onclick="removeFilter(this)" data-dismiss="alert" aria-label="Close"></button></span>`;
        })
    } else {
        $(`#srchbar-badge-party-domains > .badge-domain-${domain}`).remove()
    }

    filterSearch();
}
function addClusterFilter(cluster, formatname) {
    if ($(`#srchbar-badge-party-clusters > .badge-cluster-${cluster}`).length < 1) {
        $('#srchbar-badge-party-clusters').append(() => {
            return `<span class="badge badge-closeable badge-cluster badge-cluster-${cluster}">${formatname}<button type="button" onclick="removeFilter(this)" data-dismiss="alert" aria-label="Close"></button></span>`;
        })
    } else {
        $(`#srchbar-badge-party-clusters > .badge-cluster-${cluster}`).remove()
    }
    filterSearch();
}
//Removes badge from srcbar and re-filter
function removeFilter(self) {
    $(self).parent().remove();
    filterSearch();

}

function srchFunc(event) {
    // Function called whenever search field edited.
    //Consider replacing with Fuse, if fuzzy or faster search needed.
    // Check if search string matches canon domain.
    string_normal = $('#srchbar')[0].value.toLowerCase();
    console.log(`Calling Search Function ${string_normal}`);

    if (event == undefined || event.key == " " || event.key == "Enter") {
        canon_domains.forEach((domain) => {
            match_pos = string_normal.search(domain.replace('_', ' '));
            if (match_pos != -1) {
                $('#srchbar')[0].value = string_normal.replace(domain, '');
                addDomainFilter(domain)
            }
        })
    }
    filterSearch()
}

//Goes through each app and shows/hides accordingly.
function filterSearch() {
    //Make array of cannonical domain filters
    domain_array = [];
    cluster_array = [];
    $($(`#srchbar-badge-party-domains`)[0].children).each(function () {
        domain_array.push($(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_'))
    })
    $($(`#srchbar-badge-party-clusters`)[0].children).each(function () {
        cluster_array.push($(this).attr('class').split(' ').slice(-1)[0].split('-')[2].replace(' ', '_'))
    })

    function matchClasses(element, inarray) {
        //Only doing this as extreme DRY
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

    string_normal = $('#srchbar')[0].value.toLowerCase()
    $('.list-group-item-application').each(function () { // Get list members.
        element = $(this)
        comptxt = element.text(); // Flatten content
        $(element).removeClass('hide_search'); //Show all element    
        //console.log([matchClasses(element,"domain", domain_array),matchClasses(element,"cluster", cluster_array),comptxt.toLowerCase().indexOf(string_normal) > -1])
        // If element matches all contitions, leave visible and skip to next element
        //console.log([matchClasses(element, domain_array), matchClasses(element, cluster_array), (comptxt.toLowerCase().indexOf(string_normal) > -1)]);
        if (matchClasses(element, domain_array) && matchClasses(element, cluster_array) && (comptxt.toLowerCase().indexOf(string_normal) > -1)) {
            console.log(`${element} is visible`);
            return true
        }
        element.addClass('hide_search'); //Hides element

        // if($(`#srchbar-badge-party-domains`).children().length > 1){
        //     //if this domain is selected.
        //     if($(`#srchbar-badge-party-domains > .badge-domain-${domain}`).length > 1){
        //         return true;
        //     }
        // }else{
        //     return true;
        // }

    });
    //Stop propigation of clicks to their parent elements.
    $(".badge-largeinator").click(function (event) {
        event.stopPropagation();
    });
}

// function toggleCluster() { // Called by cluster toggle buttons.
//     setTimeout(function () { // Must fire after button state changed. Token timeout.
//         $('.list-group-item-application').addClass('hide_cluster'); // Hide all
//         if ($('.btn-cluster-mahuika').hasClass('active')) { // Is button active.
//             $('.list-group-item-application-mahuika').removeClass('hide_cluster');
//         }
//         if ($('.btn-cluster-maui').hasClass('active')) {
//             $('.list-group-item-application-maui').removeClass('hide_cluster');
//         }
//     }, 1);
// }