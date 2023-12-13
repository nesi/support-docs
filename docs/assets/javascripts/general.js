function changeVersion(version){
    // Sets the module load example to use the selected version
    document.getElementById('mod__ver').innerHTML=version
    document.querySelectorAll(".md-tag-ver-shown").forEach((e) => e.classList.remove("md-tag-ver-shown"))
    document.querySelectorAll("#mod__ver__" + version ).forEach((e) => e.classList.add("md-tag-ver-shown"))
    // ew. so gross
}
