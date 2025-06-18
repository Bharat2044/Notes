function add(a, b) {
    // this = obj
    console.log(a + b + this.num); // NaN
}
add(2, 3);

let obj = { num: 4 };
add.call(obj , 2 , 3);

// inside add() this = obj