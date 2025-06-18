let students = ['Siva', 'Yogesh', 'Rohit', 'Deepak', 'Praveen', 'Siva'];
students.sort();
console.log(students);

let arr1 = [10, 50, 20, 40, 30];
arr1.sort();
console.log(arr1);

let arr2 = [10, 92, 8, 9, 7, 101, 105, 91,8];
arr2.sort();  // Numeric sort - NO , String Sort
console.log(arr2);

arr2.sort((a,b)=>b-a)
console.log(arr2);
