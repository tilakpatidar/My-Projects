var fs = require("graceful-fs");
var mysql = require("mysql");
var bs4 = require("cheerio");
var mime=require("mime");
var mv=require("mv");
global.files=[];

process.argv.forEach(function(element,index,array){

if(index>1){

global.files.push(element);


}

});

main(global.files);
function main(files){      
 for (i = 0; i < files.length; i++) {

		

		fs.readFile("/home/srmse/Desktop/NewCrawler2/crawlNEW/"+files[i], function(err, data) {
			
				if (data) {
                                        //console.log("read");
					d = data.toString().split("###split###");
					url = d[0];

					data = d[1];
var m=mime.lookup(url);
                                   if((m==="text/html"||m==="application/octet-stream")&&(data)){
					try {
						$ = bs4.load(data);
						var t = $("title").text();
						$("[id^='footer']").remove();
						$("[id^='header']").remove();
						$("[class^='footer']").remove();
						$("[class^='header']").remove();
						$("[name^='footer']").remove();
						$("[name^='header']").remove();
						$("[class^='nav']").remove();
						$("[id^='nav']").remove();
						$("[name^='nav']").remove();
						$("header").remove();
						$("footer").remove();
						$("script").remove();
						$("style").remove();
						$("head").remove();
						$("form").remove();
						$("link").remove();
						$("[class^='widget']").remove();
						$("[id^='widget']").remove();
                                                moveFile(url.replace(/\//g,"##"));
					        dbInsert(url, filter(t), filter($("html").text()));
                                                
                                                
					} catch (err) {
						console.log(err);
					}
}

				}




			
                     
		});



	}

}
function dbInsert(u, t, b) {
	
	var row = {
		url: u,
		title: t,
		body: b
	};
var connection = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '#srmseONserver',
		database: 'test',
                connectionLimit:10
	});

connection.connect();
	var query =connection.query('INSERT INTO source_main1 SET ?', row, function(err, result) {
		//console.log(result);

               console.log(err);
	       connection.end();
                
                
		
	});


}

function moveFile(fn) {
        mv("/home/srmse/Desktop/NewCrawler2/crawlNEW/"+fn,"/home/srmse/Desktop/NewCrawler2/completed1/"+fn,function(err){
console.log("moved"+err);

});
}

function filter(data) {
	data = data.replace(/\\n+/g, "").replace(/\\t+/g, " ").replace(/\\r+/g, " ").replace(/\\n+/g, " ").replace(/\s+/g, " ").replace(/\\x\d*/g, "").replace("®","").replace("©","").trim();

	return data;
}
process.on("exit",function(){

process.send({msg:"EXIT"});
});
