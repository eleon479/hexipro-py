// Set up WebSocket connection to game server
var url = 'wss://exampleurl.com/socketserver';
var protocol = 'exampleProtocol';
var socket = new WebSocket(url, protocol);

// Listen for events from the game server
socket.onmessage = function(event) {
  console.log(event.data);

  /*
    handle incoming event:
    - update local game state
    - render the board - animate();
    - ...?
  */
}

// Send an event to the game server
function sendAction(c, r, type) {
  // let the local game state know it should wait
  // for this action to be received/validated 
  // by the server

  
  var msg = {
    column: c,
    row: r,
    action: type
  };

  socket.send(JSON.stringify(msg));
}