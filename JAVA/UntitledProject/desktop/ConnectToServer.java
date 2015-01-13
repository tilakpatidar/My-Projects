/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package desktop;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.EOFException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.PriorityQueue;
import java.util.logging.Level;

/**
 *isAuth waits to recieve msg from server thus as it returns true start writing your response.
 * @author tilak
 */
public class ConnectToServer extends Thread
{ 
        public static final  Logger log;
	public static final String serverName="172.16.7.1";
	private static final int serverPort=666;
        private static OutputStream stdinToServer;
        private static InputStream stdoutFromServer;
        private static BufferedWriter out;
        private static BufferedReader in;
        private static Socket server;
        private static boolean TIMED_OUT;
        public static boolean AUTHORIZED;
       private static String INSTRUCTION_CACHE;
       public static PriorityQueue<String> INPUT_QUEUE;
       public static PriorityQueue<String> OUTPUT_QUEUE;
       ConnectToServer(PriorityQueue<String> i,PriorityQueue<String> o){
           ConnectToServer.INPUT_QUEUE=i;
           ConnectToServer.OUTPUT_QUEUE=o;
       }
   static{
          ConnectToServer.AUTHORIZED=false;
          ConnectToServer.TIMED_OUT=false;
          log=new Logger();
          ConnectToServer.log.write("Connecting to " + serverName+ " on port " + serverPort);
           try {
               ConnectToServer.server = new Socket(ConnectToServer.serverName, ConnectToServer.serverPort);
                ConnectToServer.log.write("Just connected to "+ ConnectToServer.server.getRemoteSocketAddress());
                ConnectToServer.stdinToServer= ConnectToServer.server.getOutputStream();
                ConnectToServer.out =new BufferedWriter(new OutputStreamWriter(ConnectToServer.stdinToServer));
                ConnectToServer.stdoutFromServer= ConnectToServer.server.getInputStream();
                ConnectToServer.in =new BufferedReader(new InputStreamReader(ConnectToServer.stdoutFromServer));
                
              if(ConnectToServer.server.isConnected())
                        {
                           ConnectToServer.writeToServer("<root><username>"+Credentials.getUsername()+"</username><password>"+Credentials.getPassword()+"</password><data></data></root>");
                           ConnectToServer.log.write("Connected Yet To be Authorized");
                        }      
           } catch (IOException ex) {
               ConnectToServer.server=null;
               ConnectToServer.log.write("Connection refused " + serverName+ " on port " + serverPort);
           }
          
             
          
   }
   public static boolean isConnected(){
       if(ConnectToServer.server==null)
           return false;
       return ConnectToServer.server.isConnected();
   }
   public static boolean writeToServer(String command){
            try {
                ConnectToServer.out.write(command+"\n");
                ConnectToServer.out.flush();
               
            } catch (IOException ex) {
                java.util.logging.Logger.getLogger(ConnectToServer.class.getName()).log(Level.SEVERE, null, ex);
                return false;
            }
       
       return true;
   }
   public static String readFromServer(){
       if(ConnectToServer.AUTHORIZED){
           String temp= ConnectToServer.INSTRUCTION_CACHE;
           ConnectToServer.INSTRUCTION_CACHE="";
           return temp;
       }
       //Reads from server stream
       return null;
   }
   public static void retryConnect(){
      try {
               ConnectToServer.server = new Socket(ConnectToServer.serverName, ConnectToServer.serverPort);
                ConnectToServer.log.write("Just connected to "+ ConnectToServer.server.getRemoteSocketAddress());
                ConnectToServer.stdinToServer= ConnectToServer.server.getOutputStream();
                ConnectToServer.out =new BufferedWriter(new OutputStreamWriter(ConnectToServer.stdinToServer));
                ConnectToServer.stdoutFromServer= ConnectToServer.server.getInputStream();
                ConnectToServer.in =new BufferedReader(new InputStreamReader(ConnectToServer.stdoutFromServer));
                
              
            if(ConnectToServer.server.isConnected())
                        {
                            // System.out.println("In retry connect");
                            ConnectToServer.AUTHORIZED=false;
                            ConnectToServer.TIMED_OUT=false;
                          ConnectToServer.writeToServer("<root><username>"+Credentials.getUsername()+"</username><password>"+Credentials.getPassword()+"</password><data></data></root>\n");
                          
                          ConnectToServer.log.write("ReConnected Yet To be Authorized");
                        }    
           } catch (IOException ex) {
               ConnectToServer.server=null;
           }
   }
    public static boolean retryConnect(String data){
      try {
                ConnectToServer.server = new Socket(ConnectToServer.serverName, ConnectToServer.serverPort);
                ConnectToServer.log.write("Just connected to "+ ConnectToServer.server.getRemoteSocketAddress());
                ConnectToServer.stdinToServer= ConnectToServer.server.getOutputStream();
                ConnectToServer.out =new BufferedWriter(new OutputStreamWriter(ConnectToServer.stdinToServer));
                ConnectToServer.stdoutFromServer= ConnectToServer.server.getInputStream();
                ConnectToServer.in =new BufferedReader(new InputStreamReader(ConnectToServer.stdoutFromServer));
                
              
            if(ConnectToServer.server.isConnected())
                        {
                            // System.out.println("In retry connect");
                            ConnectToServer.AUTHORIZED=false;
                            ConnectToServer.TIMED_OUT=false;
                          ConnectToServer.writeToServer("<root><username>"+Credentials.getUsername()+"</username><password>"+Credentials.getPassword()+"</password><data>"+data+"</data></root>");
                          
                          ConnectToServer.log.write("ReConnected Yet To be Authorized");
                          return true;
                        }    
           } catch (IOException ex) {
              
          
               ConnectToServer.server=null;
               return false;
           }
    
      return false;
   }
   
