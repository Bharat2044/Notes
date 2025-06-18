var a = 10;

function demo1() { // impure
    console.log('I am demo1');
    a = 12;
}
demo1();


function add(a,b){
    console.log(a+b); // impure - no return value
}


function sub(a,b){ // impure - return value is not using input value
    console.log(a-b);
    return 'subtraction done';
}

function mul(a,b){ // Pure
    return a*b;
}