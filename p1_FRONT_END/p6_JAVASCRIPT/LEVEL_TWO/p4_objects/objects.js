// Javascript objects are the same as what a dictionary would be in python

var carInfo = { make: "Toyota", year: 1990, model: "Camry" };

carInfo["make"];
carInfo["year"] = 2006;
carInfo["year"] += 1;

// Nested Object //
var myNewO = { a: "hello", b: [1, 2, 3], c: { inside: ["a", "b"] } };

myNewO["a"];
myNewO["b"][1];
myNewO["c"]["inside"][1];

// Iterating through object //
for (k in carInfo) {
  console.log(k);
  console.log(carInfo[k]);
}

////// Objects Continued //////
var myObj = {
  prop: 37,
  reportProp: function () {
    return this.prop;
  },
};
console.log(myObj.reportProp());

var simple = {
  prop: "Hello",
  myMethod: function () {
    console.log("The myMethod was called");
  },
};

var greetObj = {
  name: "Jose",
  greet: function () {
    console.log("Hello " + this.name);
  },
};
