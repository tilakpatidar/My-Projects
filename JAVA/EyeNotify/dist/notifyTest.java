
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author tilak
 */
public class notifyTest {

    
notifyTest()
{
        time t=new time();
    Thread a=new Thread(t);
    a.start();
}
static void notifyme() throws IOException{
String[] cmd = { "/usr/bin/notify-send",
                 "-t",
                 "1000",
                 "Give yourself a break ! \n Tilak !"};
    
    Runtime.getRuntime().exec(cmd);
}
public static void main(String[] args) throws Exception{
    new notifyTest();
}
class time implements Runnable{

        @Override
        public void run() {
            int i=0;
           while(i<=6) //6sec
           {
                try {
                    Thread.sleep(1000);//1 sec pause
                } catch (InterruptedException ex) {
                    Logger.getLogger(notifyTest.class.getName()).log(Level.SEVERE, null, ex);
                }
               i++;
               System.out.println(""+i);
        }
            try {
                notifyTest.notifyme();
            } catch (IOException ex) {
                Logger.getLogger(notifyTest.class.getName()).log(Level.SEVERE, null, ex);
            }
            i=0;
            new notifyTest();
            
    }
}
}


