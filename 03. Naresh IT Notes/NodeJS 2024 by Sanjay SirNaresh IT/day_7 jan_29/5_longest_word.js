let str = 'this is javascript class';

let words = str.split(' ');
let longestWord = '';

for (word of words) {
    if (word.length > longestWord.length) {
        longestWord = word;
    }
}
console.log(longestWord)