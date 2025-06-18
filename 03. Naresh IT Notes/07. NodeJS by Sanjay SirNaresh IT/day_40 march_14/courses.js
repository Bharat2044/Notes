import express from 'express';
import cors from 'cors';
import { createHandler } from 'graphql-http/lib/use/http';
import { courseSchema, rootObj } from './course-schema.js';

let app = express();
app.use(cors());

const handler = createHandler({ schema: courseSchema, rootValue: rootObj, graphiql: true });
app.use('/courses', (req, res) => {
    handler(req, res);
});

app.listen(5000, () => { console.log('server running on port 5000') });
