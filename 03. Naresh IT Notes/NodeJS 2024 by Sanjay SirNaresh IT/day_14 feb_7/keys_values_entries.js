let emp = { name: 'ajay', sal: 5000, add: 'bangalore' };

let allKeys = Object.keys(emp);
let allValues = Object.values(emp);
let allEntries = Object.entries(emp);

console.log(allKeys)
console.log(allValues)
console.log(allEntries)

let empObj = Object.fromEntries(allEntries);
console.log(empObj)


