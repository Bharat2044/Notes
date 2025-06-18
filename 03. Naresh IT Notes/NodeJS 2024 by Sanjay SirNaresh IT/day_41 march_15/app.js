import express from 'express';
import axios from 'axios';
import { createClient } from 'redis';

const redisClient = await createClient()
    .on('error', err => console.log('Redis Client Error', err))
    .connect();

const app = express();

app.get('/fetchData', async (req, res) => {
    let countryName = req?.query?.country || 'india';
    const url = `https://en.wikipedia.org/w/api.php?action=parse&format=json&section=0&page=${countryName}`;

    const dataInRedis = await redisClient.get(countryName);
    if (dataInRedis) {
        console.log('Data Found in REDIS');
        // let jsonData = JSON.parse(dataInRedis);
        res.send({ 'source': 'REDIS', data: dataInRedis })
    } else {
        console.log('Data Not Found in REDIS');
        let response = await axios.get(url);
        let stringData = JSON.stringify(response.data);

        // Store data in REDIS
        await redisClient.set(countryName, stringData,{EX:60,NX:true})
        console.log('Data Stored in REDIS')

        res.send({ 'source': 'API', data: response.data })
    }
});

app.listen(5000,()=>{console.log('Server Running on port 5000')})