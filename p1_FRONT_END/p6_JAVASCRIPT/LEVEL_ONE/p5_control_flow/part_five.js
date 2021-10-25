var hot = false;
var temp = 40;

if (temp > 80) {
  console.log("Hot Outside!");
} else {
  console.log("Its not very hot today");
}

if (temp > 80) {
  console.log("Hot Outside!");
} else if (temp <= 80 && temp >= 50) {
  console.log("Average Temp Outside");
} else if (temp < 50 && temp >= 32) {
  console.log("Pretty cold today");
} else {
  console.log("It is very cold out");
}

var ham = 0;
var cheese = 10;
var report = "blank";

if (ham >= 10 && cheese >= 10) {
  report = "Strong sales of both ham and cheese";
} else if (ham === 0 && cheese === 0) {
  report = "Nothing sold";
} else {
  report = "We had some sales";
}

console.log(report);
