let user = {
    name: 'sachin',
    age: 50,
    add: 'mumbai',
    displayInfo() {
        console.log(this.name, this.add)
    }
}
user.displayInfo()

let userObj = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "pwd": 'adsfjkjhj',
    "add": 'bangalore'
}


function demo({name,add}) {
    // return { name: user.name, add: user.add };
    return { name,add};
}
let res = demo(userObj)
console.log(res)
