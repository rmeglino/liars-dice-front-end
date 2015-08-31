var Datastore = require('nedb')
  , db = new Datastore();

var Game = function(options) {
  this.attributes = options;
}

Game.all = function(cb) {
  var results = [];
  db.find({}, function (err, docs) {
    cb(docs);
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

    if (!this.attributes.num_players || !this.attributes.num_dice) {
      cb({
        error: "num_players and num_dice is required"
      })
      return;
    }

    db.insert(this.attributes, function(error, newDoc) {
      if (error) {
        cb(error);
      } else {
        self.attributes._id = newDoc._id;
        cb();
      }
    });
  },

  update: function() {

  }
}

module.exports = Game;