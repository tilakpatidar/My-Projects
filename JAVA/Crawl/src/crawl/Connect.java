package crawl;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
public class Connect{
    private String u;
    Connect(){
        
    }
    Connect(String u){
        this.u=u;
    }
    public void setURL(String u){
        this.u=u;
    }
    public String getURL(){
        return this.u;
    }
    public String getCode(String input_url) throws MalformedURLException, IOException {

        URL url = new URL(input_url);
        BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
        String code="";
        String inputLine;
        while ((inputLine = in.readLine()) != null){
            code+=inputLine;
        }
       // System.out.println(code);
        in.close();
        return code;
    }
      public String getCode() throws MalformedURLException, IOException {

        URL url = new URL(this.u);
        BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
        String code="";
        String inputLine;
        while ((inputLine = in.readLine()) != null){
            code+=inputLine;
        }
       // System.out.println(code);
        in.close();
        return code;
    }
    
}