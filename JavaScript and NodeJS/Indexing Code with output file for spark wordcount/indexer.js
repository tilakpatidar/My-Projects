var fs = require("graceful-fs");
global.files = [];
global.filescache={};
process.done = 0;
process.up = 100;
process.argv.forEach(function(element, index, array) {
	
	if (index > 1) {

		global.files.push(element);


	}

});
main(global.files);
function main(files) {
	for (i = 0; i < files.length; i++) {
(function(fn){
		fs.readFile("./spark/" + fn, function(err, data) {

			if (data) {
						var cp=require("child_process");
						var oh=cp.fork(__dirname+"/ws.js",[]);
						console.log(fn);
						oh.send({"data":data.toString(),"fn":fn});
						oh.on("message",function(m){
				//			console.log(m);
							if(global.filescache[m.key]){
							if(global.filescache[m.key][m.id]){
								global.filescache[m.key][m.id]=global.filescache[m.key][m.id]+m.count;

							}
							else{
							global.filescache[m.key][m.id]=m.count;

							}

							}
							else{
							global.filescache[m.key]={};
							global.filescache[m.key][m.id]=m.count;
							}
							if(m.msg==="EXIT"){
								console.log("child_done");
								
								++process.done;
							if(process.done===100){
								console.log("done 100 files counted");
								insertMongo();
							}
							}

						});
				
				
			

			}
			else{

			--process.up;
			}




		});
})(files[i]);



	}

}
function insertMongo(){
global.inserted=0;
global.num=Object.keys(global.filescache).length;
var MongoClient = require('mongodb').MongoClient;
MongoClient.connect("mongodb://192.168.103.59:27017/testIndex", function(err, db) {
console.log(err);
		var collection=db.collection("test");
		for(var k in global.filescache){
		(function(kk){

			collection.update({keyword:kk},{$set:global.filescache[kk]},{upsert:true},function(err,results){
			++global.inserted;
			console.log(global.inserted);
			if(global.inserted===global.num){
				db.close();
				process.send({"msg":"EXIT"});
				process.exit();
			}

			});
})(k);

		}
		
});


}
