const express = require('express');
const { formidable } = require('formidable');
const fs = require('fs');
const app = express();

console.log(formidable)
app.get('/', (req, res) => {
    res.send(`
      <h2>With <code>"express"</code> npm package</h2>
      <form action="/api/upload" enctype="multipart/form-data" method="post">
        <div>Text field title: <input type="text" name="title" /></div>
        <div>File: <input type="file" name="myFiles" multiple /></div>
        <input type="submit" value="Upload" />
      </form>
    `);
});
app.post('/api/upload', (req, res, next) => {
    let options = {
        multiple: true,
        // maxFileSize: 1024 * 5,
        filter: function ({ name, originalFilename, mimetype }) {
            return mimetype && mimetype.includes('image');
        }
    }
    const formidableObj = formidable(options);
    formidableObj.parse(req, (err, fields, files) => {
        if (err) {
            next(err);
            return;
        }
        for (let file of files.myFiles) {
            let oldPath = file.filepath;
            let newPath = `${__dirname}/assets/${file.originalFilename}`;
            let imageFile = fs.readFileSync(oldPath);
            fs.writeFileSync(newPath, imageFile);
        }
        res.send('Image Uploaded Successfully')
    });
});

app.listen(5000, () => {
    console.log('Server listening on http://localhost:5000 ...');
});