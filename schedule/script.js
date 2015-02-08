	var app = angular.module('app', []);

	// app.config(function($routeProvider, $locationProvider) {
	// 	$routeProvider.when('/', {
	// 		templateUrl: 'index.html',
	// 		controller: 'AppCtrl'
	// 	})
	// });

	app.controller('AppCtrl', ['$scope', '$http', function(scope, http){

		scope.mode = 'personal';
		// console.log($routeParams);
		// dict = [{'name': 'official', 'file': 'schedule314_official.json'}, {'name': 'personal', 'file': 'schedule314.json'}];
		dict = {'official': 'schedule314_official.json', 'personal': 'schedule314.json'}
		// http.get('schedule314_official.json').success(function(data){
		http.get(dict[scope.mode]).success(function(data){
			scope.days = data;
			scope.latex = "";
			var sday, lesson;
			for(var i = 0; i < scope.days.length; i++) {
				sday = scope.days[i];
				scope.latex += "    {\\begin{Large} " + sday.day + "  \\end{Large}  \n";
				scope.latex += "        \\begin{table}[!h]\n        \\begin{tabular}{ p{3cm}  p{10cm} p{5cm} }  \n";
				for(var j = 0; j < sday.lessons.length; j++) {
					lesson = sday.lessons[j];
					scope.latex += "            " + lesson.start + " - " + lesson.end + " & " + lesson.subj + " & " + lesson.place + "\\\\\n";
				}
				scope.latex += "        \\end{tabular}\n        \\end{table} \\\\\n";
			}
		});
	}]);