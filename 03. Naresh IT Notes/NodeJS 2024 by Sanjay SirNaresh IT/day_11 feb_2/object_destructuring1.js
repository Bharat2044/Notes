let user = { name: 'sachin', age: 50, add: 'mumbai' };

let a = user.name;
let b = user.age;
let c = user.add;
console.log(a, b, c);

// ES-6
let { name, age, add } = user;
console.log(name, age, add)

let { name: p, age: q, add: r } = user;
console.log(p, q, r)

