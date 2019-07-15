var http = require('http');
var serveStatic = require('serve-static');

var serverPublicDirecotry = function() {
	var root = './';
	var options = {
		index : [ 'example/basic/index.html' ]
	};
	// var servePublic = serveStatic('public', {'index': ['index.html',
	// 'index.htm']});
	var servePublic = serveStatic(root, options);

	http.createServer(
			function handler(req, res) {
				console.log(req.method, req.url, 'HTTP' + req.httpVersion,
						req.headers); // , req is too long

				res.setHeader('Access-Control-Allow-Origin', '127.0.0.1');

				servePublic(req, res, function nextHandler(req, res) {
				});
			}).listen(1337, '127.0.0.1');
	console.log('Server running at http://127.0.0.1:1337/');
};

serverPublicDirecotry();