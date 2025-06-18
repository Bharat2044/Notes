"use strict";
let p = "hdfgh";
console.log(p, typeof p);
// TS provides static data typing
// number,boolean,string,undefined,null
// TS can understand datatype by two ways
//1. type inference , 2. type annotation
// Type inference means it will guess the datatype by value
// Type annotation means we specify datatypes explicitly
let a = 25;
console.log(typeof a);
let b = true;
let c = undefined;
let d = null;
// union - what if you want to give multiple datatypes to single variable
let e = "prasad";
// declare a variable which accepts string or boolean or number
let f = true;
// arrays
let g = [25, 78, -2, 0];
let h = [55, "raj", 91];
// what if i want each element different type -- tuple
let i = [25, "dghgsd", 78];
// any -- any will remove ts static typing
let j = 25;
