let user = {
    'add': 'bangalore',
    'age': 35,
    'first name': 'sachin',
    'last name': 'Tendulkar',
}
// console.log(user.first name)
console.log(user['first name']);

let a = 'add';
console.log(user.a); // undefined
console.log(user[a]); // bangalore

for (let key in user) {
    console.log(key + " ==== " + user[key])
}