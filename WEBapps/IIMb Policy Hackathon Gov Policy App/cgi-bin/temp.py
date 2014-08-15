#!/usr/bin/python
import cgi,cgitb
print "Content-Type: text/html\r\n\r\n"
print """
<!DOCTYPE html>
<html>
<head>
<title></title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
<script type="text/javascript" src="http://hpneo.github.io/gmaps/gmaps.js"></script>
<script type="text/javascript" src="http://hpneo.github.io/gmaps/prettify/prettify.js"></script>
<link href='http://fonts.googleapis.com/css?family=Convergence|Bitter|Droid+Sans|Ubuntu+Mono' rel='stylesheet' type='text/css' />
<link href='http://hpneo.github.io/gmaps/styles.css' rel='stylesheet' type='text/css' />
<link href='http://hpneo.github.io/gmaps/prettify/prettify.css' rel='stylesheet' type='text/css' />
<link rel="stylesheet" type="text/css" href="http://hpneo.github.io/gmaps/examples/examples.css" />
<script type="text/javascript">
var map;
$(document).ready(function(){
prettyPrint();
map = new GMaps({
div: '#map',
lat: -12.043333,
lng: -77.028333
});
});
</script>
</head>
<body>

<div id="body">


<div id="map"></div>


</div>

</body>
</html>
"""
