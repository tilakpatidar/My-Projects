var fs = require("graceful-fs");
var mime=require("mime");
process.free=true;
global.files=[];
         global.i=0;
          global.j=100;
function watch_dir(){
fs.watch("./crawlNEW/",function(event,filename){

if(event==="change"){

var m = mime.lookup(filename);
	if ((m === "text/html" || m === "application/octet-stream")){ 
		console.log("file added");
			global.files.push(filename);
	}
	else{
	console.log("DELETED");
		global.clearFile(filename);
	}
	callChild();

}

});
}
global.start=function(){
fs.readdir("./crawlNEW/", function(err, files1) {
 

for(g=0;g<files1.length;g++){
	var m = mime.lookup(files1[g].replace(/##/g,"/"));
	if ((m === "text/html" || m === "application/octet-stream")){ 
console.log("added");
		global.files.push(files1[g]);
	}
	else{
	console.log("DELETED");
		global.clearFile(files1[g]);
	}

	}


          callChild();





});
}
global.start();
global.clearFile=function(fn){
fs.unlink("./crawlNEW/"+fn, function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was cleared!");
    }
}); 


};
function callChild(){
console.log("Read " + global.files.length + " files");
             var args=global.files.slice(global.i,global.j);
		if(process.free && args.length===100){
	process.free=false;
            var cp=require("child_process");
             var c=require("child_process");

             var oh=cp.fork(__dirname+"/ohn.js",args);
             oh.on("message",function(m){
if(m.msg==="EXIT"){
console.log(m.msg);
                global.i+=100;
                global.j+=100;
		process.free=true;
               callChild();
}

});
}
else{
setTimeout(function(){global.start();},30000);
}
}


