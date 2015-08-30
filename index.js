var express = require('express');
var app = express();
var mustacheExpress = require('mustache-express');
var bodyParser = require('body-parser');

var Game = require('./game');

app.engine('html', mustacheExpress());
app.set('view engine', 'html');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));


app.get('/', function(req, res) {
  res.render('documentation', {

  });
});

app.post('/games', function(req, res, next) {
  console.log(req.body);


  var game = new Game(req.body);
  game.save(function(errors) {
    if (errors) {
      res.json(errors);
    } else {
      res.json(game);  
    }
  });
});

app.post('/games/:id/claim', function(req, res) {

});

app.post('/games/:id/challenge', function(req, res) {

});

app.get('/games/:id/actions', function(req, res) {

});

var server = app.listen(8080, function() {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Listening on port %s', port);
});