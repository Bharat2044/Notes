let obj = {
    a: 10,
    b: 20,

    add: function () {
        console.log(this.a + this.b); // 30
        console.log(this)
        var that = this;

        function sub() {
            console.log(this.a - this.b); // this = global
            console.log(that.a - that.b); // this = global
            // console.log(this);
        }
        sub();

        let mul = () => { 
            console.log(this.a * this.b)
        }
        mul();
        // Arrow function doesn't care how it is called
        // where it is declared, inside add() , inside add() this=obj,  hence 
    }

}
obj.add(); // inside add() , this = obj