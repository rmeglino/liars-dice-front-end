var Die = require("../helpers/die");
var expect = require('expect');

describe("Die", function() {
  it("generates a random face between 1 and 6", function() {
    var face = Die.randomFace();
    expect(face > 0).toEqual(true);
    expect(face < 7).toEqual(true);
  });
});