var countries = ["USA", "Germany", "China"];

countries[1] = "France";

var arr = ["A", "B", "C"];

for (letter of arr) {
  alert(letter);
}

arr.forEach(alert);

var topics = ["pyton", "django", "science"];

function addAwesome(name) {
  console.log(name + " is awesome!");
}

topics.forEach(addAwesome);
