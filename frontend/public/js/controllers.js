/* global debattle global $*/

debattle.controller('mainController', ['$log', '$http', 'timeDiffService', 'userService', function($log, $http, timeDiffService, userService) {
    
    var self = this;
    
    userService.pageName = '';
    userService.change();
    
    $http({
        method: 'GET',
        url: 'https://debattle-backend.herokuapp.com/dashboard/runningDebates'
        }).then(function successCallback(response) {
            self.runningDebates = response.data.data;
        }, function errorCallback(response) {
            $log.error(response);
    });
    
    this.calcTimeLeft = timeDiffService.calcTimeLeft;
    this.calcTimePercentage = timeDiffService.calcTimePercentage;
}]);

debattle.controller('leftController', ['userService', function(userService) {
    this.username = userService.username;
    this.pageName = userService.pageName;
}]);

debattle.controller('topController', ['userService', '$scope', function(userService, $scope) {
    var self = this;
    this.header = userService.pageName;
    $scope.$on('change', function() {
        self.header = userService.pageName;
    });
}]);

debattle.controller('newDebateController', [ 'userService', 'newDebateService', '$scope', function(userService, newDebateService, $scope) {
    var self = this;
    userService.pageName = 'Start New Debate';
    userService.change();
    this.data = newDebateService.data;
    this.submit = newDebateService.submit;
    $scope.$watch("self.data", function(newValue, oldValue) {
        newDebateService.data = self.data;
    });
}]);

debattle.controller('debateViewController', ['userService', '$routeParams', '$http', '$log', 'newCommentService', '$scope',
    function(userService, $routeParams, $http, $log, newCommentService, $scope) {
    
    var self = this;
    
    $http({
        method: 'GET',
        url: 'https://debattle-backend.herokuapp.com/comments/debate/'+$routeParams.id+'/'
        }).then(function successCallback(response) {
            self.comments = response.data.data;
            newCommentService.data.debate = $routeParams.id;
            userService.pageName = self.comments[0].title;
            userService.change();
        }, function errorCallback(response) {
            $log.error(response);
    });
    
}]);

debattle.controller('newCommentController', ['userService', '$routeParams', '$http', '$log', 'newCommentService', '$scope',
    function(userService, $routeParams, $http, $log, newCommentService, $scope) {
    
    var self = this;
    
    this.data = newCommentService.data;
    this.submit = newCommentService.submit;
    
    $scope.$watch("self.data", function(newValue, oldValue) {
        newCommentService.data = self.data;
    });
    
    $( "#comment-panel-head" ).click(function() {
        $("#comment-panel-body").toggleClass("hidden");
    });
}]);