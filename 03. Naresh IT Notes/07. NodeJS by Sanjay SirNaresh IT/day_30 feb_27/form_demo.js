const express = require("express");
const app = express();
const path = require("path");

const jsonParser = express.json();
const formDataParser = express.urlencoded({ extended: false });

app.get("/", function (req, res) {
  res.sendFile(path.resolve("./form1.html"));
});
app.post("/submit-student-data", formDataParser, (req, res) => {
  res.send(
    `${req.body.firstName} ${req.body.lastName} submitted succesfully!!!`
  );
});

app.post("/users", jsonParser, (req, res) => {
  res.send(`${req.body.firstName} ${req.body.lastName} added successfully!!`);
});

app.listen(5000, function () {
  console.log("Node server is running..");
});