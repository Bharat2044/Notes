class Employee {
    name = 'sachin';
    greet1 = function () {
        console.log('Hello ' + this.name);
        // console.log(this) this = from where it is invoked
    }
    greet2 = () => {
        console.log('Hi ' + this.name); // this = where this function is written
    }
}
let emp = new Employee();
emp.greet1(); // greet1() , this = employee
emp.greet2(); // greet2() , this = employee

setTimeout(emp.greet1, 3000);
setTimeout(emp.greet2, 6000);

