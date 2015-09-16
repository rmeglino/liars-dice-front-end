'use strict';

// Declare app level module which depends on views, and components
var app = angular.module('myApp', []);

app.controller('GameController', ['$scope', function($scope) {
  $scope.games = [
    {
      _id: '12345abcde',
      numPlayers: 5,
      numDice: 5,
      actions: [
        {
          player: 1,
          actionType: 'claim',
          claimNumber: 4,
          claimFace: 5
        },
        {
          player: 0,
          actionType: 'claim',
          claimNumber: 3,
          claimFace: 5
        }
      ],
      playerHands: [
        [1,2,3,4,5],
        [5,4,3,2,1],
        [1,1,1,1,1],
        [3,3,3,3,3],
        [6,3,6,1,2]
      ]
    }
  ];
}]);
