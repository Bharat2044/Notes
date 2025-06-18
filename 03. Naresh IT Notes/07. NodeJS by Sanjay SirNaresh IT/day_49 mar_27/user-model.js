const mongoose = require('mongoose');

let userSchema = new mongoose.Schema({
    name: { type: String },
    email: { type: String },
    password: { type: String },
    phone: { type: Number },
    role: { type: String },
})
const userModel = mongoose.model('users',userSchema);
module.exports = userModel;