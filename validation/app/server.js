var http = require("http");
var express = require('express');
// var bodyParser = require('body-parser');
var fs = require("fs");
var path = require('path');
var router = express.Router();

var app = express();
// // app.use(bodyParser.json());
// app.use(bodyParser.urlencoded({extended: false}));
app.use('/static', express.static(path.join(__dirname, 'static')));

app.get('*', function(req, res) {
  res.sendFile('./index.html', {
    root: __dirname
  });
});


router.get('/test', function(req, res, next) {
  return res.json({
    message: 'hello'
  });
});

app.use(router);
http.createServer(app)
.listen(5000, function (err) {
  if (err) console.log(err);
  console.log("Server is running on port 5000");
});
