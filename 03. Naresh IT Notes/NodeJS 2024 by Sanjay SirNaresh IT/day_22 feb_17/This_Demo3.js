let obj = {
    a: 10,
    b: 20,
    add: function () {
        console.log(this.a + this.b); // this = obj
    },
    mul: () => {
        console.log(this.a * this.b); // this = 
        console.log(this)
    }
}
obj.add();
obj.mul()


