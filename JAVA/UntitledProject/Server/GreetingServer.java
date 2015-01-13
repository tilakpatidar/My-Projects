import java.io.*;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.PriorityQueue;
import java.util.logging.Level;
/**
 *
 * @author tilak
 */


class Credentials {
    private static String username;
    private static String password;
    public static void setPassword(String pswd){
        Credentials.password=Credentials.encrypt(pswd);
    }
    public static void setUsername(String username){
        Credentials.username=Credentials.encrypt(username);
    }
    public static String encrypt(String a){
        MessageDigest md;
        StringBuffer sb = null;
        try {
            md = MessageDigest.getInstance("MD5");
            md.update(a.getBytes());
            byte[] temp=md.digest();
            sb=new StringBuffer();
            for(byte aa :temp){
                sb.append(Integer.toString((aa&0xff)+0x100,16));
            }
        } catch (NoSuchAlgorithmException ex) {
           GreetingServer.log.write(ex.getMessage());
        }
        String temp=sb.toString().concat("tilak@Google05-05-1995#IndiaSal$100000$");
        //adding salt
        MessageDigest md1;
        StringBuffer sb1 = null;
        try {
            md1 = MessageDigest.getInstance("MD5");
            md1.update(temp.getBytes());
            byte[] temp1=md1.digest();
            sb1=new StringBuffer();
            for(byte aa :temp1){
                sb1.append(Integer.toString((aa&0xff)+0x100,16));
            }
        } catch (NoSuchAlgorithmException ex) {
            GreetingServer.log.write(ex.getMessage());
        }
       return sb1.toString();
    }
    public static String getPassword(){
        
        return Credentials.password;
    }
    public static String getUsername(){
        return Credentials.username;
    }
}

