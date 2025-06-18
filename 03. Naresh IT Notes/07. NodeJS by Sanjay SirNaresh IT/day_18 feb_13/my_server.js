const http = require('http');
const PORT = process.argv[2] || 5000;

// create a server
const myServer = http.createServer((req, res) => {
    res.end('<h1>This is the response from NodeJS Server...');
})

myServer.listen(PORT, () => {
    console.log(`Server is runnign on http://localhost:${PORT}`)
})
