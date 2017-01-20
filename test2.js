var mqtt = require('mqtt')
//var mysql = require('mysql');
var client  = mqtt.connect({
  host     : 'mqtt://localhost',
  port     :  30016,
  //username : 'SYSTEM',
  //password : 'Azerty00',
  //database : 'HOWDOYOUFEEL'
})

// Connects to the broker specified by the given url and options

client.on('connect', function () {
console.log("Connecté");
    /*mysql.format('select * from HOWDOYOUFEEL.VOTE', function (rows) {
          console.log("Connecté");
client.end();
              if (err) {
                return console.error('Execute error:', err);
                        }
    console.log('Results:', rows);
//console.log('Results:', rows);

      });
      */
});


client.end();
//});
