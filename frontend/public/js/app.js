/* global angular */

var debattle = angular.module('debattle', ['ngRoute']);

debattle.config(['$routeProvider', function($routeProvider) {
    
    $routeProvider
        .when('/', {
            templateUrl: 'public/views/assets/templates/pages/main.html',
            controller: 'mainController as mainvm'
        })
        .when('/new-debate', {
            templateUrl: 'public/views/assets/templates/pages/newDebate.html',
            controller: 'newDebateController as newdebatevm'
        })
        .when('/debates/:id', {
            templateUrl: 'public/views/assets/templates/pages/debateView.html',
            controller: 'debateViewController as debatevm'
        })
}]);