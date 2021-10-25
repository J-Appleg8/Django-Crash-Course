/// PART 8 - LOOP EXERCISES

///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
var hello = "Hello";

// While Loop
var x = 0;
while (x < 5) {
  console.log(hello);
  x++;
}

// For Loop
for (let i = 0; i < 5; i++) {
  console.log(hello);
}

/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25

// While Loop
myNum = 0;

while (myNum < 25) {
  if (myNum % 2 !== 0) {
    console.log(myNum);
  }
  myNum++;
}

// For Loop
for (let i = 0; i < 25; i++) {
  if (i % 2 !== 0) {
    console.log(i);
  }
}
