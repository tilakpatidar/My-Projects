/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package desktop;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.logging.Level;

/**
 *
 * @author tilak
 */
public class Terminal extends Thread{
    public static String bash;
    public static Logger log;
    public static final String LINUX_SHELL="/bin/bash";
    public static final String WIN_SHELL="cmd.exe";
    public static final String MAC_SHELL="";
    public static String EOL="\n";
    public static String ROOT_PSWD="PC";
    public static String CONT;
    public static String CD_ERROR;
    public ProcessBuilder builder;
    public Process p;
    public  BufferedWriter stdin;
    public BufferedReader stderr;
    public BufferedReader stdout;
    public String id;
    public static String PWD;
    public static String PWD_COMMAND;
    public static String OS;
    public volatile PriorityQueue<String> INPUT_QUEUE;
    public volatile PriorityQueue<String> OUTPUT_QUEUE;
    public String command;
    Terminal(String id){
       INPUT_QUEUE=new PriorityQueue();
       OUTPUT_QUEUE=new PriorityQueue();
        //this.InputCache="";
        Terminal.OS= System.getProperty("os.name").toLowerCase();
        this.id=id;
        this.log=new Logger();
        setTerminalType();
        try {
            this.builder= new ProcessBuilder(Terminal.bash);
            builder.redirectErrorStream(true);
            this.p=builder.start();
        } catch (IOException ex) {
            this.log.write(this.id+" : "+ex.getMessage());
        }
       this.stdin=new BufferedWriter(new OutputStreamWriter(this.p.getOutputStream()));
       this.stdout=new BufferedReader(new InputStreamReader(this.p.getInputStream()));
    }
    Terminal(){
        
       
    }
    public void execCommand(String cmnd){
        
        try {
            String full_command = "";
            String command=cmnd;
            if (command.contains("sudo") && (Terminal.OS.contains("linux"))){
                command=command.replaceAll("sudo","");
                full_command="cd "+Terminal.PWD+" "+Terminal.CONT+" "+"echo \""+Terminal.ROOT_PSWD+"\" | sudo -S"+" "+command+" "+Terminal.CONT+" echo \"###pwd###\" "+Terminal.CONT+Terminal.PWD_COMMAND+Terminal.CONT+" echo \"###user###\" "+Terminal.CONT+"echo $USER"+Terminal.CONT+" echo \"###hostname###\" "+Terminal.CONT+"echo $HOSTNAME";
            }
            else if((!command.contains("sudo"))&&(Terminal.OS.contains("linux"))){
                full_command="cd "+Terminal.PWD+" "+Terminal.CONT+" "+command+" "+Terminal.CONT+" echo \"###pwd###\" "+Terminal.CONT+Terminal.PWD_COMMAND+Terminal.CONT+" echo \"###user###\" "+Terminal.CONT+"echo $USER"+Terminal.CONT+" echo \"###hostname###\" "+Terminal.CONT+"echo $HOSTNAME";
            }
            else if(Terminal.OS.contains("windows")){
                
                full_command=" echo ###shit###"+Terminal.CONT+"cd "+Terminal.PWD+" "+Terminal.CONT+" "+command+" "+Terminal.CONT+" echo ###pwd### "+Terminal.CONT+Terminal.PWD_COMMAND;
            }
            
            this.stdin.write(full_command+"\n");
            this.stdin.flush();
        } catch (IOException ex) {
            java.util.logging.Logger.getLogger(Terminal.class.getName()).log(Level.SEVERE, null, ex);
        }
      
    }
    
    
   public static void setTerminalType(){
       
       if(Terminal.OS.contains("linux")){
           Terminal.bash=LINUX_SHELL;
           Terminal.CONT="&&";
           Terminal.CD_ERROR="no such file or directory";
           Terminal.PWD=System.getProperty("user.home");
           Terminal.PWD_COMMAND="pwd";
           Terminal.log.write("OS type detected is : Linux");
           
       }
       else if(Terminal.OS.contains("windows")){
           Terminal.bash=WIN_SHELL;
           Terminal.CONT="&";
           Terminal.CD_ERROR="the system cannot find the path specified";
           Terminal.PWD=System.getProperty("user.home");
           Terminal.PWD_COMMAND="echo %cd%";
           Terminal.log.write("OS type detected is : Windows");
       }
       else if(Terminal.OS.contains("mac")){
           Terminal.bash="";
           Terminal.PWD=System.getProperty("user.home");
           Terminal.log.write("OS type detected is : Mac");
           Terminal.PWD_COMMAND="pwd";
       }
       else{
           Terminal.log.write("OS type detected is : Unknown");
           Terminal.bash="";
           Terminal.PWD=System.getProperty("user.home");
           Terminal.PWD_COMMAND="pwd";
       }
       
   }
 

