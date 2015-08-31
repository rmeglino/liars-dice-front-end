var Die = function() {}

Die.randomFace = function() {
  return Math.floor(Math.random() * 6) + 1;
}
module.exports = Die;