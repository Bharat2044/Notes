let obj1 = { a: 10, b: 20, c: { d: 30 } };
// let obj2 = { ...obj1 }; // Shallow Copy
let obj2 = structuredClone(obj1); // Deepcopy
obj1.a = 15;
obj1.b = 25;
obj1.c.d = 35;
console.log('obj1', obj1)
console.log('obj2', obj2)
