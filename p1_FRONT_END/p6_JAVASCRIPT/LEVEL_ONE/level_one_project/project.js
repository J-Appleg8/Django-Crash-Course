var firstName = prompt("Please Enter Your First Name");
var lastName = prompt("Please Enter Your Last Name");
var agentAge = prompt("What is your age?");
var agentHeight = prompt("How tall are you?");
var petName = prompt("What is your pet's name?");

var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond = null;

if (firstName[0] === lastName[0]) {
  nameCond = true;
} else {
  nameCond = false;
}

if (agentAge > 20 && agentAge < 30) {
  ageCond = true;
} else {
  ageCond = false;
}

if (agentHeight >= 170) {
  heightCond = true;
} else {
  heightCond = false;
}

if (petName[petName.length - 1] === "y") {
  petCond = true;
} else {
  petCond = true;
}

if (nameCond & ageCond & heightCond & petCond) {
  console.log(
    "This message will self-destruct in 10 seconds. Please see file if you choose to accept"
  );
}
