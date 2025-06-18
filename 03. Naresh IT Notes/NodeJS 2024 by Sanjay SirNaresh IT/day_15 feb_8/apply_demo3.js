let res1 = Math.max(10, 20, 30, 40, 50);
console.log('res1 ', res1)

let arr = [10, 20, 30, 40, 50]

let res2 = Math.max(arr);
console.log('res2 ', res2)

let res3 = Math.max.apply({},arr)
console.log('res3 ', res3)

let res4 = Math.max(...arr)
console.log('res4 ', res4)