const express = require('express');
const app = express();

var whitelist = ['http://example1.com', 'http://example2.com']
var corsOptions = {
  origin: function (origin, callback) {
    if (whitelist.includes(origin)) {
      callback(null, true)
    } else {
      callback(new Error('Not allowed by CORS'))
    }
  }
}

app.use(cors(corsOption))

let todos = [
    { id: 1, text: 'ToDo -1', completed: true },
    { id: 2, text: 'ToDo -2', completed: false },
    { id: 3, text: 'ToDo -3', completed: true },
]
app.get('/todos', (req, res) => {
    console.log("I am get route for todos")
    res.status(200).json(todos)
})

app.listen(5000, () => { console.log('Server Running on port 5000') });