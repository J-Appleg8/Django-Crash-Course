// function name(parameter1, parameter2) {
// Code to be executed
//}

function helloYou(name) {
  console.log("Hello " + name);
}

function addNum(num1, num2) {
  console.log(num1 + num2);
}

//Default values in a function
function helloSomeone(name = "James") {
  console.log("Hello " + name);
}

//If you want to return the return values of a function - use the return keyword
function formal(name = "Sam", title = "Sir") {
  return title + " " + name;
}

function timesFive(numInput) {
  var result = numInput * 5;
  return result;
}

//Scope - describes how objects and variables get defined within Javascript
var v = "Global V";
var stuff = "Global Stuff";

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func";
  console.log(stuff);
}

fun();
console.log(stuff);
