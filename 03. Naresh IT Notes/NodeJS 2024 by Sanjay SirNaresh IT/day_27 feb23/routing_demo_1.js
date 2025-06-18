const http = require('http');

const server = http.createServer((req, res) => {
    const url = req.url;
    console.log(url)

    if (url == '/') {
        res.write('<h1>You are in Home Route')
    } else if (url === '/users') {
        // fetch users data from DB and return
        res.write('<h1>You are in Users Route')
    } else if (url === '/comments') {
        // fetch comments data from DB and return
        res.write('<h1>You are in Comments Route')
    } else if (url === '/createUser') {
        // fetch comments data from DB and return
        res.writeHead(201, { "content-type": "text/html" })
        res.write('<h1>User created succesfully')
    } else {
        res.writeHead(404, { "content-type": "text/html" })
        res.write('<h1>Sorry, no response')
    }
    res.end();
});

server.listen(5000, () => { console.log('Server Running on port 5000') });