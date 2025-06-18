const express = require('express');
const axios = require('axios')
const app = express();

app.get('/users/:userName', async (req, res) => {
    const { userName } = req.params;
    const response = await axios.get(`https://api.github.com/users/${userName}`);
    res.status(200).send(response.data)
})
app.get('*', (req, res) => {
    res.status(200).send('Sorry, Page not found')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });