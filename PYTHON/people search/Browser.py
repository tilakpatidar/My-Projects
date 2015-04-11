def open(url):
	print "[INFO] Runnning Ghost !"
	print "[INFO] Ghost started !"
	from selenium import webdriver
	#driver = webdriver.Chrome("/home/tilak/chromedriver")
	driver = webdriver.Firefox()
	driver.get(url)
	driver.close()
	return driver.page_source
