const { users, posts, comments } = require('./data.js');
const http = require('http');


const server = http.createServer((req, res) => {
    const url = req.url;
    if (url == '/users') {
        res.write(JSON.stringify(users))
    } else if (url === '/posts') {
        res.write(JSON.stringify(posts))
    } else if (url === '/comments') {
        res.write(JSON.stringify(comments))
    } else {
        res.writeHead(404, { "content-type": "text/html" })
        res.write('<h1>Sorry, no response')
    }
    res.end();
});

server.listen(5000, () => { console.log('Server Running on port 5000') });