const { setDbURL } = require('./db');

require('dotenv').config();

console.log(process.env.USER_ID)
console.log(process.env.PORT)
console.log(process.env.NODE_ENV);

setDbURL()