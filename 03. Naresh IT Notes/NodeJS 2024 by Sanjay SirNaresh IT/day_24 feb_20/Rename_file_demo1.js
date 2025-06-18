const fs = require('fs');

fs.rename('./assets/file4.txt', './assets/file1.txt', (err) => {
    if (err) throw err;
    console.log('file renamed successfully')
})