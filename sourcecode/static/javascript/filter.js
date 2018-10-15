filterDisable = document.getElementById("filterDisableButton")
filterActivate = document.getElementById("filterActivateButton")

filterDisable.addEventListener("click", function(){
  // document.getElementById('filterContainer').classList.add("invisibleFilter");
  window.location.replace("/pokedex")
});

filterActivate.addEventListener("click", function(){
  document.getElementById('filterContainer').classList.remove("invisibleFilter");
});
