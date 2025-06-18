const fs = require('fs');

fs.readFile('./assets/users.json', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data)
})