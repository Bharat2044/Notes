const express = require('express');
const axios = require('axios')
const app = express();

app.get('/temp', async (req, res) => {
    const  city  = req.query.city || 'bangalore';
    const myURL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&mode=json&units=metric&appid=fbf712a5a83d7305c3cda4ca8fe7ef29`
    const resp = await fetch(myURL);
    const response = await resp.json();
    console.log(response.data)
    res.send(`<h1>
        City Name is ${city} , Temperature is ${response.main.temp}
    </h1>`)
})
app.get('*', (req, res) => {
    res.status(200).send('Sorry, Page not found')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });