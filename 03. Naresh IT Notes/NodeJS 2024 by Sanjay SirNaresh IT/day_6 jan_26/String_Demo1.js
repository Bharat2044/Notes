let a = 'hello'; // String Literal
let b = new String('hello'); // String Object
let c = new String('hello'); // String Object
console.log(typeof a, typeof b); // string , object

console.log(a == b); // value comparison
console.log(c == b); // reference comparison