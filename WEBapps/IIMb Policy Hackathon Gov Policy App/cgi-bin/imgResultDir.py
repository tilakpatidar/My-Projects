#!/usr/bin/python
import cgi,cgitb,MySQLdb,hashlib,os,shutil
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
src='/home/tilak/Dropbox/IIMB/images/'
dest='/var/www/SRMSE/public_html/images/'
def fetchImages():
	src_files = os.listdir(src)
	fileList= os.listdir(dest)
	for f in fileList:
		os.remove(dest+"/"+f)
	for file_name in src_files:
   		full_file_name = os.path.join(src, file_name)
    		if (os.path.isfile(full_file_name)):
        		shutil.copy(full_file_name, dest)
	for f in os.listdir(dest):
    		if os.path.splitext(f)[1].lower() in ('.jpg', '.jpeg','.png'):
        		strr=os.path.join(dest, f)
			strr=strr.replace(dest,"/images/")+";;"
			print strr
fetchImages()
