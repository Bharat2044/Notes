console.log('LIne-1')

function f2() {
    console.log('f2 started...')
    console.log('f2 completed...')
}
function f1() {
    console.log('f1 started...')
    f2()
    console.log('f1 completed...')
}
f1();

console.log("line-14")