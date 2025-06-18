function varTest() {
    if (true) {
        var a = 10; // this variable is not block scoped, it is function scoped
        console.log('block', a); // 10
    }
    console.log('function ', a); // 10
}
varTest()

function letTest() {
    if (true) {
        let a = 10; 
        console.log('block', a); // 10
    }
    console.log('function ', a); // 10
}
letTest()