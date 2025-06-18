const express = require('express')
const cookieParser = require('cookie-parser')
const app = express();
app.use(cookieParser());

app.get('/', (req, res) => {
    console.log(req.headers);
    res.send(req.headers);
})
app.get('/setCookie', (req, res) => {
    console.log('setCookie')
    res.cookie('name', 'sanjay');
    res.cookie('age', 50);
    res.send('cookie is returned and saved')
});
app.get('/getCookie', (req, res) => {
    // get client cookies
    const cookieData = req.cookies;
    console.log(req.cookies)
    res.send(cookieData)
});
app.get('/deleteCookie', (req, res) => {
    // clear cookie
    res.clearCookie('age');
    res.send('Cookie data cleared')
});

app.listen(5001, () => { console.log('server started at 5001') })