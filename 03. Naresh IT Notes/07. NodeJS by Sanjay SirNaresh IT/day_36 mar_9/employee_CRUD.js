const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());
const { MongoClient } = require('mongodb');

let client;
async function connectToDB() {
    client = new MongoClient('mongodb://0.0.0.0:27017');
    client.connect();
    console.log('Connected  to mongoDB');
}

app.get('/employees', async (req, res) => {
    let employees = await client.db('jan_18_2024').collection('employees').find().toArray();
    res.json(employees)
})
app.get('/employees/:id', async (req, res) => {
    let employees = await client.db('jan_18_2024').collection('employees').find({ eId: +req.params.id }).toArray();
    res.json(employees[0])
})
app.post('/employees', async (req, res) => {
    const payload = req.body;
    client.db('jan_18_2024').collection('employees').insertOne(payload);
    res.status(201).send('Employee Added Successfully')
})
app.patch('/employees/:eid', async (req, res) => {
    const id = +req.params.eid;
    const payload = req.body;
    client.db('jan_18_2024').collection('employees').updateOne({eId:id},{$set:payload});
    res.status(201).send('Employee updated Successfully')
})

app.listen(5000, () => {
    connectToDB();
    console.log('Server running on port 5000')
})