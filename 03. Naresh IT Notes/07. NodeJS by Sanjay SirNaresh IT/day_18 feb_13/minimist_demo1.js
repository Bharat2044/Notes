const minimist = require('minimist');

const argsArr = process.argv.slice(2);
const argsObj = minimist(argsArr);

console.log(argsArr, argsObj.name , argsObj.add)
