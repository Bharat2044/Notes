const cp = require('child_process');

cp.exec('start chrome https://www.youtube.com/')
for(let i=1;i<=100000000;i++){
    console.log('Main Process '+i)
}

