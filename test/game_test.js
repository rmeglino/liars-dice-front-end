var expect = require("expect");
var Game = require("../game");

describe("Game", function() {
  describe("Initializing", function() {
    it("creates player hands if they do not exist", function() {
      var game = new Game({numPlayers: 2, numDice: 4});
      expect(game.document.playerHands.length).toEqual(2);
    });
  });

  it("saves a new game with a new id", function(done) {
    var game = new Game({numPlayers: 1, numDice: 2});

    game.save(function() {
      expect(typeof game.document._id).toNotEqual('undefined');
      done();
    });
  });
});