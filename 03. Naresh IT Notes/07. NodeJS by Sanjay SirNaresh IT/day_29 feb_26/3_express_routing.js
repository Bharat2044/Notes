const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.status(200).send('Server is Running...')
});

const userRouter = express.Router();
const productRouter = express.Router();

userRouter.get('/', (req, res) => {
    res.send('Users router working')
})
userRouter.get('/details', (req, res) => {
    res.status(200).send('User details router working')
})

productRouter.get('/', (req, res) => {
    res.status(200).send('productRouter working')
})
productRouter.get('/details', (req, res) => {
    res.status(200).send('product details  router working')
})

app.use('/users', userRouter)
app.use('/products', productRouter)

app.listen(5000, () => { console.log('Server Running on port 5000') });