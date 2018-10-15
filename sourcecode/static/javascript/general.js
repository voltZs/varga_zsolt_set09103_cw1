var dexTiles = document.querySelectorAll(".dexTile");

dexTiles.forEach(function(elem){
  elem.addEventListener("mouseenter", function(){
    elem.getElementsByClassName('LabelHolder')[0].classList.add("LabelHolderLit");
  });
  elem.addEventListener("mouseleave", function(){
    elem.getElementsByClassName('LabelHolder')[0].classList.remove("LabelHolderLit");
  });
});
