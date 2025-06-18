const express = require('express');
const fileUpload = require('express-fileupload');
const app = express();

app.use(fileUpload());

app.post('/upload', (req, res) => {
    console.log("routeeeeeeeee",req.files)
    let sampleFile;
    let uploadPath;

    if (!req.files || Object.keys(req.files).length == 0) {
        return res.status(400).send('No Files were uploaded.')
    }

    sampleFile = req.files.sampleFile;
    uploadPath = __dirname + '/assets/' + sampleFile.name;

    sampleFile.mv(uploadPath, function (err) {
        if (err)
            return res.status(500).send(err);

        res.send('File uploaded!');
    });

});
app.listen(5000, () => console.log('Server Running on port 5000'));
