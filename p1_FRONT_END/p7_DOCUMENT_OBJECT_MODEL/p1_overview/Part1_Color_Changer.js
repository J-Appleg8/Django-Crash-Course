// Type this into your console:
// Grab the Header with h1
// Then you can interface with the object.

var header = document.querySelector("h1");

header.style.color = "red";

// Random Color Function:
// http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
// From letters - function creates random hex codes
// Then changes the header style on an interval

function getRandomColor() {
  var letters = "0123456789ABCDEF";
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function changeHeaderColor() {
  colorInput = getRandomColor();
  header.style.color = colorInput;
}

setInterval("changeHeaderColor()", 500);
