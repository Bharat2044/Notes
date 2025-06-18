const TicketManager = require('./TicketManager');
const EmailService = require('./EmailService');

const ticketManager = new TicketManager(2);
const emailService = new EmailService();

ticketManager.on('purchased', (person, price, time) => {
    console.log(`${person} purchased a ticket for ${price} at ${time}`);
    emailService.send(person)
})
ticketManager.on('NoTicketAvailable', (err) => {
    console.log(err);
})

ticketManager.buyTicket('person-1@gmail.com', 200);
ticketManager.buyTicket('person-2@gmail.com', 300);
ticketManager.buyTicket('person-3@gmail.com', 400);