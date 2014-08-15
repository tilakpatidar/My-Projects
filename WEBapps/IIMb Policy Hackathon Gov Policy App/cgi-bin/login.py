#!/usr/bin/python

import cgi
print "Content-Type: text/html\r\n\r\n"
print "<p>login page</p>"
print "<html><head><title>Login</title></head><body>"
print """<div id="fb-root"></div>"""
print """ <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>"""
print """<script type="text/javascript">
  var accesTokens;
  function statusChangeCallback(response) {
    if (response.status === 'connected') {
      accessTokens=response.authResponse.accessToken;
      getDetails(accessTokens);
    } 
  }
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
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
    FB.login(function(response){
    FB.api('/me/feed', 'post', {message: 'Using Live Street!'});
    statusChangeCallback(response);
    }, {scope: 'publish_actions'});
  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=889869211026963&version=v2.0";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
  
  function getDetails(access) {
    FB.api('/me?fields=name,first_name,friends,gender,email,last_name,link',function(response){
      $.ajax({
        type:'POST',
        contentType : 'application/json; charset=utf-8',
        data:JSON.stringify(response),
        dataType:'text',
        url:'update.py',
        success: function(result,status){
          if (status === "success")
            window.location="ui.py";
        }
      });
    });
  }
</script>

<fb:login-button scope="public_profile,email,publish_stream" onlogin="login">
</fb:login-button>

<div id="status">
</div>
  
"""
print "</body></html>"