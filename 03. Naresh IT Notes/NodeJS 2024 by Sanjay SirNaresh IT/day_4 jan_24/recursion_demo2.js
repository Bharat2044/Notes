var data = {
    a: {
      a1: 'hello',
      a2: true,
      a3: false,
      a4: {},
      a5: [],
      a6: ['red', 'blue', true],
      a7: null,
      a8: undefined,
      a9: NaN,
      a10: function() {},
      a11: Math,
      a12: JSON,
      a13: /a-z/,
      a14: new ReferenceError,
      a15: new Date,
      a16: new Number(7),
      a17: new String("abc"),
      a18: new Boolean(true)
    },
    b: {
      b1: {
        b1a: true,
        b1b: 100
      },
      b2: {
        b2a: true,
        b2b: false,
        b2c: 10.10
      }
    }
  }


  true = myKeyPresent(b2b)
  false = myKeyPresent(b2d)