let obj1 = {
    a: 10,
    b: 20,
    add: function () {
        console.log(this.a + this.b)
    }
}
obj1.add(); // inside add() , this = obj1 (default)


let obj2 = { a: 15, b: 25 };
obj1.add.call(obj2); // inside add() , this = obj2


let obj3 = { a: 100, b: 200 }
obj1.add.call(obj3); // inside add() , this = obj3