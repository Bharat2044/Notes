// function declaration
function add(a, b) {
    console.log(a + b);
}
add(2, 3);
add(3, 4);


// Function Expression
let sub = function (a, b) {
    console.log(a - b)
}
sub(10, 4)


// Self Invoked
(function (a, b) {
    console.log(a * b)
})(3, 5);   