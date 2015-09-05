var es = require('event-stream');
var request = require('request');

var config = require('./config.json');

function fetchPage (pageUrl) {
    return request.get(pageUrl)
        .pipe(es.wait())
        .pipe(es.through(function filterPosts (pageData) {
            // Have we reached the last known post
            done = false;
            pageData.data.forEach(function checkPost (post) {

            });
            if (!done) {

            }

        })
    ;
}

function GetFilteredPosts (pages, keywords, token, since) {
    var reqs = [];

    function fetchPage (pageUrl) {
        return request.get(pageUrl)
            .pipe(es.wait())
            .pipe(es.parse())
            .pipe(es.through(function filterPosts (pageData) {
                // Have we reached the last known post
                done = false;
                pageData.data.forEach(function checkPost (post) {
                    if
                });
                if (!done) {

                }

            })
        ;
    }

    pages.forEach(function getPage (page) {
        var req = request.get({
            // uri: {
            //     protocol: 'https',
            //     hostname: 'graph.facebook.com',
            //     pathname: '/v2.0/' + page + '/feed/'
            // },
            url: 'https://graph.facebook.com/v2.0/' + page + '/feed/',
            qs: {
                access_token: token,
                since: since
            }
        });


        reqs.push(req.pipe(es.wait())
           .pipe(es.parse())
           .pipe(es.through(function splitPage (pageData) {

            }))
           .pipe(es.through(function filterPost (post) {

           }))
       );
    });
}

GetFilteredPosts(config.pages, config.keywords, config.token, config.since);
