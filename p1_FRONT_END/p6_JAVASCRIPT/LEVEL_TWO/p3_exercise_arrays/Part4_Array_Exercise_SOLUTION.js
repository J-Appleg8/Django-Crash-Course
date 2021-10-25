var roster = [];

// ADD A NEW STUDENT
function addNew() {
  var newName = prompt("What name would you like to add? ");
  roster.push(newName);
}

// REMOVE STUDENT
function remove() {
  var remName = prompt("What name would you like to remove?");
  var index = roster.indexOf(remName);
  roster.splice(index, 1);
}

// DISPLAY ROSTER
function display() {
  console.log(roster);
}

// Start by asking if they want to use the web app
var start = prompt("Would you like to start the roster web app? y/n");
var request = "empty";

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
if (start === "y") {
  while (request !== "quit") {
    request = prompt("Please select an action: add, remove, display, or quit.");
    if (request === "add") {
      addNew();
    } else if (request === "display") {
      display();
    } else if (request == "remove") {
      remove();
    }
  }
}
alert("Thanks for using the Web App! Please refresh the page to start over.");
