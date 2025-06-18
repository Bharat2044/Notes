const express = require('express')
const users = require('./users.json');
const userRouter = express.Router();

userRouter.get('/', (req, res) => {
    res.json(users)
})
userRouter.get('/:id', (req, res) => {
    let user = users.find(usr => usr.id === +req.params.id);
    res.json(user)
})

module.exports = userRouter;