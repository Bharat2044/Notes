const path = require('path');

console.log(path.join())
console.log(path.resolve())

let res1 = path.join('hello','/path','me')
console.log(res1)
let res2 = path.resolve('hello','path','me')
console.log(res2)