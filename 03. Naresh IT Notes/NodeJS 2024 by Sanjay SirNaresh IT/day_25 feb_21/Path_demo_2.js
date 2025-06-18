const path = require('path');

const isabsolute1 = path.isAbsolute('c:/program file')
console.log(isabsolute1)

const isabsolute2 = path.isAbsolute('home/')
console.log(isabsolute2)


let pathStr = path.format({dir:'d:/nodejs/html/js',base:'app.js'})
console.log(pathStr)

let pathstr2 = path.join('/home/','/abc','pqr')
console.log(pathstr2)