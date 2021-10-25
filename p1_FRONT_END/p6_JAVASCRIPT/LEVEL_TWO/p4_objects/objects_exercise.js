// PROBLEM 1
// Add a method that prints the length of the employees name to the console.
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function () {
    console.log(this.name.length);
  },
};

// PROBLEM 2
// Create an Alert in the browser of each of the object's values for the key value pairs.
// Name is John Smith, Job is Programmer, Age is 31.
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  employeeInfo: function () {
    alert(
      "Name is " + this.name + ", Job is " + this.job + ", Age is " + this.age
    );
  },
};

// PROBLEM 3
// Add a method called lastName that prints out the employee's last name to the console.
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  lastName: function () {
    let str = this.name;
    var array = str.split(" ");
    console.log(array[1]);
    // Course Solution: console.log(this.name.split(" ")[1]);
  },
};
