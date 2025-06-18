let students = ['Siva', 'Yogesh', 'Rohit', 'Deepak'];

// 1. Loop
for (let i = 0; i < students.length; i++) {
    console.log(students[i])
}

// 2. for-in loop
for (i in students) {
    console.log(i, students[i])
}

// 3. for-of loop
for (ele of students) {
    console.log(ele)
}

// 4. forEach(callback)
/* function printMe(val, ind, arr) {
    console.log(val, ind, arr)
}
students.forEach(printMe) */

students.forEach((val,ind)=>console.log(val , ind))
