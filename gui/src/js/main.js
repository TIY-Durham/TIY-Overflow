;(function(){
  angular.module('TIY-Overflow', [ 'ngRoute' ], function($routeProvider){
    $routeProvider
      .when('/', {
        redirectTo: '/questions'
      })
      .when('/questions', {
        templateUrl: 'partials/question-list.html',
      })
      .when('/questions/1', {
        templateUrl: 'partials/question-detail.html',
      })
    .otherwise('/');
  });
})();
