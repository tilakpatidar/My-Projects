var fs = require("graceful-fs");
var mysql = require("mysql");
var bs4 = require("cheerio");
var mime = require("mime");
global.files = [];
process.filecache = [];
process.done = 0;
process.up = 100;
process.final_inlinks=[];
process.MySQLdb= mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: '#srmseONserver1',
		database: 'test',
		connectionLimit: 10000,
		multipleStatements: true
	});

	process.MySQLdb.connect();


process.argv.forEach(function(element, index, array) {
	
	if (index > 1) {

		global.files.push(element);


	}

});
global.clean = function() {
		if (process.filecache.length === process.up) {
			console.log("100 done");
			global.dumpFiles();
		}


	};
main(global.files);

function main(files) {
	for (i = 0; i < files.length; i++) {
		fs.readFile("./crawlNEW/" + files[i], function(err, data) {

			if (data) {

				d = data.toString().split("###split###");
				if(d.length===0){
					--process.up;
					moveFile(files[i]);
					return;
				}
				url = d[0];

				data = d[1];
				var m = mime.lookup(url);
				console.log(m);

				if ((m === "text/html" || m === "application/octet-stream") && (data)) {

					try {
						urls = [];
						$ = bs4.load(data);
						var a = $("a");
						urls = [];
						a.each(function(index, element) {
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
						idd = dbInsert(url, filter(t), filter($("html").text()), urls);
						global.clean();


						global.dumpFiles = function() {
var fs=require('fs');
fs.writeFile("./monogocache/monogocache.txt"+process.filecache[0]["id"].toString(), process.final_inlinks.join("\n"), function(err) {

console.log("written to mongo cache");


});
							var p = process.filecache.splice(0, process.up);
							var f = "";
							for (k = 0; k < p.length; k++) {
								var rec = p[k];

								f += rec["id"].toString().replace(/\/n/g, "") + "##DELIMITER##" + rec["domain"].replace(/\/n/g, "") + "##DELIMITER##" + rec["title"].replace(/\/n/g, "") + "##DELIMITER##" + rec["body"].replace(/\n/g, " ") + "\n";

							}
							var fs = require('fs');
							fs.writeFile("./spark/" + p[0]["id"], f.toLowerCase(), function(err) {
								if (err) {
									console.log(err);
								} else {
									console.log("The file was saved!");
									process.MySQLdb.end();
									process.exit(0);
								}
							});

						}
						global.inlinks = function(absu,u, urlsCollection) {

							for (h = 0; h < urlsCollection.length; h++) {
								try {
									s = urlsCollection[h];
									if(s.toString().indexOf("http://")>=0){
if(s.slice(s.length-1,s.length)==="/"){
	s=s.slice(0,s.length-1);
}
process.final_inlinks.push(s);
}

else{
s=path.join(absu,s);
if(s.slice(s.length-1,s.length)==="/"){
	s=s.slice(0,s.length-1);
}
process.final_inlinks.push(s);

}

										
									
								} catch (err) {

								}
							}
						}
					} catch (err) {
					--process.up;
						console.log(err);
					}
				} else {
					--process.up;
				}

			}
else{

--process.up;
}




		});



	}

}

function dbInsert(u, t, b, uls) {



	
	var row = {};
	var q = 'INSERT INTO source_main1 (`url`,`title`,`body`,`indexed`) values ("' + u.toString() + '","' + t.toString() + '","' + b.toString().slice(0, 200) + '","true");SELECT LAST_INSERT_ID();';

	var query = process.MySQLdb.query(q, row, function(err, result) {
		console.log(err);
		if (!err) {
			console.log("push");
			var temp = {};
			temp["id"] = result[1][0]["LAST_INSERT_ID()"];
			if (u.toString().indexOf("www") === 7) {
				temp["domain"] = u.split("/")[2].split('.', 2)[1];
			} else {

				var g = u.split("/")[2].split('.');
				temp["domain"] = g.slice(0, g.length).join('.');
			}
			temp["title"] = t;
			temp["body"] = b;
			temp["filename"] = u.toString().replace(/\//g, "##");
			process.filecache.push(temp);
			moveFile(temp["filename"]);
var l=u.replace("://","@");
try{
l=l.split("/")[0].replace("@","://");
}
catch(err){
l=l.replace("@","://");
}
			global.inlinks(b,u, uls);
			global.clean();
		} else {
			moveFile(u.toString().replace(/\//g, "##"));
			--process.up;
			console.log("push error " + process.up);
			global.clean();

		}
		

	});




}

function moveFile(fn) {

	fs.unlink("./crawlNEW/" + fn, function(err) {
console.log(err);
		if (!err) {
			console.log("moved");
			global.clean();
		}
	});
}

function filter(data) {
	data = data + " ";
	//approved by sai prashanth
	data = data.replace(/®/g, " ").replace(/©/g, " ").replace(/[\.\,-\/#!<>?$%\^&\*;:\+{}=\-_`~()\[\]]/g, " ").replace(/\\u.*\s/g, " ").replace(/\\n+/g, " ").replace(/\\t+/g, " ").replace(/\\r+/g, " ").replace(/\\x.*\s/g, " ").replace(/\\/g,"").replace(/\'/g,"").replace(/\"/g,"").replace(/\\/g,"").replace(/\s+/g, " ").trim();

	return data;
}

process.on("exit", function() {

	process.send({
		msg: "EXIT"
	});
});
