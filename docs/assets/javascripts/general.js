function changeVersion(app, machine, version, ){
    // Sets the module load example to use the selected version
    document.getElementById("mod_" + app + "_" + machine).innerHTML=version
    document.querySelectorAll(".md-tags-ver-" + app + "-" + machine + ">.md-tag-ver-shown").forEach((e) => e.classList.remove("md-tag-ver-shown"))
    document.getElementById("mod_" + app + "_" + machine + "_" + version).classList.add("md-tag-ver-shown")
    // ew. so gross
}