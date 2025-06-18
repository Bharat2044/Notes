function add(a, b) {
    console.log(a + b + this.num);
}
add(2, 3); // NaN

let obj = { num: 4 };
add.call(obj, 2, 3);

let arr = [2, 3];
add.call(obj, arr);

add.apply(obj , arr);
// 1. inside add(), this=obj 
// 2. a = arr[0] , b = arr[1]
