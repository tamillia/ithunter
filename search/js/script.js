
var app = angular.module('app', []);

function testAttachment(attch, regex, id)
{
    for(var i = 0; i < attch.length; i++) {
        if(attch[i].photo !== undefined)
            if(regex.test(attch[i].photo.text)) {var str = attch[i].photo.text; /*console.log(str.match(regex), id, i, "photo");*/ return true;}
        if(attch[i].page !== undefined)
            if(regex.test(attch[i].page.title)) {var str = attch[i].page.title; /*console.log(str.match(regex), id, i, "page");*/ return true;}
        if(attch[i].video !== undefined)
            if(regex.test(attch[i].video.title)) {var str = attch[i].video.title; /*console.log(str.match(regex), id, i, "videotitle");*/ return true;}
        // if(attch[i].doc !== undefined)
        //  if(regex.test(attch[i].doc.title)) {var str = attch[i].doc.title; console.log(str.match(regex), id, i, "doc");*/ return true;}
        if(attch[i].link !== undefined) 
            if(regex.test(attch[i].link.title)) {var str = attch[i].link.title; /*console.log(str.match(regex), id, i, "link");*/ return true;}
    }
    return false;
}

app.filter('byWord', function () {
    return function (items, query) {
        var filtered = [];
        if(!query) return items;
        query = query.replace(/([\+\?\(\)\[\]\$\<\>\\])/gim, "\\$1");
        var queryMatch = new RegExp('(^|[ \(\)\.\,\!\?"])' + query + '([ \(\)\,\!\?"]|$)', 'gim');
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            if (queryMatch.test(item.text) || (item.attachments && testAttachment(item.attachments, queryMatch, item.id))) {
                if(queryMatch.test(item.text)) {var str = item.text; /*console.log(str.match(queryMatch), item.id, "text");*/}
                filtered.push(item);
            }
        }
        return filtered;
    };
});

app.filter('byRegEx', function () {
    return function (items, queryMatch) {
        var filtered = [];
        if(!queryMatch) return items;
        var queryMatchRegEx = new RegExp(queryMatch, 'gim');
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            if (queryMatchRegEx.test(item.text) || (item.attachments && testAttachment(item.attachments, queryMatchRegEx, item.id))) {
                if(queryMatchRegEx.test(item.text)) {var str = item.text; /*console.log(str.match(queryMatchRegEx), item.id, "text");*/}
                filtered.push(item);
            }
        }
        return filtered;
    };
});

app.filter('byRegExNot', function () {
    return function (items, queryNotMatch) {
        var filtered = [];
        if(!queryNotMatch) return items;
        var queryMatchRegEx = new RegExp(queryNotMatch, 'gim');
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            if(!(queryMatchRegEx.test(item.text) || (item.attachments && testAttachment(item.attachments, queryMatchRegEx, item.id)))) {
                if(queryMatchRegEx.test(item.text)) {var str = item.text; /*console.log(str.match(queryMatchRegEx), item.id, "text");*/}
                filtered.push(item);
            }
        }
        return filtered;
    };
});

app.controller('cntntAppCtrl', ['$scope', '$http', '$sce', function (scope, http, sce){
    http.get('54530371.json').success(function(data) {
        scope.posts = data;
    });

    scope.query = '';
    scope.queryMatch = '';
    scope.queryNotMatch = '';

    scope.submit = function() {
        scope.query = scope.querySub;
        scope.queryMatch = scope.queryMatchSub;
        scope.queryNotMatch = scope.queryNotMatchSub;
    };

    scope.renderHtml = function(obj)
    {
        var text = obj.text;
        text = text.replace(/((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)/gim, "<a href='$1' target='_blank'>$1</a>");
        var attch = obj.attachments;
        var images_url = [];
        var img_url;
        for(var i = 0; i < attch.length; i++) {
            if(attch[i].photo !== undefined) {
                img_url = attch[i].photo.src_big;
                images_url.push(img_url);
                // text += "<br><br><img src='" + img_url + "' class='img-responsive'>";
            }
        }
        if(images_url !== undefined) {
            if(images_url.length == 1)
                text += "<br><br><img src='" + images_url[0] + "' class='img-responsive'>";
            else if(images_url.length == 2)
                text += "<br><br><div class='row'><div class='col-lg-6'><img src='" + images_url[0] + "' class='img-responsive'></div> \
                                      <div class='col-lg-6'><img src='" + images_url[1] + "' class='img-responsive'></div></div>";  
            else if(images_url.length == 3)
                text += "<br><br><div class='row'><div class='col-lg-6'><img src='" + images_url[0] + "' class='img-responsive'></div> \
                                      <div class='col-lg-6'><img src='" + images_url[1] + "' class='img-responsive'> \
                                      <img src='" + images_url[2] + "' class='img-responsive'></div></div>";
        }

            // if(attch[i].page !== undefined)
            //     if(regex.test(attch[i].page.title)) {var str = attch[i].page.title; /*console.log(str.match(regex), id, i, "page");*/ return true;}
            // if(attch[i].video !== undefined)
            //     if(regex.test(attch[i].video.title)) {var str = attch[i].video.title; /*console.log(str.match(regex), id, i, "videotitle");*/ return true;}
            // // if(attch[i].doc !== undefined)
            // //  if(regex.test(attch[i].doc.title)) {var str = attch[i].doc.title; console.log(str.match(regex), id, i, "doc");*/ return true;}
            // if(attch[i].link !== undefined) 
            //     if(regex.test(attch[i].link.title)) {var str = attch[i].link.title; /*console.log(str.match(regex), id, i, "link");*/ return true;}
        var html = sce.trustAsHtml(text);
        return html;
    }
}]);
