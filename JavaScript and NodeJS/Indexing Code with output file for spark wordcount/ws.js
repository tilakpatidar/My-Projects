var mv = require("mv");
function moveFile(fn){
mv("/data/New_IQT/NewCrawler5/spark/"+fn,"/data/New_IQT/NewCrawler5/completedTilak/" + fn, function(err) {
		if (!err) {
			console.log("moved");
		}
		console.log(err);
		process.send({"msg":"EXIT"});
	});

}
process.on("message",function(msg){
data=msg["data"];
fn=msg["fn"];

				d = data.toString().split("\n");
				for(l=0;l<d.length;l++){
					try{
					t=d[l].split("##delimiter##");
					var temp=filter(t[2]+" "+t[1]);
					twords=temp.split(" ");
					told=temp;
					tu=0;cc=0;
					while(tu<twords.length){

                                                tkey=twords[tu];
                                                count=0;
                                                for(to=tu;to<twords.length;to++){
                                                        if(twords[to]===tkey){
                                                                count=count+20;
                                                        }


                                                }
                                                var re = new RegExp(" "+tkey+" ","g");
                                                        told=told.replace(re," ");
                                                        twords=told.split(" ");
						        (function(k,c,t){
                                                        process.send({"key":k,"count":c,"id":t});

                                                })(tkey,count,t[0].replace(/#/g,""));



                                        tu++;
                                        }
					var temp1=filter(t[3]+" "+t[1])
					words=temp1.split(" ");
					old=temp1;
					u=0;
					while(u<words.length){
						
						key=words[u];
						count=0;
						for(o=u;o<words.length;o++){
							if(words[o]===key){
								count=count+2;
							}
							
							
						}
						var re = new RegExp(" "+key+" ","g");
							old=old.replace(re," ");
							words=old.split(" ");
						(function(k,c,t){
							process.send({"key":k,"count":c,"id":t});

						})(key,count,t[0].replace(/#/g,""));
						
						
					u++;
					}
				}
				catch(err){

//				console.log(err.stack);
				}
					
				}
				moveFile(fn);
				

});

function filter(data) {
	data = data + " ";
	//approved by sai prashanth
	data = data.replace(/®/g, " ").replace(/©/g, " ").replace(/[\.\,-\/#!<>?$%\^&\*;:\+{}=\-_`~()\[\]]/g, " ").replace(/\\u.*\s/g, " ").replace(/\\n+/g, " ").replace(/\\t+/g, " ").replace(/\\r+/g, " ").replace(/\\x.*\s/g, " ").replace(/\\/g,"").replace(/\'/g,"").replace(/\"/g,"").replace(/\\/g,"").replace(/\s+/g, " ").trim();

	return data;
}

