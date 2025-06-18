function f1(){
    console.log('I am f1...');
    f2()
}
function f2(){
    console.log('I am f2...');
    f3()
}
function f3(){
    console.log('I am f3...');
    console.trace()
}
f1();
