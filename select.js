var hdb    = require('hdb');
var client = hdb.createClient({
  host     : 'localhost',
  port     : 30015,
  user     : 'SYSTEM',
  password : 'Azerty00'
});
client.on('error', function (err) {
  console.error('Network connection error', err);
});
client.connect(function (err) {
  if (err) {
    return console.error('Connect error', err);
  }

        client.exec('select * from HOWDOYOUFEEL.VOTE', function (err, rows) {
      client.end();
      if (err) {
        return console.error('Execute error:', err);
      }
      console.log('Results:', rows);
    });
  });


//./neo.sh open-db-tunnel -h hanatrial.ondemand.com -a p1942374509trial -u p1942374509 -i howdoyoufeel
