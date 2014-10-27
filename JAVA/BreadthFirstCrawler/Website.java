import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.net.MalformedURLException;
import java.util.HashSet;
import java.util.Iterator;
import java.util.concurrent.ConcurrentHashMap;
/*
*Website is the main class of the project.
*This is breadth wise crawler which crawls web directories breadth wise.
*Features:
*Serializable so that crawling can be resumed.
*Due to breadth wise implementation no loss of pages over resuming.
*The other classes are :
*Crawl:To get a links
*Connect:To get page source
*Threads:To introduce parrallelism among Website
*To run the crawler on a website create a new object of class Website.
*Then run Website.setWebsite(String a)
*Website.setWebsiteName(String a)
*obj.init()
*obj.crawl()
*You can also set the number of threads running at a time by obj.THREAD_COUNT
*Inside each thread one breadth is crawled.
*author@Tilak
*/
class Threads extends Thread{
    Website w;
    String parent;
    Threads(){
        
    }
    Threads(Website w,String parent){
        this.w=w;
        this.parent=parent;
    }
}
public class Website implements Serializable{
     private String website; 
     private String websiteName;
     private ConcurrentHashMap<String,HashSet<String>> map;
     private String encode;
     public int THREAD_COUNT=5;
    Website(){
        System.setProperty("http.proxyHost", "172.16.0.19");
        System.setProperty("http.proxyPort", "8080");
        
        
    }
    public void init(){
        
        map=new ConcurrentHashMap<>();
        //Initialize the map set with some values
        Object[] links=getLinksArray(this.getWebsite());
        if (links!=null)
            this.addToDictionary(links);
    }
    public void crawl() throws MalformedURLException{
       
       
        Iterator i=map.keySet().iterator();
        while(true){
            while(i.hasNext() && Thread.activeCount()<this.THREAD_COUNT){
                String parent=i.next().toString();
                
                Threads t=new Threads(this,parent){
                    
                    @Override
                    public void run(){
                            
                            Object[] set=w.map.get(this.parent).toArray();
                            for(Object page:set){
                                String reconUrl;
                                if(!this.parent.contains(".html")){
                                    String newPage="";
                                    if(this.parent.charAt(this.parent.length()-1)!='/')
                                    {
                                        this.parent=this.parent+"/";
                                        if(page.toString().length()>0){
                                            if(page.toString().charAt(0)=='/'){
                                                   newPage=page.toString().substring(1);
                                            }
                                            else{
                                                newPage=page.toString();
                                            }
                                        }
                                    }
                                    else{
                                        if(page.toString().length()>0){
                                            if(page.toString().charAt(0)=='/'){
                                                   newPage=page.toString().substring(1);
                                            }
                                            else{
                                                newPage=page.toString();
                                            }
                                        }
                                    }
                                    
                                    reconUrl=this.parent+newPage;
                                }
                                else{
                                    reconUrl=this.parent+page;
                                }
                                System.out.println(reconUrl);//Instead of printing save it in file or db
                                Object[] links=w.getLinksArray(reconUrl);
                                if (links!=null)
                                    w.addToDictionary(links);
                            }
                    }
                };
                t.start();
            }
           // writeObjectToFile(this);
        }
       
      
    }
    public  Object[] getLinksArray(String link){
        
        Object[] links;
        try{
            Connect c=new Connect(link,10000);//10 sec max time out
            links=Crawl.getALinks(c,this.getWebsite());
            //System.out.println(""+Arrays.toString(links));
            
        }
        catch(Exception e){
             System.out.println("Here"+e.getMessage());
             return null;
        }
        
            
            return links;
        
    }
    public  void writeObjectToFile(Website w){
                try {
                        FileOutputStream fs = new FileOutputStream("testSer.ser");
                        ObjectOutputStream os = new ObjectOutputStream(fs);
                        os.writeObject(w);
                        
                        os.close();
                    } 
                catch (IOException e) 
                    { 
                        e.printStackTrace(); 
                    }
            }
    public  void readObjectToFile(String filename){
        try {
                Website w=new Website();
                FileInputStream fis = new FileInputStream(filename);
                ObjectInputStream ois = new ObjectInputStream(fis);
                w = (Website) ois.readObject(); // 4
                ois.close();
            }
        catch (Exception e) 
            { 
                e.printStackTrace(); 
            }
    }
    public synchronized void addToDictionary(Object[] links){
        
            for(Object l:links){
                String temp=l.toString();
                String[] sp;
                String[] branches;
               // To satisfy the following test case
                //http://www.dmoz.org/docs/en/about.html
                //cannot split it as http://www.dmoz.org/docs/ is a dir not page
                if(!temp.contains(".html")){
                    if(temp.contains(this.getWebsite())){
                        sp=temp.split(this.getWebsite());
                        try{
                            branches=sp[1].split("/");
                        }
                        catch(ArrayIndexOutOfBoundsException e){
                            branches=new String[1];
                            branches[0]=this.getWebsite();
                        }
                        String parent=this.getWebsite();
                        HashSet<String> val;
                        for(String branch:branches){
                            if(!branch.equals("")){

                                if(this.map.containsKey(parent)){
                                    val=this.map.get(parent);
                                    val.add(branch);
                                    this.map.remove(parent);
                                    this.map.put(parent, val);
                                   // System.out.println("Set added Key :"+parent+" Value : "+val);
                                }
                                else{
                                    HashSet<String> set =new HashSet<>();
                                    set.add(branch);
                                    this.map.put(parent, set);
                                   // System.out.println("Set added Key :"+parent+" Value : "+set);

                                }
                                parent+="/"+branch;   

                            } 
                        }
                    }
            }
                else{
                     HashSet<String> set =new HashSet<>();
                     set.add("");
                     this.map.put(temp, set);
                }
            }
        
    }
   public void setWebsite(String website){
       this.website=website;
   }
    public void setWebsiteName(String websiteName){
       this.websiteName=websiteName;
   }
   public String getWebsite(){
       return this.website;
   }
   public String getWebsiteName(){
       return this.websiteName;
   }
    public static void main(String[] args) throws MalformedURLException{
        Website y =new Website();
        y.setWebsite("http://www.dmoz.org");//Do not enter value like http://www.dmoz.org/
        y.setWebsiteName("www.dmoz.org");
        y.init();
        y.crawl();
        
    }
}