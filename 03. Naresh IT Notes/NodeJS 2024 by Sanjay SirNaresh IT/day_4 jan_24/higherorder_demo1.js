function f1(){
    function f2(){
        console.log('I am f2')
    }
    return f2;
}
// f1 - HigherOrder , it return f2

let arr = [10,20,30];

function myFunc(ele){
    console.log(ele)
}
arr.forEach(myFunc);
// forEach() is higherorder , it takes myFunc() as argument
// myFunc - callback function