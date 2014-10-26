Breadth wise crawler
===========

Website is the main class of the project.
This is breadth wise crawler which crawls web directories breadth wise.
Features:
Serializable so that crawling can be resumed.
Due to breadth wise implementation no loss of pages over resuming.
The other classes are :
Crawl:To get a links
Connect:To get page source
Threads:To introduce parrallelism among Website
To run the crawler on a website create a new object of class Website.
Then run Website.setWebsite(String a)
Website.setWebsiteName(String a)
obj.init()
obj.crawl()
You can also set the number of threads running at a time by obj.THREAD_COUNT
Inside each thread one breadth is crawled.
author@Tilak

