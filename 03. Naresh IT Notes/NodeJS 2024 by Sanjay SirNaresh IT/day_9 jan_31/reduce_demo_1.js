let arr = [10, 20, 30, 40, 50];

let sum = 0;
for(ele of arr){
    sum = sum + ele;
}
console.log(sum)

let res = arr.reduce((sum,ele)=>{
    console.log(sum,ele)
    return sum + ele;
});
console.log(res)