var a = 10;
let b = 20;
const c = 30;
console.log('global ', a, b, c); // 10 20 30

function test() {
    var a = 12;
    let b = 22;
    const c = 32;
    console.log('Function-1', a, b, c); // 12  22  32

    if (true) {
        var a = 15;
        let b = 25;
        const c = 35;
        console.log('BLock ', a, b, c);  // 15 25 35
    }
    console.log('Function-2', a, b, c); // 15 22 32
}
test()

