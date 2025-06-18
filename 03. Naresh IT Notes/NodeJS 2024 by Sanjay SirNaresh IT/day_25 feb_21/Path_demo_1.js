const path = require('path');

console.log(`Separator ${path.sep}`)
console.log(`Delimeter ${path.delimiter}`)

const dirName = path.dirname('C:/Users/SANJAY/OneDrive/Desktop/NareshIT/Node_jan_18_2024/day_25 feb_21/Path_demo_1.js')
console.log(dirName)

const fileNameWithExt = path.basename('C:/Users/SANJAY/OneDrive/Desktop/NareshIT/Node_jan_18_2024/day_25 feb_21/Path_demo_1.js')
console.log(fileNameWithExt)

const fileNameWithoutExt = path.basename('C:/Users/SANJAY/OneDrive/Desktop/NareshIT/Node_jan_18_2024/day_25 feb_21/Path_demo_1.js','.js')
console.log(fileNameWithoutExt)

const extName = path.extname('C:/Users/SANJAY/OneDrive/Desktop/NareshIT/Node_jan_18_2024/day_25 feb_21/Path_demo_1.js','.js')
console.log(extName)

