var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(':memory:');

db.run("CREATE TABLE actions (id INTEGER PRIMARY KEY autoincrement NOT NULL, game_id INT NOT NULL, action_type string)");

var Action = function(options) {
  this.action_type = options.action_type;
  this.game_id = options.game_id;
  this.id = null;
}

Action.allForGame = function(game_id, cb) {
  var results = [];
  db.each("SELECT * FROM actions where game_id="+game_id, function(error, row) {
    results.unshift(row);
  }, function() {
    cb(results);
  });
}

Action.prototype = {

  save: function(cb) {
    var self = this;

    var stmt = "INSERT INTO actions (action_type, game_id) VALUES (\""+this.action_type+"\", "+this.game_id+")";
    var response = db.run(stmt, function(error) {
      if (error) {
        cb(error);
      } else {
        self.id = this.lastID;
        cb();
      }
    });
  },
}

module.exports = Action;