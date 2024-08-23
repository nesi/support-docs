function changeVersion(app, version, warn = false){
    // Sets the module load example to use the selected version
    document.getElementById("mod_" + app.toLowerCase() + "_code").innerHTML=`module load ${app}/${version}`
    document.querySelectorAll(".md-tags-ver-" + app.toLowerCase() +">.md-tag-ver-shown").forEach((e) => e.classList.remove("md-tag-ver-shown"))
    document.getElementById("mod_" + app.toLowerCase() + "_" + version).classList.add("md-tag-ver-shown")
    if (warn){
        document.getElementById("mod_" + app.toLowerCase() + "_warn").style.display = "block";
        document.getElementById("mod_" + app.toLowerCase() + "_warn").querySelector("p.warning-text").innerHTML = document.getElementById("mod_" + app.toLowerCase() + "_" + version).title;
    }else{
        document.getElementById("mod_" + app.toLowerCase() + "_warn").style.display = "none";
    }

    // ew. so gross
}
function toggle(id){
    var item = document.getElementById(id);
    console.log(id);
    console.log(item);
    if (item){
        if (item.classList.contains("hidden"))
        {
           item.classList.remove("hidden")
        }
        else
        {
            item.classList.add("hidden")    
        }
    }else{
        console.log(item)
    }

  }
