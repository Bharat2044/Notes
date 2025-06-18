class Student {
    constructor(roll, name) {
        this.roll = roll;
        this.name = name;
    }
}
Student.prototype.clgName = 'nareshIT';

let std1 = new Student(101, 'Jyoti', 'NodeJS');

console.log('roll' in std1);
console.log(std1.hasOwnProperty('name'));

console.log('clgName' in std1);  // true
console.log(std1.hasOwnProperty('clgName')); // false

console.log('course' in std1); // false
console.log(std1.hasOwnProperty('course')); //false