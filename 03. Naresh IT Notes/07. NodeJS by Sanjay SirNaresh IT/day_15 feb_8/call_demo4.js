// call() used for inheritance
function Person(name, age) {
    this.name = name;
    this.age = age;
}
function Employee(name, age, eid, sal) {
    Person.call(this, name, age);
    this.eid = eid;
    this.sal = sal;
}
let emp1 = new Employee('sachin', 35, 101, 5000);
console.log(emp1)

