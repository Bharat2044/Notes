const fs = require('fs');

fs.readFile('./assets/file1.txt','utf-8',(err,data)=>{
    console.log(data)
})