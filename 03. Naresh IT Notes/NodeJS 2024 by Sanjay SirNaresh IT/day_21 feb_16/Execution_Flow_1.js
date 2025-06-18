console.log('Helloooo')

let a = 10;
let b = 20;

function f1() {
    console.log('F1 startes here...')
    f2();
    console.log('F1 ends here...')
}
function f2() {
    console.log('F2 startes here...')
    f3();
    console.log('F2 ends here...')
}
function f3() {
    console.log('F3 startes here...')
    console.log('F3 ends here...')
}
f1();
console.log('Hiiiiiiiiiii')