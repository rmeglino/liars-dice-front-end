var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(':memory:');

db.run("CREATE TABLE games (id INTEGER PRIMARY KEY autoincrement NOT NULL, num_players INT NOT NULL, num_dice INT NOT NULL)");

var Game = function(options) {
  this.num_players = options.num_players;
  this.num_dice = options.num_dice;
  this.id = null;
}

Game.all = function(cb) {
  var results = [];
  db.each("SELECT * FROM games", function(error, row) {
    results.unshift(row);
  }, function() {
    cb(results);
  });
}

Game.prototype = {
  save: function(callback) {
    if (this.id == null) {
      this.create(callback);
    } else {
      this.update();
    }
  },

  create: function(cb) {
    var self = this;

    if (!this.num_players || !this.num_dice) {
      cb({
        error: "num_players and num_dice is required"
      })
      return;
    }

    var stmt = "INSERT INTO games (num_players, num_dice) VALUES ("+this.num_players+", "+this.num_dice+")";
    var response = db.run(stmt, function(error) {
      if (error) {
        cb(error);
      } else {
        self.id = this.lastID;
        cb();
      }
    });
  },

  update: function() {

  }
}

module.exports = Game;