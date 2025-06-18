const express = require('express');
const socket = require('socket.io');

const app = express();
const server = app.listen(5000, () => {
    console.log('server running at http://localhost:5000');
});

let a = 5;
let b = 5;

if(a == b){
    console.log('hiiii');
}

// static files
app.use(express.static('public'));

const io = socket(server);

const activeUsers = new Set();
io.on('connection', (socket) => {
    console.log('User Connected...');

    socket.on('new user', (userData) => {
        socket.user = userData;
        activeUsers.add(userData);
        io.emit('new user', [...activeUsers]);
    });
    socket.on('disconnect', () => {
        activeUsers.delete(socket.user);
        io.emit('disconnect', socket.user);
    });
    socket.on('chat message', (chatData) => {
        io.emit('chat message', chatData);
    });
    socket.on('typing', (data) => {
        // io.emit('typing',data);
        socket.broadcast.emit('typing', data);
    });
});