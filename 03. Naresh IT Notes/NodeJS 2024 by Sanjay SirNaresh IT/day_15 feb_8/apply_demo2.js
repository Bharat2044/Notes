function add(a, b, c) {
    console.log(a + b + c);
}
add(10, 20, 30);

let arr = [10, 20, 30];
add(arr)

add.apply({},arr);
