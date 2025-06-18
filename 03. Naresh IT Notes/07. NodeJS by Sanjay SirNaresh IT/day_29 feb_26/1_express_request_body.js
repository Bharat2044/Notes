const express = require('express');
const app = express();

app.use(express.json());

app.post('/login', (req, res) => {
    const { email, password } = req.body;
    console.log(email, password)
    res.send('post request received on /login')

    // Req Object
    const { method, protocol, params, ip } = req;
    console.log(method, protocol, params, ip)
});

app.listen(5000, () => { console.log('Server Running on port 5000') });