const fs = require('fs');

fs.readFile('day_22_notes.txt', () => {
    setTimeout(() => {
        console.log('Timeout')
    }, 0);
    setImmediate(() => {
        console.log('Immediate')
    })
});