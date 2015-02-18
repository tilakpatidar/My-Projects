var fs = require("graceful-fs");
fs.readdir("./crawlNEW/", function(err, files) {
          global.i=0;
          global.j=100;
          global.files=files;console.log("read");
          callChild();
fs.watch("./crawlNEW/",function(filename,event){

global.files.push(filename);


});




});
function callChild(){
console.log("Read " + global.files.length + " files");
             var args=global.files.slice(i,j);
             var cp=require("child_process");
var c=require("child_process");
             var oh=cp.fork(__dirname+"/oh.js",args);
             oh.on("message",function(m){
if(m.msg==="EXIT"){

                global.i+=100;
                global.j+=100;
                callChild();
}

});
}


