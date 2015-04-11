var fs = require("graceful-fs");
var mime=require("mime");

global.clearFile=function(fn){
fs.unlink("/home/srmse/Desktop/IQT/NewCrawler5/crawlNEW/"+fn, function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was cleared!");
    }
}); 


};
fs.watch("./crawlNEW/",function(event,filename){

if(event==="change"){

var m = mime.lookup(filename);
	if ((m === "text/html" || m === "application/octet-stream")){ 
			console.log("added");
	}
	else{
	console.log("DELETED");
		global.clearFile(filename);
	}

}

});
