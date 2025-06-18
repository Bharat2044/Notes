let students = ['Siva', 'Yogesh', 'Rohit', 'Deepak'];

students.push('praveen');
console.log(students);

students.pop();
console.log(students);

students.unshift('praveen');
console.log(students);

students.shift()
console.log(students);

// array.splice( index , how many elements to delete , elements to add)
students.splice(2, 2, 'praveen');
console.log(students);

students.splice(3, 0, 'Rohit', 'Deepak');
console.log(students);

console.log(students.slice(1, 4));

let arr1 = [10, 20, 30];
let arr2 = [40, 50, 60];
console.log(arr1.concat(arr2));

