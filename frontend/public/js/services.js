/* global debattle */



debattle.service('userService', function($rootScope) {
    
    this.username = "";
    this.pageName = "";
    
    this.change = function() {
        $rootScope.$broadcast('change');
    }
});

debattle.service('newDebateService', ['$http', '$log', 'userService', function($http, $log, userService) {
    var self = this;
    this.data = {};
    this.data.author = userService.username;
    this.data.title = "";
    this.data.debateText = "";
    this.data.proText = "";
    this.data.conText = "";
    this.submit = function() {
        $http({
        method: 'POST',
        url: 'https://debattle-backend.herokuapp.com/createDebate',
        headers: {
            'Content-Type': undefined,
        },
        data: { title: self.data.title,
            selftext: self.data.debateText,
            pro: self.data.proText,
            con: self.data.conText,
            author: self.data.author }
        }).then(function successCallback(response) {
            
        }, function errorCallback(response) {
            $log.error(response);
            
    });
    }
}]);

debattle.service('newCommentService', ['$http', '$log', 'userService', function($http, $log, userService) {
    var self = this;
    this.data = {};
    this.data.author = "";//userService.username;
    this.data.title = "";
    this.data.text = "";
    this.data.state = "";
    this.data.debate = "";
    this.submit = function() {
        $http({
        method: 'POST',
        url: 'https://debattle-backend.herokuapp.com/createComment',
        headers: {
            'Content-Type': undefined,
        },
        data: { title: self.data.title,
            text: self.data.text,
            state: self.data.state,
            author: self.data.author, 
            debate: self.data.debate
        }
        }).then(function successCallback(response) {
            
        }, function errorCallback(response) {
            $log.error(response);
            
    });
    }
}]);


debattle.service('timeDiffService', function() {
    
    var makeDoubleDigit = function (num) {
        if(num < 10) {
            return "0" + num;
        }
        return num;
    }
    
    this.calcTimeLeft = function (startTimeStamp) {
        var now = Date.now();
        var timePassed = now-startTimeStamp*1000;
        var timeLeft = 86400000 - timePassed;
        var hoursLeft = makeDoubleDigit(Math.floor(timeLeft/(60*60*1000)));
        var minsLeft = makeDoubleDigit(Math.floor((timeLeft%(60*60*1000))/(60*1000)));
        var secsLeft = makeDoubleDigit(Math.floor((timeLeft%(60*1000)/1000)));
        return hoursLeft + ":" + minsLeft + ":" + secsLeft;
    }
    
    this.calcTimePercentage = function(startTimeStamp) {
        var now = Date.now();
        var timePassed = now-startTimeStamp*1000;
        return Math.floor(timePassed/864000);
    }
})

