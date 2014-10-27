import java.io.IOException;
import java.net.MalformedURLException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
public class test{
	test(){
		
	}
	 public String getCode(String input_url) throws MalformedURLException, IOException {
                System.setProperty("https.proxyHost", "172.16.0.19");
        	System.setProperty("https.proxyPort", "8080");
                System.setProperty("http.proxyHost", "172.16.0.19");
        	System.setProperty("http.proxyPort", "8080");
		Document doc = Jsoup.connect("http://www.google.com/").timeout(7000).get();
                System.out.println("hjhj"+doc);
		String code=doc.html();
                return code;
    }
	public static void main(String[] arg){
		test t=new test();
		try{
			System.out.println(t.getCode("http://dir.yahoo.com"));}
		catch(Exception e){
			System.out.println(""+e.getMessage());}
	}
}
	
