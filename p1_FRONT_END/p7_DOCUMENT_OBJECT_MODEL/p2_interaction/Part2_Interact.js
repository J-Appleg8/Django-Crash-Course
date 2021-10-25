// var p = document.querySelector("p")
// p.textContent = "new text"
// p.innerHTML = "<strong>Im Bold</strong>"

// var special = document.querySelector("#special")

var x = document.querySelector("p");

// Show Text
x.textContent;

// Reassign Text
x.textContent = "new";

// Show actual HTML
x.innerHTML;

// Edit HTML
x.innerHTML = "This is <strong>BOLD</strong>";

//////////////////
// Attributes

var special = document.querySelector("#special");
var specialA = special.querySelector("a");

specialA.getAttribute("href");
specialA.setAttribute("href", "https://www.amazon.com");