   public static boolean isAuth(){
            
                String response="";
                
                    try {
                        ConnectToServer.log.write("Waiting for Authorization.");
                        response=ConnectToServer.in.readLine();
                        
                       
                      
                String inst;
                        //##test##ConnectToServer.log.write(response);
                        String[] t=response.split("</flag>");
                        response=t[0].replace("<flag>","");
                        try{
                        inst=t[1].replace("<data>","").replace("</data>","");
                        }
                        catch(Exception e){
                            ConnectToServer.log.write(e.getMessage());
                            inst="";
                        }
                       
                        switch(response){
                    case "TIMED_OUT":
                        ConnectToServer.out.close();
                        ConnectToServer.in.close();
                        ConnectToServer.TIMED_OUT=true;
                        ConnectToServer.server.close();
                          break;
                    case "AUTHORIZED":
                        ConnectToServer.AUTHORIZED=true;
                        ConnectToServer.log.write("Connection Authorized");
                         ConnectToServer.INSTRUCTION_CACHE=inst;
                        return true;
                    case "NOT_AUTHORIZED":
                        ConnectToServer.AUTHORIZED=false;
                        ConnectToServer.log.write("Wrong Credentials");
                    default:
                        return false;
                          }
                    }
                    catch(EOFException e){
                        ConnectToServer.log.write(e.getMessage());
                        ConnectToServer.AUTHORIZED=false;
                    }
                   catch (IOException ex) {
                        java.util.logging.Logger.getLogger(ConnectToServer.class.getName()).log(Level.SEVERE, null, ex);
                       ConnectToServer.AUTHORIZED=false;
                    }
                                  
                
             
       return ConnectToServer.AUTHORIZED;
       
   }
   public static boolean isTimedOut(){
       return ConnectToServer.TIMED_OUT;
   }
        @Override
   public void run(){
      while(ConnectToServer.isConnected()){
          try {
              Reader read=new Reader(this);
              Writer write=new Writer(this);
              Thread tread=new Thread(read);
              Thread twrite=new Thread(write);
              tread.start();
              twrite.start();
              tread.join();
              twrite.join();
          } catch (InterruptedException ex) {
              java.util.logging.Logger.getLogger(ConnectToServer.class.getName()).log(Level.SEVERE, null, ex);
          }
      }
   }
   
}
class Reader extends Thread
{
    ConnectToServer c;
    Reader(ConnectToServer c){
        this.c=c;
    }
    public void run(){
        while(true){
            while(ConnectToServer.isAuth()){
            String recievedInst=ConnectToServer.readFromServer();
            System.out.println(recievedInst);
            ConnectToServer.INPUT_QUEUE.add(recievedInst);
            
        }
        }
        
    }
}
class Writer extends Thread
{
    ConnectToServer c;
    Writer(ConnectToServer c){
        this.c=c;
    }
    public void run(){
        while(true){
            System.out.println(""+ConnectToServer.AUTHORIZED);
        while(ConnectToServer.AUTHORIZED){
             System.out.println(""+ConnectToServer.OUTPUT_QUEUE.size());
            if(ConnectToServer.OUTPUT_QUEUE.size()>0){
                 String data=ConnectToServer.OUTPUT_QUEUE.poll();
                 System.out.println(data);
                 ConnectToServer.writeToServer(data);
            }
           
        }
    }
    }
}
