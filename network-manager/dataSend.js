console.log('UPLOADING DATA TO THE SERVER...\n');

var net = require('net');

var redis = require("redis");
var redisClient = redis.createClient(6379,'127.0.0.1');

var mqtt    = require('mqtt');
var client  = mqtt.connect('mqtt://128.199.217.137');

var mysql      = require('mysql');
var mysqlClient = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : 'root',
    database : 'iot'
});


var cursor = '0';
var data = [];
var send = ['apikey:123'];

var keyArray = [];
var sql = "INSERT INTO data (data) VALUES ";

function removeFromCache(keyArray) {
    redisClient.del(keyArray,function (test) {
        console.log('Uploaded Entries Successfully Deleted');
        process.exit();
    });
}

function logMysql(sql) {
    mysqlClient.connect();
    sql = sql.slice(0,-1);
    sql+=";";
    console.log(sql);
    mysqlClient.query(sql, function(err, rows, fields) {
        if (!err) {
            console.log('added to the database');
            removeFromCache(keyArray);
        }
        else {
            console.log('Error while performing Query.' + err);
        }
    });

    mysqlClient.end();

}

function PostCode(dataEnter,sql) {
    var dataToSend = JSON.stringify(dataEnter);
    client.on('connect', function () {
        client.publish('test', dataToSend, {retain: false, qa: 1},function () {
            logMysql(sql);
        });
        client.end();
    });
}

function scan () {
    redisClient.scan(
        cursor,
        'MATCH', '*',
        'COUNT', '10',
        function (err, res) {
            if (err) throw err;

            // Update the cursor position for the next scan
            cursor = res[0];
            // get the SCAN result for this iteration
            var keys = res[1];


            if (keys.length > 0) {
                data = data.concat(keys);
            }

            if (cursor === '0') {
                sendData(data);
                return null;
            }

            return scan();
        }
    );
}

scan();
function sendData() {
    var count =0;
    if(data.length ==0){
        process.exit()
    }
    for(var i=0;i<data.length;i++)
    {
        keyArray.push(data[i]);
        var temp = data[i];
        var tempValue = null;
        redisClient.get(temp, function(err, reply) {
            tempValue = reply;
            sql+="('"+ tempValue+ "'),";
            send.push(tempValue);
            count+=1;
            if (count == data.length){
                // console.log('sdsd');
                PostCode(send,sql);
                // console.log(send.length);
            }
        });
    }
}
