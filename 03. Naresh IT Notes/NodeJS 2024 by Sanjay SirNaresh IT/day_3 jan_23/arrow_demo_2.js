let obj = {
    a: 10,
    b: 20,

    add: function () {
        console.log(this.a + this.b); // 30
        console.log(this)
    },
    mul: () => {
        console.log(this.a * this.b); // 200
        console.log(this)
    }
}
obj.add(); // inside add() , this = obj
obj.mul(); // mul() , this = {} 