const express = require('express');
const app = express();
app.use(express.json());

let todos = [
    { id: 1, text: 'ToDo -1', completed: true },
    { id: 2, text: 'ToDo -2', completed: false },
    { id: 3, text: 'ToDo -3', completed: true },
]
app.get('/todos', (req, res) => {
    console.log("I am get route for todos")
    res.status(200).json(todos)
})
app.get('/todos/:id([0-9]{1,2})', (req, res) => {
    const todo = todos.find(todo => todo.id === +req.params.id)
    res.status(200).json(todo)
})
app.get('*', (req, res) => {
    res.status(200).send('Sorry, Page not found')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });