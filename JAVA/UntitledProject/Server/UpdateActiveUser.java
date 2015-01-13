import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
public class UpdateActiveUser extends MySQLCredentials{
    public static void main(String[] args){
        try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con; 
            con = (Connection) DriverManager.getConnection("jdbc:mysql://"+MYSQL_HOSTNAME+":"+MYSQL_PORT+"/"+MYSQL_DB,MYSQL_USER,MYSQL_PSWD);
            String query="UPDATE `session` SET `active`=0 WHERE (TIME(CURRENT_TIMESTAMP-TIME('time')))>1000;--";
            int rowsEffected = con.createStatement().executeUpdate(query);
            System.out.println(""+rowsEffected);
            con.close();
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(CloseTimedOutSession.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SQLException ex) {
            Logger.getLogger(CloseTimedOutSession.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}
