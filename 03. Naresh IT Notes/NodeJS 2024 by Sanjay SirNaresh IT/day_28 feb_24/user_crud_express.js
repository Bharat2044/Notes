const { users } = require('../day_27 feb23/data');

const express = require('express');
const server = express();
server.get('/users', (req, res) => {
    res.send('<h1>All Users</h1>')
})
server.get('/users/:id', (req, res) => {
    res.send('<h1>1 Users</h1>')
})
server.post('/users', (req, res) => {
    res.send('<h1>Create User</h1>')
})
server.put('/users/:id', (req, res) => {
    res.send('<h1>PUT  User</h1>')
})
server.patch('/users/:id', (req, res) => {
    res.send('<h1>PATCH/Update  User</h1>')
})
server.delete('/users/:id', (req, res) => {
    res.send('<h1>Delete  User</h1>')
})

server.listen(5000, () => { console.log('Server Running on port 5000') });