module.exports = {
    'env': {
        'browser': true,
        'commonjs': true,
        'es2021': true
    },
    'extends': 'eslint:recommended',
    'parserOptions': {
        'ecmaVersion': 'latest'
    },
    'rules': {
        'semi': ['error', 'always'],
        'quotes': ['error', 'single'],
        'no-var': 2,
        'eqeqeq': 2
    }
};
