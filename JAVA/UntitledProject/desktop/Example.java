/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */



import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Console;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/**
 *
 * @author tilak
 */
public class Example extends Thread{
    private ProcessBuilder builder;
    private Process p;
    private static BufferedWriter stdin;
    private static BufferedReader stdout;
    private static BufferedReader stderr;
    @Override
    public void run(){
         try {
            this.builder= new ProcessBuilder("/bin/bash");
            builder.redirectErrorStream(true);
            this.p=builder.start();
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage());
        }
       Example.stdin=new BufferedWriter(new OutputStreamWriter(this.p.getOutputStream()));
       Example.stdout=new BufferedReader(new InputStreamReader(this.p.getInputStream()));
       Thread input=new Thread(){
           public void run(){
               while(true){
                   try {
                       Console c=System.console();
                       String in=c.readLine();
                       
                       Example.stdin.write(in+"\n");
                       Example.stdin.flush();
                   } catch (IOException ex) {
                       Logger.getLogger(Example.class.getName()).log(Level.SEVERE, null, ex);
                   }
                 }
           }
          
       };
       input.start();
         Thread output=new Thread(){
           public void run(){
               while(true){
                   String line;
                   try {
                       while((line=Example.stdout.readLine())!=null){
                           System.out.println(line);
                       }
                       
                   } catch (IOException ex) {
                       Logger.getLogger(Example.class.getName()).log(Level.SEVERE, null, ex);
                   }
                 }
           }
          
       };
       output.start();
       
       
       
    }
     public static void main(String[] args){
         Example e=new Example();
         Thread th=new Thread(e);
         th.start();
        try {
            th.join();
        } catch (InterruptedException ex) {
            Logger.getLogger(Example.class.getName()).log(Level.SEVERE, null, ex);
        }
     }
}
