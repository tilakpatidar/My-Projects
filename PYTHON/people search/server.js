
var http = require("http");
var server = http.createServer(function(request, response) {
console.log(request["url"]);
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write("<!DOCTYPE \"html\">");
  response.write("<html>");
  response.write("<head>");
  response.write("<title>Hello World Page</title>");
  response.write("</head>");
  response.write("<body>");
  response.write("Hello World!");
  response.write("</body>");
  response.write("</html>");
  response.end();
});
 
server.listen(2000);
console.log("Server is listening");
/*
var spawn = require('child_process').spawn,
    py    = spawn('ls', ['-lh', '/usr']);

py.stdout.on('data', function (data) {
  console.log('stdout: ' + data);
});*/
