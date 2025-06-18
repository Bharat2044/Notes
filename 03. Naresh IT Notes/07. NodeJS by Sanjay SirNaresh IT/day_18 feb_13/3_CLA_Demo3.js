let argsArr = process.argv.slice(2);
console.log(argsArr);

let argsObj = {};
for (ele of argsArr) {
    let keyValueArr = ele.split('=');
    let [key, val] = keyValueArr;
    argsObj[key] = val;
}
console.log(argsObj)