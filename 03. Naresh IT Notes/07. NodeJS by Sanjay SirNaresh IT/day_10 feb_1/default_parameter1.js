function add(a, b, c) {
    console.log(a + b + c); // NaN
}
add(2, 3)

function sum(a, b, c) {
    a = a | 0;
    b = b | 0; // ES-5
    c = c | 0;
    console.log(a + b + c);
}
sum(2, 3)


function addition(a = 0, b, c = 0) { // ES-6 Default parameter value
    console.log(a + b + c);
}
addition(2, 3)
