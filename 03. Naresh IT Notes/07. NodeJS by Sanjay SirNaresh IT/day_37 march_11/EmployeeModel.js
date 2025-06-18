const mongoose = require('mongoose');

let employeeSchema = new mongoose.Schema({
    eId: {
        type: String,
        required: [true,'eId is mandatory']
    },
    name: {
        type: String
    },
    sal: {
        type: Number
    },
    gender: {
        type: String
    }
})
const employeeModel = mongoose.model('employees', employeeSchema);
module.exports = employeeModel;