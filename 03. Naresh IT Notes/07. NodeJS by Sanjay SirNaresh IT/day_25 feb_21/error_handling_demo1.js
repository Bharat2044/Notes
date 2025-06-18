const fs = require('fs');

fs.unlink('./assets/file3.txt',(err) => {
    // if (err) throw err;
    console.log('file deleted successfully')
})