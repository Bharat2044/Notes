const express = require('express')
const products = require('./products.json');
const productRouter = express.Router();

productRouter.get('/', (req, res) => {
    res.json(products)
})
productRouter.get('/:id', (req, res) => {
    let product = products.find(prod => prod.id === +req.params.id);
    res.json(product)
})

module.exports = productRouter;