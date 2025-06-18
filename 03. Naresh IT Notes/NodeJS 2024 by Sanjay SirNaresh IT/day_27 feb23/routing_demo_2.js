const http = require('http');

const server = http.createServer((req, res) => {
    const url = req.url;
    if (url === '/') {
        res.write('<h1>This is Home page</h1>')
    } else if (url === '/login') {
        res.writeHead(200,{ "content-type": "text/html" })
        res.write(`
        <center>
            <h2>Login Form</h2>
            <form method='post' action='login-success'>
                <p>userName : <input /></p>
                <p>password : <input type='password' /></p>
                <button type='submit'>Login</button>
            </form>
        </center>`
        )
    }else if (url === '/login-success' && req.method==='POST') {
        res.writeHead(200,{ "content-type": "text/html" })
        res.write('<h1>Login SUccess</h1>')
    }

    res.end();
});

server.listen(5000, () => { console.log('Server Running on port 5000') });