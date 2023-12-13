function changeVersion(version){
    document.getElementById('mod__ver').innerHTML=version
    console.log(document.querySelectorAll(".md-tag-ver-shown")[0])
    document.querySelectorAll(".md-tag-ver-shown")[0].classList.remove("md-tag-ver-shown")
    document.getElementById("mod__ver__" + version ).classList.add("md-tag-ver-shown")
}
