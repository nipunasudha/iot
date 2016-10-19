var mqtt    = require('mqtt');
var client  = mqtt.connect('mqtt://128.199.217.137');

client.on('connect', function () {
    client.publish('presence', 'Hi!', {retain: false, qa: 1});
    client.end();
});