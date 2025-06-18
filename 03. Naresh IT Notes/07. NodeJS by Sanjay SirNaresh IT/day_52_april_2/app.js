const cron = require('node-cron');
const nodemailer = require("nodemailer");

async function sendEmail() {
    console.log('Sending email')
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
        `
    }
    await transporter.sendMail(mailInfo);
    console.log('Mail Sent Successfully!!!');
}

cron.schedule('* * * * *', () => {
    sendEmail();
});

