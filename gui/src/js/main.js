;(function(){
  angular.module('TIY-Overflow', [ 'ngRoute' ], function($routeProvider){
    var BASE_URL = '/apis/django';

    $routeProvider
      .when('/', {
        redirectTo: '/questions'
      })
      .when('/questions', {
        templateUrl: 'partials/question-list.html',
        controller: [ '$scope', '$http', function($scope, $http){
          $http.get(BASE_URL + '/questions')
            .then(function(response){
              $scope.all = response.data;
            });
        } ],
      })
      .when('/questions/:question_id', {
        templateUrl: 'partials/question-detail.html',
        controller: function($routeParams, $scope, $http){
          // console.log($routeParams.question_id); // <-- Use the $routeParams, Luke!

          $http.get(BASE_URL + '/questions/' + $routeParams.question_id)
            .then(function(response){
              $scope.question = response.data;
            });
        }
      })
    .otherwise('/');
  });
})();
