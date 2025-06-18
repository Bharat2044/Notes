const { EventEmitter } = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('customEvent', function () {
    console.log('A Custom Event trigerred')
});
eventEmitter.emit('customEvent')

eventEmitter.on('customEventWithParam', function (name, add) {
    console.log(`A Custom Event trigerred with params, and they are ${name} & ${add}`)
});
eventEmitter.emit('customEventWithParam', 'Sanjay', 'Bangalore')
eventEmitter.emit('customEventWithParam', 'Deepak', 'Hyderabad'); // Multiple emits