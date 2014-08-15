#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
print "Content-Type:text/html\r\n\r\n"
print """<html>
	<head>
		<link href='http://fonts.googleapis.com/css?family=Roboto+Slab:400,300' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="http://localhost/jpages/css/jPages.css"/>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
		<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
		<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
		<script src="http://localhost/jpages/js/jPages.js"></script>
		<script type="text/javascript">
			$(document).ready(function(){
				$(document).on('click','.data',function(e){
					$('.hidden').slideDown(1000);
				});
			});
		window.onload=function(){
			FB.init({
				appId:'889869211026963',
				cookie:true,
				status:true,
				xfbml:true,
				version:'v2.0'
			});	
			FB.getLoginStatus(function(response){
				FB.api('/me',function(response){
					window.response=response;
					FB.api('/me/friends',{fields:'picture'},function(response){
						for(var i=0;i<response.data.length;i++){
							$(document).ready(function(){
								$(".friends").append("<img src='"+response.data[i].picture.data.url+"'>");
							});
						}
					});
				});
    		});
		}
		$(document).ready(function(){
			$.ajax({
				type:'get',
				url:'details.py',
				success:function(response){
					$("#itemContainer").append(response);
					$(".holder").jPages({
    					containerID : "itemContainer",
    					perPage: 6,
						keyBrowse: true,
						scrollBrowse: true
  					});
				}
			});
		}); 
		$(document).on('click','.like',function(e){
			var bid=$(this).parent().attr('id');
			name=response.id;
			$.ajax({
				type:'POST',
				datatype:"json",
				url:"update-like.py?value="+name+"&id="+bid,
				success:function(e,status)
				{
					}
			});
		});
			$(document).on('click','.post',function(e){
				var post=$(this).parent().attr('id');
				var message=post+"Had been clicked";
				FB.api('/me/feed', 'post', {message: message}, function(response){
					console.log(response);
					});
				});
		(function(d, s, id) {
    		var js, fjs = d.getElementsByTagName(s)[0];
    		if (d.getElementById(id)) return;
    		js = d.createElement(s); js.id = id;
    		js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=889869211026963&version=v2.0";
    		fjs.parentNode.insertBefore(js, fjs);
  			}(document, 'script', 'facebook-jssdk'));
		function logout(){
		FB.logout(function(){
			window.location="login.py";
			});
		}
	</script>
	<style type="text/css">
		#itemContainer{
		width:1200px;
		margin:0 auto;
		background-color:black;
		}
		#details{
		font-size:18px;
		word-wrap: break-word;
		}
		.data{
		margin-left:20px;
		margin-bottom:20px;
		padding:10px;
		border-radius:5px;
		display:inline-block;
		width:300px;height:200px;
		box-shadow:0px 0px 20px 0px black;
		font-family: 'Roboto Slab', serif;
		color:white;
		}
		.holder {
    	margin: 0 auto;
		}
		img{
		padding:5px
		}
		.holder a {
    		font-size: 12px;
    		cursor: pointer;
    		margin: 0 5px;
    		color: #333;
		}
		.holder a:hover {
    		background-color: #222;
    		color: #fff;
		}
		.holder a.jp-previous { margin-right: 15px; }
		.holder a.jp-next { margin-left: 15px; }
		.holder a.jp-current, a.jp-current:hover { 
    		color: #FF4242;
    		font-weight: bold;
		}
		.holder a.jp-disabled, a.jp-disabled:hover {
    		color: #bbb;
		}
		.holder a.jp-current, a.jp-current:hover,
		.holder a.jp-disabled, a.jp-disabled:hover {
    		cursor: default; 
    		background: none;
		}
	</style>
</head>
<body>"""
print """
<button onclick="logout()">Logout</button>
<div class="wrapper" style="width:100%;height:inherit;background-color:black">
	<div id="itemContainer" style="margin-top:100px;padding:10px">
	</div>

</div>

<div class="holder"></div>
<div style="background-color:blue;height:100px;width:100px" class="hidden"></div>
"""
print "</body></html>"
