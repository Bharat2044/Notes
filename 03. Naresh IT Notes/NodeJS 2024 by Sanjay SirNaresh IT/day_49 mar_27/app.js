const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json())
const PORT = 5000;

const mongoose = require('mongoose');
const userModel = require('./user-model');

mongoose.connect('mongodb://0.0.0.0:27017/march2023');

app.get('/api/auth/users', async (req, res) => {
    let users = await userModel.find({});
    res.status(200).json(users)
});
app.post('/api/auth/register', async (req, res) => {
                req.body.password = bcrypt.hashSync(req.body.password, 8);
    try {
        const newuser = new userModel(req.body);
        await newuser.save();
        res.status(201).send('User Created Succesfully!!')
    } catch (err) {
        console.log(err)
    }
});
app.post('/api/auth/login', async (req, res) => {
    try {
        let user = await userModel.findOne({ email: req.body.email });
        if (!user) {
            res.send({ auth: false, msg: 'No User Found, Please Register' })
        } else {
            const passwordIsValid = bcrypt.compareSync(req.body.password, user.password);

            if (!passwordIsValid) {
                res.send({ auth: false, msg: 'Invalid Password' })
            }

            // if both email & password are correct, create a JWT token and send it back to user
            let token = jwt.sign({ id: user._id }, "mySecretToken", { expiresIn: 60 * 2 });
            res.send({ auth: true, token, expiresIn: 60 * 2 })
        }
    } catch (err) {
        res.send({ auth: false, msg: 'Error While Login' })
    }
});
app.get('/api/auth/products', async (req, res) => {
    let token = req.headers['my-token'];
    if (!token) {
        res.send({ auth: false, msg: 'No Token Found' })
    }
    //Verify the token
    try {
        jwt.verify(token, 'mySecretToken');
        res.send({ auth: true, products: [{}, {}] })
    } catch (err) {
        res.send({ auth: false, msg: 'Invalid Token' })
    }
})
app.listen(PORT, () => { console.log(`Server running on port ${PORT}`) })

console.log('End of the file')