const express = require('express');
const app = express();

app.use("/book", (req, res) => {
    res.send('use method')
});
app.all("/book", (req, res) => {
    res.send('all method')
});

app.listen(5000, () => { console.log('Server Running on port 5000') });