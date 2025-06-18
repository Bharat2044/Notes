let user = {
    name: 'sachin',
    sayHi:  function() {
        console.log('Hiiii ' + this.name); // this = user
    }
}
user.sayHi();

setTimeout(user.sayHi, 2000)

setTimeout(()=>{
    user.sayHi.call(user)
}, 4000)
