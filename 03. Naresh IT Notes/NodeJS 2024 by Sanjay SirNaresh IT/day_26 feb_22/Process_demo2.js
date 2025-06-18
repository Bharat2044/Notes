console.log('Normal Code execution starts');

let f1 = () => console.log('I am f1....')
let f2 = () => console.log('I am f2....')
let f3 = () => console.log('I am f3....')
let f4 = () => console.log('I am f4....')
let f5 = () => console.log('I am f5....')

setTimeout(f1, 0)
Promise.resolve().then(f2)
process.nextTick(f3);
process.nextTick(() => {
    console.log('Normal code in nextTick')
    setTimeout(f4, 0)
    process.nextTick(f5, 0)
});

console.log('Normal Code execution ends');