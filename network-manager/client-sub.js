var mqtt    = require('mqtt');
var client  = mqtt.connect('mqtt://128.199.217.137');

client.on('connect', function () {
    client.subscribe('presence');

    client.on('message', function (topic, message) {
        console.log(message.toString());
        // client.end();
    });
});