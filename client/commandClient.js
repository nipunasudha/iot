console.log(process.pid);
// require('daemon')();

var gpio = require("pi-gpio");

var mqtt    = require('mqtt');
var client  = mqtt.connect('mqtt://128.199.217.137');

client.on('connect', function () {
    client.subscribe('canorycommand');

    client.on('message', function (topic, message) {
    console.log(message.toString());
    console.log(topic.toString());
        if(topic =='canorycommand'){
        console.log("ok");
            if(message.toString()=='start'){
                gpio.open(18, "output", function(err) {
                    gpio.write(18, 1, function() {
                        console.log('pin high');
                    });
                });
            }
            else if(message.toString() =='stop'){
                gpio.open(18, "output", function(err) {
                    gpio.write(18, 0, function() {
                        console.log('pin low');
                    });
                });
            }
        }
    });
});
