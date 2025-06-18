const express = require('express');
const app = express();

let users = ['Yogesh', 'Manoj', 'Sanjay', 'Shruti', 'Jyoti'];

app.set('views', './views');
app.set('view engine', 'pug');

app.get('/', (req, res) => {
    res.render('index')
});
app.get('/users', (req, res) => {
    res.render('users', { users })
});

app.listen(5000, () => { console.log('Server running on port 5000') });