class Logger {
    private static File log;
    public static FileWriter out;
    Logger(){
     
        
    }
    static{
         try {
         
            log=new File(System.getProperty("user.home")+File.separator+"ShitBoxServer.log");
          boolean createNewFile = log.createNewFile();
            out=new FileWriter(log);
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(Logger.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    public void write(String line){
        try {
            out.append(line+"\n");
            out.flush();
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(Logger.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    @Override
    public void finalize(){
        try {
            out.close();
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(Logger.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}

public class GreetingServer extends Thread
{
   private ServerSocket serverSocket;
   public static Logger log;
   public static final String MYSQL_HOSTNAME="localhost";
   public static final String MYSQL_PORT="3306";
   public static final String MYSQL_USER="root";
   public static final String MYSQL_DB="shitbox";
   public static final String MYSQL_PSWD="1";
   public boolean AUTHORIZED;
   public String username;
   public String password;
    public BufferedReader in;
    public BufferedWriter out;
    public PriorityQueue<String> INPUT;
    public PriorityQueue<String> OUTPUT;
   public GreetingServer(int port) throws IOException
   {
       AUTHORIZED=false;
      serverSocket = new ServerSocket(port);
      serverSocket.setSoTimeout(0);
      log=new Logger();
   }

   @Override
   public void run()
   {
       
       try {
           Socket server = serverSocket.accept();
           log.write("Waiting for client on port " +serverSocket.getLocalPort() + "...");
           log.write("Just connected to "+ server.getRemoteSocketAddress());
            this.in =new BufferedReader(new InputStreamReader(server.getInputStream()));
           this.out =new BufferedWriter(new OutputStreamWriter(server.getOutputStream()));
           String input=this.in.readLine();
            if(this.validConnection(input)){
                System.out.println("accepted");
                this.out.write("<flag>AUTHORIZED</flag><data></data>");
                this.out.flush();
                this.AUTHORIZED=true;
                Reader read=new Reader(this);
                Writer write=new Writer(this);
                Thread tread=new Thread(read);
                Thread twrite=new Thread(write);
                tread.start();
                twrite.start();
                tread.join();
                twrite.join();
                
               }
            else{
                            this.out.write("<flag>NOT_AUTHORIZED</flag><data></data>");
                            this.out.flush();
                            this.AUTHORIZED=false;
                }
           } catch (IOException | InterruptedException ex) {
           GreetingServer.log.write(ex.getMessage());
       }
          
       
               


           
   }
   public boolean validConnection(String xml){
       String usernamee;
       String passwordd;
       String data;
       data = null;
        try{ 
            
           String temp=xml.replace("<root>","");
           temp=temp.replace("</root>","");
           String[] t=temp.split("</username>");
           usernamee=t[0].replace("<username>","");
           temp=t[1].replace("<password>","");
           String[] t1=temp.split("</password>");
           passwordd=t1[0];
           try{
           data=t1[1].replace("<data>","").replace("</data>","");
           }
           catch(ArrayIndexOutOfBoundsException e){
                GreetingServer.log.write(e.getMessage());
               data=null;
           }
           
         
            
         //##Test##  System.out.println(username);
          //##Test##  System.out.println(password);
            
            Class.forName("com.mysql.jdbc.Driver");
            Connection con; 
            con = (Connection) DriverManager.getConnection("jdbc:mysql://"+MYSQL_HOSTNAME+":"+MYSQL_PORT+"/"+MYSQL_DB,MYSQL_USER,MYSQL_PSWD);
            String query="SELECT `username_hash`,`password_hash` FROM auth WHERE username_hash='"+usernamee+"';--";
            ResultSet rs = con.createStatement().executeQuery(query);
            String username_hash = null;
            String password_hash=null;
           
            while (rs.first()) {
               username_hash=rs.getString("username_hash");
               password_hash=rs.getString("password_hash");
               break;
            }
            con.close();
            if(usernamee.equals(username_hash) && passwordd.equals(password_hash)){
                this.username=username_hash;
                this.password=password_hash;
                return true;
            }
            
            
              return username.equals(username_hash) && password.equals(password_hash);
        }
        catch(ClassNotFoundException | SQLException e){
                   GreetingServer.log.write(e.getMessage());
                   return false;
        }
     
       
   }
   public boolean isActive(String xml){
       log.write("Checking for active user");
       String usernamee;
       try{
            String temp=xml.replace("<root>","");
           temp=temp.replace("</root>","");
           String[] t=temp.split("</username>");
           usernamee=t[0].replace("<username>","");
          // System.out.println(username);
        Class.forName("com.mysql.jdbc.Driver");
            Connection con; 
            con = (Connection) DriverManager.getConnection("jdbc:mysql://"+MYSQL_HOSTNAME+":"+MYSQL_PORT+"/"+MYSQL_DB,MYSQL_USER,MYSQL_PSWD);
            String query="SELECT `active` FROM session WHERE `username_hash`='"+usernamee+"';--";
            ResultSet rs = con.createStatement().executeQuery(query);
            String active_flag = null;
           
            while (rs.first()) {
               active_flag=rs.getString("active");
               break;
            }
            System.out.println(active_flag);
            con.close();
            if(active_flag!=null) {
               if (active_flag.equals("1")) {
                   return true;
               }
           }
            return false;
            
            
            
        }
        catch(ClassNotFoundException | SQLException e){
                   GreetingServer.log.write(e.getMessage());
                   return false;
        }
       
   }
   public static void main(String [] args)
   {
      int port = Integer.parseInt(args[0]);
      try
      {
         GreetingServer g = new GreetingServer(port);
         Thread t=new Thread(g);
         t.start();
        
      }catch(IOException e)
      {
          System.out.println(e.getMessage());
        //  GreetingServer.log.write(e.getMessage());
      }
   }
   
}
class Reader extends Thread{
    GreetingServer g;
    Reader(GreetingServer g){
        this.g=g;
    }
    public void run(){
        while(this.g.AUTHORIZED){
            try {
                //read from connection and send output to db
                String data=this.g.in.readLine();
                File f=new File("/var/www/IIMB/public_html/filestore/get/"+this.g.username);
                String dataa="";
                while(!dataa.equals("")){
                        
                        BufferedReader read1=new BufferedReader(new FileReader(f));
                        dataa=read1.readLine();
                }
               BufferedWriter write=new BufferedWriter(new FileWriter(f));
               write.write(data+"\n");
               write.flush();
               BufferedWriter write1=new BufferedWriter(new FileWriter(f));
               write1.write("");
               write1.flush();
            } catch (IOException ex) {
                java.util.logging.Logger.getLogger(Reader.class.getName()).log(Level.SEVERE, null, ex);
            }
            
        }
        
    }
}
class Writer extends Thread{
    GreetingServer g;
    Writer(GreetingServer g){
        this.g=g;
    }
    public void run(){
         while(this.g.AUTHORIZED){
             String data="";
             try {
                 //read from db and write to connection
                 File f=new File("/var/www/IIMB/public_html/filestore/set/"+this.g.username);
                 while(data.equals("")){
                     
                     BufferedReader read=new BufferedReader(new FileReader(f));
                     data=read.readLine();
                 }
            System.out.println(data);
                 this.g.out.write(data+"\n");
                 this.g.out.flush();
                 BufferedWriter write1=new BufferedWriter(new FileWriter(f));
                 write1.write("");
                 write1.flush();
             } catch (IOException ex) {
                 java.util.logging.Logger.getLogger(Writer.class.getName()).log(Level.SEVERE, null, ex);
             }
             }
        }
    }

