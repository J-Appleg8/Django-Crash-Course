var roster = [];

// ADD A NEW STUDENT
function addNew() {
  var name = prompt("What name would you like to add? ");
  roster.push(name);
}

// REMOVE STUDENT
function removeStudent() {
  var name = prompt("Please enter the student's name you would like to remove");
  var index = roster.indexOf(name);
  if (index > -1) {
    roster.splice(index, 1);
  }
}

// DISPLAY ROSTER
function displayRoster() {
  console.log(roster);
}

var start = prompt("Would you like to start the roster web app? y/n");
var request = "empty";

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
if (start === "y") {
  while (request !== "quit") {
    var request = prompt(
      "Please select an action: add, remove, display, or quit."
    );

    if (request === "add") {
      addNew();
    } else if (request === "remove") {
      removeStudent();
    } else if (request === "display") {
      displayRoster();
    }
  }
}

alert("Thanks for using the Web App! Please refresh the page to start over.");
