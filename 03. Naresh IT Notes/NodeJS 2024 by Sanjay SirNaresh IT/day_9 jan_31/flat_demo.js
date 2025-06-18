let arr = [10, 20, [30, 40, [50, 60, [70, 80]]]];

console.log(arr, arr.length);

let arr1 = arr.flat(); // depth = 1
console.log(arr1, arr1.length);

let arr2 = arr.flat(2); // depth = 2
console.log(arr2, arr2.length);

let arr3 = arr.flat(Infinity);  // depth = n
console.log(arr3, arr3.length);

