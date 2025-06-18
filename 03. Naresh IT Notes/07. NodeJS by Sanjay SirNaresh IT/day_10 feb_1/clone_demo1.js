let arr1 = [10, 20];
let arr2 = arr1;  // Reference copy
arr2.push(30);
console.log(arr1, arr2);

let arr3 = [10, 20];
let arr4 = [...arr3]; // Spread Operator , value copy
arr4.push(30)
console.log(arr3, arr4)

