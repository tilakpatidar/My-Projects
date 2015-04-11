def init(details):
	d=details.copy()
	del d["Keywords"]
	del d["Gender"]
	print "[INFO] Starting Google+ Engine"
	from selenium import webdriver
	print "[INFO] Runnning Ghost !"
	from ghost import Ghost
	ghost = Ghost(wait_timeout=60,download_images=False)
	print "[INFO] Ghost started !"
	page, resources = ghost.open('https://plus.google.com/s/'+" ".join(d.values())+'/people')
	print "[INFO]Starting Parsing"
	from bs4 import BeautifulSoup as bs
	print bs(page.content).findAll("div",{"class":"Osd Hfb"})
	browser.quit()
