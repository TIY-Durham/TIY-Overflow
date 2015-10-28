;(function(){
  angular.module('TIY-Overflow', [ 'ngRoute' ], function(BASE_URL, $routeProvider){

    $routeProvider
      .when('/', {
        redirectTo: '/questions'
      })
      .when('/login', {
        templateUrl: 'partials/signup-login.html',
        controller: function(BASE_URL, $http){
          var login = this;

          login.user = { };

          login.send = function(){
            console.log(login.user)
            // TODO: Make a hash...? Send the hash in the `Authorization` header...
            $http.get(BASE_URL + '/whoami', {
              headers: {
                Authorization: "Basic " + btoa(login.user.username + ':' + login.user.password)
              }
            }).then(function(response){
              $http.defaults.headers.common.Authorization = "Basic " + btoa(
                login.user.username + ':' + login.user.password
              );

              // TODO: Log OUT with: `$http.defaults.headers.common.Authorization = undefined`
              // TODO: Do something with `response.data`...?
            })

            // TODO: Maybe store the user's login information somewhere?
            // TODO: Redirect to another view?
          };
        },
        controllerAs: 'login'
      })
      .when('/signup', {
        templateUrl: 'partials/signup-login.html',
        controller: function($http){
          var signup = this;

          signup.user = { };

          signup.send = function($form){
            console.log(signup.user);
            // TODO: Send `signup.user` to the API for registration...
            // TODO: Do something with what we get back?
            // TODO: Maybe store the user's login information somewhere...?
            // TODO: Redirect to another view?
          };
        },
        controllerAs: 'signup'
      })
      .when('/questions', {
        templateUrl: 'partials/question-list.html',
        controller: function($http){
          var questions = this;

          $http.get(BASE_URL + '/questions')
            .then(function(response){
              questions.all = response.data;
            });
        },
        controllerAs: 'questions'
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
  .constant('BASE_URL', 'http://localhost:8000/api');
})();
