const express = require('express');
const app = express();

app.get('/users', (req, res) => {
    res.send('GET on /Users route')
    
})
app.use('/employees', (req, res) => {
    res.send('all types of methods  on /Users route')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });