function fibonacci(n) {
    if (n === 1) {
        return [0, 1];
    } else {
        var s = fibonacci(n - 1);
        s.push(s[s.length - 1] + s[s.length - 2]);
        return s;
    }
}
function isPrime(num) {
    for (let i = 2; i < num; i++) if (num % i === 0) return false;
    return num !== 1 && num !== 0;
}
function isEven(n) {
    return n % 2 == 0;
}
function isOdd(n) {
    return Math.abs(n % 2) == 1;
}

function toLowerCase(str) {
    return str.toLowerCase();
}
function toUpperCase(str) {
    return str.toUpperCase();
}
function contains(str, substring, fromIndex) {
    return str.indexOf(substring, fromIndex) !== -1;
}
function repeat(str, n) {
    return new Array(n + 1).join(str);
}

module.exports = {
    fibonacci: fibonacci,
    isPrime: isPrime,
    isEven: isEven,
    isOdd: isOdd,
    toLowerCase: toLowerCase,
    toUpperCase: toUpperCase,
    contains: contains,
    repeat: repeat,
};