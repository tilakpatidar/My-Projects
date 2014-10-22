/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package crawl;
import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
/**
 *
 * @author tilak
 */
public class Crawl {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        Connect c=new Connect("http://www.google.com");
        String code=c.getCode();
        Document doc = Jsoup.parse(code,"UTF-8");
        Elements links = doc.getElementsByTag("a");
        for (Element a:links){
            System.out.println(a.attr("href"));
        }
    
    }
    
}
