let arr1 = [10, 20, 30, 40, 50];

/* let arr2 = [];
for (ele of arr1) {
    ele = ele + 5;
    arr2.push(ele)
}
console.log(arr2) */

let arr3 = arr1.map( ele=>{
    return ele == 20 ? ele+5 : ele;
});
console.log(arr3);