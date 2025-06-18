let counter = 0;
function fibonacci(n) {
    console.log('called',++counter)
    if (n <= 1) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
};
let res = fibonacci(8);
console.log(res);
// 0 1 1 2 3 5 8 13 21 34