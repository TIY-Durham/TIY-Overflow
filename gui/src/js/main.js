;(function(){
  angular.module('TIY-Overflow', [ 'ngRoute' ], function(BASE_URL, $routeProvider){

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
      }) // END /questions
      .when('/questions/new', {
        templateUrl: 'partials/question-form.html',
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
  }) // END config
    .constant('BASE_URL', 'http://192.168.254.120:8000/api');
})();
