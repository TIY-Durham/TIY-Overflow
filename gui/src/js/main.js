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
        controller: function($scope, $http, $location){
          $scope.question = { };

          $scope.createQuestion = function(){
            $http.post(BASE_URL + '/questions/', $scope.question)
              .then(function(response){ // success
                /** @jamesmallen says: response.data will be:
                 *  - String URL to `question`
                 *  - Number: `question_id`
                 *  - Object: `question`
                 */
                // TODO: Do something with `response`...

                // Redirect back to "questions-list.html"...
                $location.path('/questions');
              }, function(){ // error
                console.log('It broke...');
              })
          }
        }
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
