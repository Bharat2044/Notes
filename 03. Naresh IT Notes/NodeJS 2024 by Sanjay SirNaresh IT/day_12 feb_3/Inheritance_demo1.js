class Person {
    constructor(name, add) {
        this.name = name;
        this.add = add;
    }
}
class Employee extends Person{
    constructor(name,add,eid,sal){
        super(name,add); // invoke parent's constructor
        this.eid = eid;
        this.sal = sal;
    }
}
class Student extends Person{
    constructor(name,add,roll,course){
        super(name,add); // invoke parent's constructor
        this.roll = roll;
        this.course = course;
    }
}
let std1 = new Student('sanjay','bangalore',101,'NodeJS');

let emp1 = new Employee('deepak','e105','Hyderabad',35000);

console.log(std1)
console.log(emp1)

