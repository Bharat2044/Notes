const express = require('express');
const cors = require('cors');
const app = express();
app.use(cors());
const { MongoClient } = require('mongodb');


// Connection URL
const url = 'mongodb://0.0.0.0:27017';
const client = new MongoClient(url);
async function main() {
    await client.connect();
    console.log('Connected successfully to server');
    return 'done.';
}
app.get('/users', async (req, res) => {
    const usersArr = await client.db('jan_18_2024').collection('users').find({}).toArray();
    res.json(usersArr);
})
main()
    .then(() => {
        app.listen(5000)
    })
    .catch(console.error)
    
