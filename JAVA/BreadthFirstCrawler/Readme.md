Breadth wise crawler
===================


Website is the main class of the project. This is breadth wise crawler which crawls web directories breadth wise. 

----------


Features
-------------

Serializable so that crawling can be resumed. Due to breadth wise implementation no loss of pages over resuming. 
The other classes are : 
<b>Crawl</b>:To get a links
<b> Connect</b>:To get page source 
<b>Threads</b>:To introduce parallelism among Website .

> **Note:**

> - To run the crawler on a website create a new object of class Website.
> - Website.setWebsite(String a)
> - Website.setWebsiteName(String a) 
> - obj.init() 
> - obj.crawl()
> - You can also set the number of threads running at a time by obj.THREAD_COUNT.
> - Inside each thread one breadth is crawled.


#### <i class="icon-file"></i> Author Tilak Patidar
