// Rest Parameter ...
function add(...arr) {
    let sum = 0;
    for (ele of arr) {
        sum = sum + ele;
    }
    console.log(sum)
}

add(1, 2, 3)
add(1, 2, 3, 4)
add(1, 2, 3, 4, 5)

// let arr2 = [...arr1]  Spread Operator