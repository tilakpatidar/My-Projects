var fs = require("graceful-fs");
process.filecache=[];
fs.readdir("./crawlNEW/", function(err, files) {
          global.i=0;
          global.j=100;
          global.files=files;
          callChild();
fs.watch("./crawlNEW/",function(filename,event){

global.files.push(filename);


});




});
function callChild(){
console.log("Read " + global.files.length + " files");
             var args=global.files.slice(global.i,global.j);
             var cp=require("child_process");
             var c=require("child_process");

             var oh=cp.fork(__dirname+"/ohn.js",args);
             oh.on("message",function(m){
if(m.msg==="EXIT"){
console.log(m.msg);
               
                global.i+=100;
                global.j+=100;
                callChild();
}

});
}


