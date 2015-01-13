/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package desktop;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;

/**
 *
 * @author tilak
 */
public class Logger {
    private static File log;
    public static FileWriter out;
    Logger(){
     
        
    }
    static{
         try {
            log=new File(System.getProperty("user.home")+File.separator+"ShitBox.log");
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
