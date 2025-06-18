// Normal Function
function add(a, b, c) {
    console.log(a + b + c);
}
add(2, 3, 4);

// Function Curring
let sum = function (a) {
    return function (b) {
        return function (c) {
            console.log(a + b + c);
        }
    }
}
sum(2)(3)(4)

