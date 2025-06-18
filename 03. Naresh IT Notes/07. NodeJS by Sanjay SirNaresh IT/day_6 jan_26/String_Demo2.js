let str1 = '2+2';
let str2 = new String('2+3');

console.log(eval(str1)); // Eval() works with string literal
console.log(eval(str2)); // Eval() doesn't work with string object

let str3 = str2.valueOf(); // valueOf() converts string object to string literal
console.log(eval(str3)); 


