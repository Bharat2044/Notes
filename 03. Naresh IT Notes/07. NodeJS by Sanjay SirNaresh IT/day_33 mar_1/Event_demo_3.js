const http = require("http");

/* const server = http.createServer((req, res) => {
  res.end("Hello World!");
}); */
const server = http.createServer();
server.on("request", (req, res) => {
  res.end("Hello World!");
});
server.listen("5000", () => console.log("server is listening on port 5000"));
