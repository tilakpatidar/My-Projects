var fs = require("graceful-fs");
var mysql = require("mysql");
var bs4 = require("cheerio");
var mime=require("mime");
var mv=require("mv");
global.files=[];
process.filecache=[];
process.done=0;
process.up=100;
process.argv.forEach(function(element,index,array){
global.clean=function(){

if(process.filecache.length===process.up){
	console.log("100 done");
	global.dumpFiles();
}
						

};
if(index>1){

global.files.push(element);


}

});

main(global.files);
function main(files){      
 for (i = 0; i < files.length; i++) {
		fs.readFile("/home/srmse/Desktop/IQT/NewCrawler2/crawlNEW/"+files[i], function(err, data) {
			
				if (data) {
                                        
					d = data.toString().split("###split###");
					url = d[0];

					data = d[1];
var m=mime.lookup(url);

                                   if((m==="text/html"||m==="application/octet-stream")&&(data)){

					try {
                                                urls=[];
						$ = bs4.load(data);
                                                var a=$("a");
urls=[];
a.each(function(index,element){
urls.push($(this).attr("href"));


});
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
						idd=dbInsert(url, filter(t), filter($("html").text()),urls);
						global.clean();
							
							
global.dumpFiles=function(){
	var p=process.filecache.splice(0,process.up);
	var f="";
	for(k=0;k<p.length;k++){
		var rec=p[k];
f+=rec["id"].toString().replace(/\/n/g,"")+"##DELIMITER##"+rec["domain"].replace(/\/n/g,"")+"##DELIMITER##"+rec["title"].replace(/\/n/g,"")+"##DELIMITER##"+rec["body"].replace(/\n/g," ")+"\n";
	}
     var fs = require('fs');
	fs.writeFile("./spark/"+p[0]["id"],f, function(err) {
    if(err) {
        console.log(err);
    } else {
        console.log("The file was saved!");
    }
}); 

}            
                                 global.inlinks=function(idd,u,urlsCollection){

for(h=0;h<urlsCollection.length;h++){
try{
s=urlsCollection[h];
if(s.toString().indexOf(u)<=-1){
updateLinks(s,idd);
}
}
catch(err){

}
}                      
                  }		} catch (err) {
						console.log(err);
					}
}

				}




			
                     
		});



	}

}
function dbInsert(u,t,b,uls) {
	
	

var connection = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '#srmseONserver',
		database: 'test',
                connectionLimit:1000,
multipleStatements:true
	});

connection.connect();
var row={};
var q='INSERT INTO source_main1 (`url`,`title`,`body`) values ("'+escape(u.toString())+'","'+escape(b.toString().slice(0,200))+'","'+escape(t.toString())+'");SELECT LAST_INSERT_ID();';

	var query =connection.query(q, row, function(err, result) {
console.log(err);
			if(!err){
console.log("push");
							var temp={};
							temp["id"]=result[1][0]["LAST_INSERT_ID()"];
							temp["domain"]=u.split("/")[2];
							temp["title"]=t;
							temp["body"]=b;
							temp["filename"]=u.toString().replace(/\//g,"##");
							process.filecache.push(temp);
moveFile(temp["filename"]);
global.inlinks(temp["id"],u,uls);  
global.clean();
}
else{
moveFile(u.toString().replace(/\//g,"##"));
--process.up;
console.log("push error "+process.up);

}
         connection.end();       
		
	});




}

function moveFile(fn) {
        mv("/home/srmse/Desktop/IQT/NewCrawler2/crawlNEW/"+fn,"/home/srmse/Desktop/IQT/NewCrawler2/completed1/"+fn,function(err){
if(!err){
console.log("moved");
global.clean();
}
});
}

function filter(data) {
	data = data.replace(/\\n+/g, "").replace(/\\t+/g, " ").replace(/\\r+/g, " ").replace(/\\n+/g, " ").replace(/\s+/g, " ").replace(/\\x\d*/g, "").replace("®","").replace("©","").trim();

	return data;
}
function updateLinks(u,idd){

var row = {
		id:idd,
		url: u
	};
var connection = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '#srmseONserver',
		database: 'test',
                connectionLimit:1000
	});

connection.connect();
	var query =connection.query('INSERT INTO source_main_inlinks SET ? ON DUPLICATE KEY UPDATE inlinks=inlinks+1', row, function(err, result) {
	       connection.end();
                global.clean();
                
		
	});




}
process.on("exit",function(){

process.send({msg:"EXIT"});
});
