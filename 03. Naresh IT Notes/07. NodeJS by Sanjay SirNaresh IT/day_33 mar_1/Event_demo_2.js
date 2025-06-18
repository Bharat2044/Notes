const { EventEmitter } = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('customEvent', function () {
    console.log('I am Listener-1 for customEvent')
});
eventEmitter.addListener('customEvent', function () {
    console.log('I am Listener-2 for customEvent')
});
eventEmitter.emit('customEvent')
