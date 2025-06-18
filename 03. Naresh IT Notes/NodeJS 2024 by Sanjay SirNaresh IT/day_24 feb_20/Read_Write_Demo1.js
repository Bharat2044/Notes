const { readFileSync, writeFileSync } = require('fs');

try {
    let data1 = readFileSync('./assets/file1.txt', 'utf8');
    let data2 = readFileSync('./assets/file2.txt', 'utf8');
    writeFileSync('./assets/file3.txt', `${data1} ${data2}`);
}
catch (err) {
    console.log('something is wrong')
}