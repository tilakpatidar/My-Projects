var fs=require('fs');
var mime = require("mime");
global.clearFile=function(fn){

fs.unlink("./monogocache/"+fn, function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was cleared!");
    }
}); 


};
global.mongoInsert=function(u,l){
process.col.update({url:u},{$inc:{count:1}},{upsert:true},function(err,results){
		console.log(results);
		


	});

};
global.readFile=function(fn){
	data=fs.readFileSync("./monogocache/"+fn);

		if(data){
			console.log("file read");
			urls=data.toString().split("\n");
			console.log(urls.length);
			
			global.clearFile(fn);
			for(k=0;k<urls.length;k++){
				(function(test){
					global.mongoInsert(test,urls.length);

				})(urls[k]);

			}

		}
	
};
fs.watch("/home/srmse/Desktop/IQT/NewCrawler5/monogocache/",function(event,filename){
console.log(filename.toString());
	if(event.toString()==="change"){
	console.log("file added");
		try{
		global.readFile(filename);
		}
			catch(err){}

	}



});
var MongoClient = require('mongodb').MongoClient;
MongoClient.connect("mongodb://localhost:27017/inlinks", function(err, db) {
		var collection=db.collection("test");
		process.col=collection;
});

