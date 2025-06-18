const express = require('express');
const cors = require('cors');
const { graphqlHTTP } = require('express-graphql');
const app = express();
let ToDoSchema = require('./ToDoSchema')
app.use(cors())

app.use(
    '/todos',
    graphqlHTTP({
        schema: ToDoSchema,
        graphiql: true,
    }),
);

app.listen(5000);