   public String parseXMLInput(String xml){
       /*
       
       INput given is 
       
       <terminal id="">
       <command>
       
       </command>
       </terminal>
       
       
       */
       
       
      String command;
        String[] temp=xml.split("<command>");
        command=temp[1].replace("</command>","").replace("</terminal>","");
        return command;
        /*
        
        Output is only command in string
        */
       
   }
   public String buildXMLOutput(HashMap<String,String> result){
       
       /*
       Input is a hashmap
       
       Aim is to build
       <terminal id="">
       <command></command>
       <output></output>
        <user></user>
       <hostname></hostname>
       <pwd></pwd>
       </terminal>
       */
       String idd=this.id;
       String commandd=result.get("command");
       String output=result.get("output");
       String user=result.get("user");
       String hostname=result.get("hostname");
       String pwd=result.get("pwd");
       //line ="0" means end line and just ignore the complete output and get hostname,user and pwd
       String xml="<terminal id=\""+idd+"\""+"><command>"+commandd+"</command><output line=\"0\">"+output+"</output><user>"+user+"</user><hostname>"+hostname+"</hostname><pwd>"+pwd+"</pwd></terminal>";
       return xml;
   }
   
    @Override
  public void run(){
      String input;
      while(true){
          
          if(this.INPUT_QUEUE.size()>0){
              input= this.INPUT_QUEUE.poll();
              this.command=this.parseXMLInput(input);
              this.execCommand(this.command);
              TerminalInput tin=new TerminalInput(this);
              Thread Thread_tin=new Thread(tin);
              Thread_tin.start();
              TerminalOutput tout=new TerminalOutput(this);
              Thread Thread_tout=new Thread(tout);
              Thread_tout.start();
              
          }
          
      }
      
     
  }

 
}
class TerminalOutput extends Thread{
Terminal t;
    TerminalOutput(Terminal t){
        this.t=t;
    }
    public void run(){
        String line;
        String result="";
        String pwd ="";
        String user = "";
        String hostname = "";
        String output = "";
        try {
            
            int i=1;
           
            while ((line=t.stdout.readLine())!=null){
                
                boolean add = t.OUTPUT_QUEUE.add("<terminal id=\""+t.id+"\"><command>"+t.command+"</command><output line=\""+i+"\">"+line+"</output></terminal>");
               
                result+="\n"+line;
            }
         
          //  input.close();
        } catch (IOException ex) {
            
            Terminal.log.write(t.id+" : "+ex.getMessage());
        }
         //parsing our result to get keys
        
        Terminal.log.write(result);
        if(Terminal.OS.contains("linux")){
           String[] temp=result.split("###pwd###");
           output=temp[0];
           String[] temp1=temp[1].split("###user###");
           pwd=temp1[0];
           String[] temp2=temp1[1].split("###hostname###");
           user=temp2[0];
           hostname=temp2[1];
        }
        else if(Terminal.OS.contains("windows")){
             String[] temp=result.split("###shit###");
           String main=temp[2];
           String temp1[]=main.split("###pwd###");
           output=temp1[0];
           pwd=temp1[1];
        }
        
         HashMap<String,String> map=new HashMap();
        map.put("output",output);
        map.put("pwd",pwd);
        map.put("command",t.command);
        map.put("user",user);
        map.put("hostname",hostname);
       
        result=t.buildXMLOutput(map);
        t.OUTPUT_QUEUE.add(result.replace("<output line=\"0\">","<output>"));
        
        
    }
}
class TerminalInput extends Thread{
Terminal t;
    TerminalInput(Terminal t){
        this.t=t;
        
    }
    public void run(){
        
    
      while(true){
           
       
        
        
    }
}
}