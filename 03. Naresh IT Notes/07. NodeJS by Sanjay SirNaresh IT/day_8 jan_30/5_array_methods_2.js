let students = ['Siva', 'Yogesh', 'Rohit', 'Deepak', 'Praveen', 'Siva'];

console.log(students[3])
console.log(students[-2])

console.log(students.at(3))
console.log(students.at(-2)) // takes -ve index

console.log(students.indexOf('Siva')); // 0
console.log(students.lastIndexOf('Siva')); // 5
console.log(students.indexOf('Manoj')); // -1

console.log(students.includes('Manoj')); // false
console.log(students.includes('Siva')); // true