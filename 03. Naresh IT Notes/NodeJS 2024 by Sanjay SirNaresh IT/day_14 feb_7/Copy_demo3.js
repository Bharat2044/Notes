let emp1 = {
    name: 'deepak',
    sal: 5000,
    displayInfo: function () {
        console.log(this.name, this.sal)
    }
}
// let emp2 = structuredClone(emp1);
let emp2 = JSON.parse(JSON.stringify(emp1))

console.log(emp1)
console.log(emp2)