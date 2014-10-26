/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.util.ArrayList;
import java.util.Arrays;
import java.net.MalformedURLException;
/**
 *
 * @author tilak
 */
public class Crawl {

    /**
     * @param args the command line arguments
     */
    public static Object[] getALinks(Connect c,String website) throws MalformedURLException,IOException{
        String code=c.getCode();
       // System.out.println(code);
        Document doc = Jsoup.parse(code,"UTF-8");
        Elements links = doc.getElementsByTag("a");
        ArrayList<String> arr=new ArrayList<>(); 
        for (Element a:links){
        	String temp=a.attr("href").toString();
        	//System.out.println(temp);
        	if(!temp.contains("http://")){
        		if(!temp.contains("https://"))
            		arr.add(website+temp);
            	}
            
        }
       //System.out.println(Arrays.toString(arr.toArray()));
    return arr.toArray();
    }
    
}
