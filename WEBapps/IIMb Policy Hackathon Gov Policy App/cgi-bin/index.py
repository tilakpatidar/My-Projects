#!/usr/bin/python
import cgi
print "Content-Type: text/html\r\n\r\n"
print "<p>Index</p>"
print "<html><head><title>Index</title></head><body>"
print """<div id="fb-root"></div>"""
print """ <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>"""
print """<script type="text/javascript">
	var accesTokens;
  function statusChangeCallback(response) {
    if (response.status === 'connected') {
    accessTokens=response.authResponse.accessToken;
      getDetails(accessTokens);

    } else if (response.status === 'not_authorized') {
      document.getElementById('status').innerHTML = 'Please log ' +'into this app.';
        window.location='login.py';
    } else {
      document.getElementById('status').innerHTML = 'Please log ' +'into Facebook.';
        window.location='login.py';
    }
  }
  function checkLoginState(){
    FB.getLoginStatus(function(response){
      statusChangeCallback(response);
    });
  }

  window.fbAsyncInit = function() {
  FB.init({
    appId      : '889869211026963',
    cookie     : true,  // enable cookies to allow the server to access 
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.0' // use version 2.0
  });
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); 
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=889869211026963&version=v2.0";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
  
  
  function getDetails(access) {
    FB.api('/me',{fields:'friends'}, function(response) {
    	var data=jQuery.param(response);
    	console.log(response);
    	window.location="ui.py";
    });
	//getting list of friends

  }
</script>

<fb:login-button scope="public_profile,email,publish_stream" onlogin="checkLoginState();">
</fb:login-button>

<div id="status">
</div>
	
"""
print "</body></html>"
