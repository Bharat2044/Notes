const express = require('express');
const app = express();

app.get('/',(req,res)=>{
    res.status(200).send('This is Home Route')
})
app.get('/about',(req,res)=>{
    res.status(200).send('This is About Route')
})
app.get('/contactus',(req,res)=>{
    res.status(200).send('This is ContactUs Route')
})
app.get('*',(recq,res)=>{
    res.status(400).send('No Page Found')
})

app.listen(5000, () => { console.log('Server Running on port 5000') });