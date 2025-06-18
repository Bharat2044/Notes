const os = require('os');

console.log(os.uptime() / 60 / 60); // hours

console.log(os.cpus().length)
console.log(os.homedir())
console.log(os.tmpdir())
console.log(os.hostname())