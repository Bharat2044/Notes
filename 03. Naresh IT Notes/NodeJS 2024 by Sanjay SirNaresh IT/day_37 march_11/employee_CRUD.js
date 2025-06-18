const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
app.use(express.json());
const mongoose = require('mongoose');
const employeeModel = require('./EmployeeModel');

function isMongoModel(yourObject) {
    return yourObject.hasOwnProperty('schema') && yourObject.schema instanceof mongoose.Schema;
}


async function connectToDB() {
    const url = 'mongodb://0.0.0.0:27017/jan_18_2024';
    mongoose.connect(url)
    console.log('Connected  to mongoDB');
}

app.get('/employees', async (req, res) => {
    let employees = await employeeModel.find({});
    res.json(employees)
})
app.get('/employees/:id', async (req, res) => {
    let employee = await employeeModel.findById(req.params.id);
    res.json(employee)
})
app.post('/employees', async (req, res) => {
    const payload = req.body;
    const newEmp = new employeeModel(payload);
    try {
        await newEmp.save();
        res.status(201).send('Employee Added Successfully')
    } catch (err) {
        res.status(400).json(err);
    }
})
app.delete('/employees/:eid', async (req, res) => {
    await employeeModel.deleteOne({ eId: +req.params.eid });
    res.send('Employee Deleted Successfully')
})

app.listen(5000, () => {
    connectToDB();
    console.log('Server running on port 5000')
})