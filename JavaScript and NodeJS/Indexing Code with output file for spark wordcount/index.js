var fs = require("graceful-fs");
global.files=[];
process.free=true;
function readDIR(){
	fs.readdir("./spark/", function(err, files) {
		  global.i=0;
		  global.j=100;
		  global.files=files;
	});
	callChild();
}
readDIR();
function callChild(){
	console.log("Read " + global.files.length + " files");
	var args=global.files.slice(global.i,global.j);
	if(process.free && args.length===100){
		process.free=false;
		var cp=require("child_process");
		var oh=cp.fork(__dirname+"/indexer.js",args);
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
		setTimeout(function(){readDIR();},5000);
	}
}
