function test(a, b, ...c) {
    console.log(a, b, c)
}
test(2, 3) // 2   3   []   
test(2, 3, 4, 5)  // 2   3  [4,5]   
