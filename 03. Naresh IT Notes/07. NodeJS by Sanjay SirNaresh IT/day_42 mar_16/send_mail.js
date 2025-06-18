const express = require('express');
const nodemailer = require("nodemailer");
const app = express();

app.get('/', (req, res) => {
    console.log('Server Running....')
})
app.get('/sendMail', async (req, res) => {
    // call createTransport()
    const transporter = nodemailer.createTransport({
        service: "gmail",
        auth: {
            user: "sanjaysamantra2@gmail.com",
            pass: "wjvl ayzz kbpd egxw"
        }
    });

    let mailInfo = {
        from: "sanjaysamantra2@gmail.com",
        to: ["yogeshborkar02@gmail.com", "Vmanoj.1b8@gmail.com"],
        subject: "Test Email Using NodeJS",
        html: `
            <h1>This is a test mail</h1>
            <h3 style="color:red;text-align:center">Congratulations!!!</h1>
            <p>Please follow the instructions given below to redeem this amount<p>
            <pre>
                Hello, world
                Hiiiii
                Good Morning
            </pre>
        `,
        attachments: [
            { filename: 'nodejs', path: './node.png' }
        ]
    }
    await transporter.sendMail(mailInfo);
    console.log('Mail Sent Successfully!!!');
    res.send('Mail Sent Successfully!!!')
})

app.listen(5000, () => console.log('Server Running on port 5000'));