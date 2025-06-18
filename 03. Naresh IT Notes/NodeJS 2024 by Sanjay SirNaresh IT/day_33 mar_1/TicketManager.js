const { EventEmitter } = require('events');

class TicketManager extends EventEmitter {
    constructor(ticketCount) {
        super();
        this.ticketCount = ticketCount; // max ticket
    }
    buyTicket(email, price) {
        if (this.ticketCount > 0) {
            this.ticketCount--;
            this.emit('purchased', email, price, new Date().toLocaleTimeString())
        } else {
            this.emit('NoTicketAvailable', new Error('There are no more tickets left'))
        }
    }
}

module.exports = TicketManager;