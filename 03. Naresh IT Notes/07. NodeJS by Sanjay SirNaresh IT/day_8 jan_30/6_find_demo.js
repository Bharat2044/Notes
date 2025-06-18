let employees = [
    { eId: 101, name: 'sanjay', sal: 5000, gender: 'male' },
    { eId: 104, name: 'geeta', sal: 8000, gender: 'female' },
    { eId: 103, name: 'sameer', sal: 7000, gender: 'male' },
    { eId: 102, name: 'sita', sal: 9000, gender: 'female' },
    { eId: 105, name: 'deepak', sal: 8000, gender: 'male' },
];
// Find the employee whose sal is 8000
let res1 = employees.find((ele) => ele.sal == 8000);
console.log(res1);

// find the last employee whose sal is 8000
let res2 = employees.findLast((ele) => ele.sal == 8000);
console.log(res2);

// find all the employees whose sal is 8000
let res3 = employees.filter((ele) => ele.sal == 8000);
console.log(res3);


let students = ['Siva', 'Yogesh', 'Rohit', 'Deepak', 'Praveen', 'Siva'];
console.log(students.indexOf('Rohit')); // number,string array

console.log(employees.indexOf('Sameer'))
console.log(employees.indexOf({ eId: 103, name: 'sameer', sal: 7000, gender: 'male' }))

console.log(employees.findIndex(emp=>emp.name === 'sameer'))
