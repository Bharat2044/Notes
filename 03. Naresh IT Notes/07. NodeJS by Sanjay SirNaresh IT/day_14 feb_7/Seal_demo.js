let obj = { a: 10, b: 20 };
obj.a = 15; // update value of A
obj.c = 30; // Add a new Property
delete obj.b; // Delete a property
console.log(obj);

let emp = { name: 'ajay', sal: 5000 }
Object.seal(emp);
emp.name = 'deepak'; // value change - yes
emp.add = 'bangalore'; // add a new property - No
delete emp.sal; // delete a property - No
console.log(emp)

console.log(Object.isSealed(obj))
console.log(Object.isSealed(emp))

