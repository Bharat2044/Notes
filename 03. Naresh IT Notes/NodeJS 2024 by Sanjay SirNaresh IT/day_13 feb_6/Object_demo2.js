let user = {
    'add': 'bangalore',
    'age': 35,
    'first name': 'sachin',
    'last name': 'Tendulkar',
}
console.log(user.length);
let allKeys = Object.keys(user);
console.log(allKeys.length);

console.log('age' in user); // true
console.log(user.hasOwnProperty('add'))