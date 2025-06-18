class Employee {
    name = 'sanjay';
    sal = 5000;

    displayInfo1() {
        console.log('display Info - 1');
        console.log(this.name, this.sal)
    }
    displayInfo2 = () => {
        console.log('display Info - 2');
        console.log(this.name, this.sal)
    }
}
let emp = new Employee();
emp.displayInfo1();
emp.displayInfo2();

let a = emp.displayInfo1;
// a();

let b = emp.displayInfo2;
b();

let c = b;
c();

let d = c;
d();
