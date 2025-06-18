let fs = require('fs');

let f1 = () => console.log('I am f1....')
let f2 = () => console.log('I am f2....')
let f3 = () => console.log('I am f3....')

console.log('Normal Code execution starts');
setTimeout(f1, 0)
Promise.resolve().then(f2)
process.nextTick(f3);

fs.readFile('./day_26_notes.txt', 'utf8', (err, data) => {
    console.log('I/O operation done')
})
console.log('Normal Code execution ends');