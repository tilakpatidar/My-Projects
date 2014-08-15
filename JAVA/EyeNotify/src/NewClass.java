
import java.awt.Dimension;
import java.awt.Toolkit;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFrame;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author tilak
 */
public class NewClass{
 time t=new time();
    Thread a=new Thread(t);
   
time.Dialog d=t.new Dialog();
 Thread b=new Thread(d);
    
NewClass()
{
    
       
    a.start();
}
static void notifyme() throws IOException{
String[] cmd = { "/usr/bin/notify-send",
                 "-i",
                 "/home/tilak/EyeRest/bat.ico","-t","1000",
                 "Give yourself a break ! ","Tilak !"};
    
    Runtime.getRuntime().exec(cmd);
}
public static void main(String[] args) throws Exception{
    new NewClass();
}
class time implements Runnable{

        @Override
        public void run() {
            int i=0;
           while(i<=7) //7sec
           {
                try {
                    Thread.sleep(1000);//1 sec pause
                } catch (InterruptedException ex) {
                    Logger.getLogger(NewClass.class.getName()).log(Level.SEVERE, null, ex);
                }
               i++;
               System.out.println(""+i);
        }
            try {
                NewClass.notifyme();
            } catch (IOException ex) {
                Logger.getLogger(NewClass.class.getName()).log(Level.SEVERE, null, ex);
            }
                b.start();
            try {
                b.join();
            } catch (InterruptedException ex) {
                Logger.getLogger(NewClass.class.getName()).log(Level.SEVERE, null, ex);
            }
            i=0;
            new NewClass();
            
    }
        class Dialog implements Runnable{

        @Override
        public void run() {
           Frame f=new Frame();
           f.setVisible(true);
           int opt=f.getOption();
           while(opt==0)
           {
               try {
                   Thread.sleep(10);
               } catch (InterruptedException ex) {
                   Logger.getLogger(NewClass.class.getName()).log(Level.SEVERE, null, ex);
               }
               // 1 for continue
               //2 for exit
               //3 for Lock Screen
              opt=f.getOption();
           }
           if(opt==1)
           {
               
           }
           else if(opt==2)
           {
               System.exit(0);
           }
           else if(opt==3)
           {
               
               try {
                   String cmd="gnome-screensaver-command -l";
                   Runtime.getRuntime().exec(cmd);
               } catch (IOException ex) {
                   Logger.getLogger(NewClass.class.getName()).log(Level.SEVERE, null, ex);
               }
           }
        }
            
        }
}
}

