// Event Listeners
var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function () {
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = "red";
});

headOne.addEventListener("mouseout", function () {
  headOne.textContent = "Hover over Me!";
  headOne.style.color = "black";
});

headTwo.addEventListener("click", function () {
  headTwo.textContent = "Clicked On";
  headTwo.style.color = "blue";
});

headThree.addEventListener("dblclick", function () {
  headThree.textContent = "I Was Double Clicked!";
  headThree.style.color = "red";
});
