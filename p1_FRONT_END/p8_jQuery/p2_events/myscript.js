$("h1").click(function () {
  $(this).text("You sit on a throne of lies");
});

$("#beef").click(function () {
  $(this).text("You smell like beef and cheese you dont smell like Santa");
});

$("input")
  .eq(0)
  .keypress(function (event) {
    if (event.which === 13) {
      $("h3").toggleClass("turnBlue");
    }
  });

// on() Method
$("h1").on("dblclick", function () {
  $(this).toggleClass("turnBlue");
});

$("#beef").on("mouseenter", function () {
  $(this).toggleClass("turnBlue");
});

// Events and Animations
$("input")
  .eq(1)
  .on("click", function () {
    $(".container").fadeOut(3000);
  });
