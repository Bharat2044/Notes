const express = require('express');
const { createServer } = require('http');
const { Server } = require('socket.io');
const app = express();

let path = require('path');
app.use(express.static(path.join(__dirname, "public")));

const server = createServer(app);
const io = new Server(server);

io.on('connection', (socket) => {
    console.log('a user connected...');
    socket.on('setName', (name) => {
        socket.userName = name;
    });
    socket.on('chat', (msgData) => {
        const payload = {
            message: msgData.message,
            nick: socket.userName,
            time: new Date().toLocaleTimeString()
        }
        io.emit('chat', payload);
    });
});

server.listen(5000, () => {
    console.log('server running at http://localhost:5000');
});