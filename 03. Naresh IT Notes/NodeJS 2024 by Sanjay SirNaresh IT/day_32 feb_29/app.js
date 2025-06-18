const express = require('express');
const cors = require('cors');

const userRouter = require('./user')
const productRouter = require('./product');

const app = express();

var corsOptions = {
    origin: 'https://www.w3schools.com',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
}
app.use(cors(corsOptions));

app.use('/users', userRouter);
app.use('/products', productRouter);

app.listen(5000, console.log, 'server running at port 5000')