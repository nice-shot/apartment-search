var Promise = require('bluebird');
var request = require('request');
Promise.promisifyAll(request);

var config = require('./config.json');

function GetFilteredPosts (pages, keywords, token, since) {
    var reqs = pages.map(function getPage (page) {
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
            },
            json: true
        });
        req.pipe(es.through(function splitPage (pageData) {
                console.log(pageData);
            })).pipe(process.stdout)
        ;
    });
}

GetFilteredPosts(config.pages, config.keywords, config.token, config.since);
