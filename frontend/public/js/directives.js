/* global debattle */

debattle.directive('debateListMainItemDirective', function() {
    return {
        restrict: 'A',
        templateUrl: 'public/views/assets/templates/directives/mainlistdirective.html',
        replace: true,
        scope: {
            debate: "=",
            getTimeLeft: "&",
            getTimePercentage: "&"
        }
    };
});

debattle.directive('debateListLeftItemDirective', function() {
    return {
        restrict: 'A',
        templateUrl: 'public/views/assets/templates/directives/leftlistdirective.html',
        replace: true,
        scope: {
            directiveName: "@"
        }
    };
});

debattle.directive('commentDirective', function() {
    return {
        restrict: 'A',
        templateUrl: 'public/views/assets/templates/directives/commentdirective.html',
        replace: true,
        scope: {
            comment: "="
        }
    };
});