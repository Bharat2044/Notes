let cardNumber = '1111222233334444';

let result1 = cardNumber.match(/.{1,4}/g).join('-');
console.log(result1);

let arr = [];
for (let i = 0; i < cardNumber.length; i = i + 4) {
    arr.push( cardNumber.substr(i,4) );
}
let result2 = arr.join('-')
console.log(result2)