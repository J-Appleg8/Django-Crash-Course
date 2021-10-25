// Changing CSS Styling

var x = $("h1");

var newCSS = {
  color: "white",
  background: "blue",
  border: "2px solid red",
};

x.css(newCSS);

var listItems = $("li");
listItems.css("color", "blue");
listItems.eq(0).css("color", "orange");
listItems.eq(-1).css("color", "yellow");

// Changing HMTL Text and Elements
$("h1").text();
$("h1").text("Brand new text");
$("h1").html("<em>NEW</em>");

// Changing input boxes and attributes
$("input").eq(1).attr("type", "checkbox");
$("input").eq(0).val("Hi");

// Toggles CSS Class on and off if run and re-run
$("h1").toggleClass("turnBlue");
