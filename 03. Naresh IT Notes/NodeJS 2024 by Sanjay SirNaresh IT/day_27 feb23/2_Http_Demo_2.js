const http = require('http');

const server = http.createServer((req, res) => {
    console.log(req.url, req.method);
    res.write('<h1>Response From Server...</h1>');
    res.end();
});

server.listen(5000, () => { console.log('Server Running on port 5000') });

setTimeout( server.close , 5000 );