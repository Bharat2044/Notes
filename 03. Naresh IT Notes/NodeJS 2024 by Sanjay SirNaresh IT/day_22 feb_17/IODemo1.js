const fs = require('fs');

fs.readFile('day_22_notes.txt', () => {
    console.log('IO Code')
    setTimeout(() => {
        console.log('Timeout')
    }, 0);
    setImmediate(() => {
        console.log('Immediate')
    })
});

console.log('Program starts')
function f1() {
    console.log('I am f1...')
}
function f2() {
    console.log('I am f2...')
}
function f3() {
    console.log('I am f3...')
}
function f4() {
    console.log('I am f4...')
}
f1();
setTimeout(f2, 0);
Promise.resolve().then(f3);
f4();
console.log('Program ends')

