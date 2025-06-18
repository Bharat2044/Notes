const fs = require('fs');

fs.appendFile('./assets/file2.txt', 'This is File-2 Content \n', () => {
    console.log('Write Operation is done')
});