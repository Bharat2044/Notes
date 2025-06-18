const { fibonacci, isPrime, isEven } = require("../util");

describe('This is a test suite for util file', () => {
    beforeAll(() => { // 1
        console.log('before all'); // 1 time initialization, Setup
    })
    beforeEach(()=>{  // N of times
        console.log('before Each')
    })
    afterEach(()=>{  // N of times
        console.log('after Each')
    })
    afterAll(() => { // 1 , Teardown
        console.log('after all');  // 1 time clean up after all the testcases are executed
    })

    it('This is testcase for fibonacci function', () => {
        console.log('It---1')
        expect(fibonacci(3)).toEqual([0, 1, 1])
    })
    it('This is testcase for isPrime function', () => {
        console.log('It---2')
        expect(isPrime(2)).toBe(true);
        expect(isPrime(6)).not.toBe(true);
    })
    it('This is testcase for isEven function', () => {
        console.log('It---3')
        expect(isEven(2)).toBe(true);
        expect(isEven(3)).not.toBe(true);
    })
});