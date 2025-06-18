const express = require('express');
const axios = require('axios')
const app = express();

app.get('/user', async (req, res) => {
    const { name, add } = req.query;
    res.json({ name, add })
})
app.get('*', (req, res) => {
    res.status(200).send('Sorry, Page not found')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });