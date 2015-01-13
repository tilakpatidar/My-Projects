/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package desktop;

/**
 *
 * @author tilak
 */
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
public class Credentials {
    private static String username;
    private static String password;
    private static Logger log;
    
    static{
        log=new Logger();
    }
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
            log.write(ex.getMessage());
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
             log.write(ex.getMessage());
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
