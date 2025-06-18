let res1 = Math.max(10, 20, 40, 30);
console.log(res1); // 40 

let arr = [10, 20, 40, 30, 50]
// let res2 = Math.max(arr);  NaN
let res2 = Math.max.apply(null, arr);
console.log(res2);


let res3 = Math.max(...arr);
console.log(res3)
