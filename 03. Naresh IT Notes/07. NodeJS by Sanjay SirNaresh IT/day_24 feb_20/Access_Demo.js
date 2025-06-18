const fs = require('fs');

fs.access('./assets/users.json', fs.W_OK, (err, data) => {
    if (err) throw err;
    console.log('Yes You have write access')
})
fs.access('./assets/users.json', fs.R_OK, (err, data) => {
    if (err) throw err;
    console.log('Yes You have Read access')
})