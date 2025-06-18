const fs = require('fs');

fs.readdir('./assets',(err,files) => {
    if (err) throw err;
    console.log(files)
})