/////////
// IF //
///////
// Here is the syntax for an if statement in JavaScript:
// if (condition){
//     // Execute some code
// }

var hot = false
var temp = 60

if (temp > 80) {
    hot = true

}
console.log(hot)

// Set temp higher
var temp = 100

if (temp > 80) {
    hot = true

}

console.log(hot)

///////////
// ELSE //
/////////
// if (condition) {
//   // Code to execute if true
// } else {
//   // Code to execute if above was not true
// }

temp = 30

if (temp > 90) {
    console.log("Hot outside!")
} else {
    console.log("Its not too hot today!")
}


///////////////
// ELSE IF ///
/////////////

// What if we wanted more options to print out, rather than just two, the if
// and the else? This is where we can use the else if statement to add multiple
// condition checks, using else at the end to execute code if none of our
// conditions match up with and if or else if.
// Let's see this in action!

temp = 75
// temp = 30

if (temp > 80) {
    console.log("Hot outside!")
} else if (temp <= 80 && temp >= 50) {
    console.log('Nice outside!')
} else if (temp <= 50 && temp >= 32) {
    console.log("Its cooler outside!")
} else {
    console.log("Its really cold outside!")
}

//////////////////////////////////////////////
// Final Example with Comparison Operators //
////////////////////////////////////////////


// Items sold that day
var ham = 10
var cheese = 10

// Report to HQ
var report = 'blank'

if (ham >= 10 && cheese >= 10) {
    report = "Strong sales of both items"

} else if (ham === 0 && cheese === 0) {
    report = "Nothing sold!"
} else {
    report = 'We had some sales'
}
console.log(report)
