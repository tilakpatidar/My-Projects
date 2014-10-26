import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashSet;
import java.util.Iterator;
import java.util.concurrent.ConcurrentHashMap;
import java.util.logging.Level;
import java.util.logging.Logger;
public class Website implements Serializable{
    static public String website="http://www.dmoz.org"; 
    static public String websiteName="www.dmoz.org";
    static public ConcurrentHashMap<String,HashSet<String>> map;
    static public String encode;
    static public int THREAD_COUNT=5;
    Website(){
        System.setProperty("http.proxyHost", "172.16.0.19");
        System.setProperty("http.proxyPort", "8080");
        
        
    }
    public static void init(){
        map=new ConcurrentHashMap<>();
        //Initialize the map set with some values
        Object[] links=getLinksArray(Website.website);
        if (links!=null)
            Website.addToDictionary(links);
    }
    public void crawl() throws MalformedURLException{
       
       
        Iterator i=map.keySet().iterator();
        while(true){
            while(i.hasNext() && Thread.activeCount()<Website.THREAD_COUNT){
                String parent=i.next().toString();
                Thread t=new Thread(parent){
                    
                    public void run(){
                            String parent=this.getName();
                            Object[] set=map.get(parent).toArray();
                            for(Object page:set){
                                try {
                                    URL url = new URL(parent);
                                    URL reconUrl = new URL(url, page.toString());
                                    Object[] links=getLinksArray(reconUrl.toString());
                                    if (links!=null)
                                        Website.addToDictionary(links);
                                } catch (MalformedURLException ex) {
                                    Logger.getLogger(Website.class.getName()).log(Level.SEVERE, null, ex);
                                }
                            }
                    }
                };
                t.start();
            }
            writeObjectToFile(this);
        }
       
      
    }
    public static Object[] getLinksArray(String link){
        Object[] links;
        try{
            Connect c=new Connect(link);
            links=Crawl.getALinks(c); 
            //System.out.println(""+Arrays.toString(links));
            
        }
        catch(Exception e){
             System.out.println(e.getMessage());
             return null;
        }
        
            
            return links;
        
    }
    public static void writeObjectToFile(Website w){
                try {
                        FileOutputStream fs = new FileOutputStream("testSer.ser");
                        ObjectOutputStream os = new ObjectOutputStream(fs);
                        os.writeObject(w);
                        // 3
                        os.close();
                    } 
                catch (IOException e) 
                    { 
                        e.printStackTrace(); 
                    }
            }
    public static void readObjectToFile(String filename){
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
    public static void addToDictionary(Object[] links){
        
            for(Object l:links){
                String temp=l.toString();
                String[] sp;
                String[] branches;
                //System.out.println(temp);
                if(temp.contains(Website.website)){
                    sp=temp.split(Website.website);
                    try{
                        branches=sp[1].split("/");
                    }
                    catch(ArrayIndexOutOfBoundsException e){
                        branches=new String[1];
                        branches[0]=Website.website;
                    }
                    String parent=Website.website;
                    HashSet<String> val;
                    for(String branch:branches){
                        if(!branch.equals("")){
                                
                            if(map.containsKey(parent)){
                                val=map.get(parent);
                                val.add(branch);
                                map.remove(parent);
                                map.put(parent, val);
                            }
                            else{
                                HashSet<String> set =new HashSet<>();
                                set.add(branch);
                                map.put(parent, set);
                                
                            }
                            parent+="/"+branch;   

                        } 
                    }
                }
            }
        
    }
    public void setEncodeType(String a){
        
        Website.encode=a;
    }
   
    public static void main(String[] args) throws MalformedURLException{
        Website y =new Website();
        Website.init();
        y.crawl();
        
    }
}