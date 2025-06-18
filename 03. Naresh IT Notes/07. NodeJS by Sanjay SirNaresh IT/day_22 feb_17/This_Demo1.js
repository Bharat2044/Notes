console.log(this, this === module.exports); //true
module.exports.name = "sanjay";
console.log(this); // { name:sanjay }
console.log(module.exports); // { name:sanjay }