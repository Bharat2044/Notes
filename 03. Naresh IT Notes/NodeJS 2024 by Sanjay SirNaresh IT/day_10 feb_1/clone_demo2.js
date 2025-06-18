let arr1 = [10,20,[30,31]];

// let arr2 = [...arr1]; // value copy,  Shallow Copy
let arr2 = structuredClone(arr1)
arr2.push(40)
arr2[2].push(32)
console.log(arr1)
console.log(arr2)