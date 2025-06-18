let counter = 0;
function fibonacci(n, cache={}) {
    console.log('called',++counter, cache);
    if(cache[n]){
        return cache[n];
    }
    if (n <= 1) {
        return 1;
    }
    return (cache[n] = fibonacci(n - 1,cache) + fibonacci(n - 2,cache));
};
let res = fibonacci(8);
console.log(res);
// 0 1 1 2 3 5 8 13 21 34