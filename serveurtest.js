var mqtt = require('mqtt')
var client  = mqtt.connect('mqtt://172.31.6.109', 1900)

client.on('connect', function () {

//  subscribe to a repository
  client.subscribe('projet4')

//  Publish a message
  client.publish('projet4',"test")
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  //Close connexion
  //client.end()
})
