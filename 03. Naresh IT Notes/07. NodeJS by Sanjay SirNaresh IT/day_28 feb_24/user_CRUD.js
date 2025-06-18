const http = require('http');
const { users } = require('../day_27 feb23/data');

const server = http.createServer((req, res) => {
    const { url, method } = req;
    const userId = +req.url.split("users/").pop();

    console.log(url, userId)
    if (url === '/') {
        res.write('<h1>This is Home Page</h1>')
    } else if (url === '/users' && method === 'GET') {
        res.writeHead(200, { "content-type": "application/json" })
        res.write(JSON.stringify(users))
        res.end()
    } else if (url.includes('/users') && userId && method === 'GET') {
        const user = users.find(usr => usr.id === userId)
        res.writeHead(200, { "content-type": "application/json" });
        res.write(JSON.stringify(user))
        res.end()
    } else if (url.includes('/users') && method === 'POST') {
        res.write('<h1>User Created successfully</h1>')
        res.end()
    }
});

server.listen(5000, () => { console.log('Server Running on port 5000') });