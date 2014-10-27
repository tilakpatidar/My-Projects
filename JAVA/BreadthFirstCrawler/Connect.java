import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
public class Connect{
    private String u;
    int time_out;
    Connect(){
        
    }
    Connect(String u){
        this.u=u;
    }
    Connect(String u,int t){
        this.u=u;
        this.time_out=t;
    }
    public void setURL(String u){
        this.u=u;
    }
    public String getURL(){
        return this.u;
    }
    public String getCode(String input_url,String Stream) throws MalformedURLException, IOException {
	//getCode() ver using url.openStream()
        URL url = new URL(input_url);
        BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream(),"UTF-8"));
        String code="";
        String inputLine;
        while ((inputLine = in.readLine()) != null){
            code+=inputLine;
        }
       // System.out.println(code);
        in.close();
        return code;
    }
      public String getCode(String input_url,int time_out) throws MalformedURLException, IOException {
	//getCode() ver using Jsoup Connect
        Document doc = Jsoup.connect(input_url).timeout(time_out).get();
        String code=doc.html();
        return code;
    }
     public String getCode() throws MalformedURLException, IOException {
	//getCode() ver using Jsoup Connect
	String code="";
	try{
        Document doc = Jsoup.connect(this.u.toString()).timeout(this.time_out).get();
        code=doc.html();
        }
        catch(Exception e){
        
        System.out.println(e.getMessage());}
        return code;
    }
    
}
