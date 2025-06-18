let obj1 = { a: 10 }
let obj2 = { b: 20 }
let obj3 = { c: 30 }

Object.assign(obj1, obj2, obj3);

console.log(obj1, obj2, obj3); // copies by value - shallow copy