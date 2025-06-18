const http = require('http');

function reqListener(req,res){
    console.log(req.url,req.method,req.headers);
    res.write('<h1>Response From Server...</h1>');
    res.end();
}
const server = http.createServer(reqListener);

server.listen( 5000 , ()=>{console.log('Server Running on port 5000')})