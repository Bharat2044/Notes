let name = 'sachin'; // Global ,its part of script object, but its scope is global
var add = 'mumbai';  // Global 

function f1() {
    let a = 10;
    let b = 20;

    function f2() {
        let c = 30;
        console.log('I am f2');

        function f3() {
            console.log('I am f3',a);
        }
        f3();
        console.dir(f3)
    }
    f2();
    console.dir(f2)
}
f1();
console.dir(f1)