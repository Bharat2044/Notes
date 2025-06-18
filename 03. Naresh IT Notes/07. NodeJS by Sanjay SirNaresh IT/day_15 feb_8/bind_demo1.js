function add(a, b) {
    console.log(a + b + this.num);
}
add(2, 3); // NaN

let obj = { num: 4 };

let sum = add.bind(obj);
sum(2,3)
sum(4,5)
sum(10,20)

setTimeout( add , 2000 , 2,3)
setTimeout( sum , 4000 , 2,3)
