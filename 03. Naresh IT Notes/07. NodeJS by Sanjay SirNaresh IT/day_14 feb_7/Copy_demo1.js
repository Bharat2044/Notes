let obj1 = { a: 10, b: 20 };
let obj2 = obj1;  // Address Copy / Reference
obj1.a = 15;
obj2.b = 25;
console.log(obj1)
console.log(obj2)

let obj3 = { a: 10, b: 20 };
let obj4 = Object.assign({}, obj3); // Value Copy - Shallow copy
obj3.a = 15;
obj4.b = 25;
console.log(obj3)
console.log(obj4)