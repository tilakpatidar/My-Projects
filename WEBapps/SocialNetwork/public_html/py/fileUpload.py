#!/usr/bin/python -v3
import cgi, os
import cgitb; cgitb.enable()




form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass
# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('files/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message)
