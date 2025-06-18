console.log(this) ; // module.exports = {}

function f1() {
    console.log(this); // this = global
}
f1();
function f2() {
    'use strict'
    console.log(this); // this = undefined
}
f2();

