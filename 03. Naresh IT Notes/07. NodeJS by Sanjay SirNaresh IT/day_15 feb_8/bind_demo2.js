class Employee {
    fname = 'Sachin';
    lName = ' Tendulkar';

    fullName() {
        console.log(this.fname + this.lName)
    }
}
let emp1 = new Employee();
emp1.fullName();

let myFullName = emp1.fullName.bind(emp1);

setTimeout( emp1.fullName , 2000 )
setTimeout(  myFullName , 4000 )

function Test(myCallBack){
    myCallBack();
}
// Test(emp1.fullName);
Test(myFullName)