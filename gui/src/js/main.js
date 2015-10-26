;(function(){
  angular.module('TIY-Overflow', [ 'ngRoute' ], function($routeProvider){
    $routeProvider
      .when('/', {
        redirectTo: '/questions'
      })
      .when('/questions', {
        templateUrl: 'partials/question-list.html',
        controller: [ '$scope', '$http', function($scope, $http){
          $scope.all = [
            { question_id: 123,
              question_title: 'This is the title!',
              question_body: 'What is the meaning of life, the universe, and everything?',
              asker: 'username',
              created_on: String(new Date),
              modified_on: String(new Date),
            }
          ];
        } ],
      })
      .when('/questions/1', {
        templateUrl: 'partials/question-detail.html',
      })
    .otherwise('/');
  });
})();
