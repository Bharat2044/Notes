let str = 'this is javascript class';

let words = str.split(' ');
let result = '';

for(word of words){
    let changedWord = word[0].toUpperCase() + word.substring(1);
    result = result + changedWord+' ';
}
console.log(result)