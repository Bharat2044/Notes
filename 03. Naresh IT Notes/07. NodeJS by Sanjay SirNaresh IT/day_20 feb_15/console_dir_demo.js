function f1() {
    let a = 10;

    function f2() {
        console.log(a);
    }
    f2();

    console.log(f2)
    console.dir(f2)
}
f1();