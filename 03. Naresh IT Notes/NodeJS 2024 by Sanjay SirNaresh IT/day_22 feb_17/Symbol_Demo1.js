let id = Symbol('this is my id');
let user = {
    'name': 'sanjay',
    'age': 50,
    'cars': ['tata', 'honda'],
    [id]: 101
}
console.log(user);
console.log(user['name'])
console.log(user[id])

for(key in user){
    console.log(key+"      "+user[key])
}
console.log(Object.keys(user))
console.log(Object.getOwnPropertySymbols(user))