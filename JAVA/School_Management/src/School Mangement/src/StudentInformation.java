import java.awt.Dimension;
import java.awt.Toolkit;
import java.sql.*;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * StudentInformation.java
 *
 * Created on Aug 19, 2012, 11:42:12 AM
 */
/**
 *
 * @author Tilak PC
 */
public class StudentInformation extends javax.swing.JFrame {
String mysqlpass;
    /** Creates new form StudentInformation */
    public StudentInformation() {
        initComponents();
        
        
    }
    public StudentInformation( String mysqlpassword)
    {
        initComponents();
        mysqlpass=mysqlpassword;
        jPanel1.setVisible(false);
        Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
        
        int w = this.getSize().width;
        int h = this.getSize().height;
        int x = (dim.width-w)/2;
        int y = (dim.height-h)/2;
        this.setLocation(x, y);
        
        jPanel2.setVisible(true);
        jPanel1.setVisible(false);
        
        
    }

    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jScrollPane1 = new javax.swing.JScrollPane();
        studentinfo_textarea = new javax.swing.JTextArea();
        img_label = new javax.swing.JLabel();
        jPanel2 = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        jTextField1 = new javax.swing.JTextField();

        setResizable(false);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true), "Student Information", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Tahoma", 1, 14))); // NOI18N

        studentinfo_textarea.setColumns(20);
        studentinfo_textarea.setFont(new java.awt.Font("Calibri", 0, 18)); // NOI18N
        studentinfo_textarea.setRows(5);
        jScrollPane1.setViewportView(studentinfo_textarea);

        img_label.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        img_label.setIcon(new javax.swing.ImageIcon(getClass().getResource("/nophoto.png"))); // NOI18N
        img_label.setBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true));
        img_label.setHorizontalTextPosition(javax.swing.SwingConstants.CENTER);

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 546, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(53, 53, 53)
                .addComponent(img_label, javax.swing.GroupLayout.PREFERRED_SIZE, 183, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(78, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(20, 20, 20)
                        .addComponent(img_label, javax.swing.GroupLayout.PREFERRED_SIZE, 208, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(28, 28, 28)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 372, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(103, Short.MAX_VALUE))
        );

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 30, 880, 530));

        jPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder(new javax.swing.border.LineBorder(new java.awt.Color(0, 0, 0), 1, true), "Enter the Enrollment number"));

        jButton1.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jButton1.setText("SUBMIT");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, 364, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGap(139, 139, 139)
                        .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 113, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(22, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jTextField1, javax.swing.GroupLayout.PREFERRED_SIZE, 43, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(28, 28, 28)
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 39, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(129, 129, 129))
        );

        getContentPane().add(jPanel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(260, 210, -1, 188));

        pack();
    }// </editor-fold>//GEN-END:initComponents

private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
int enno;
enno=Integer.parseInt(jTextField1.getText());


String queryFINAL = "SELECT * FROM admission WHERE enroll_no='"+(enno)+"'";
        
     
        try{ 
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            Connection con = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/SVM","root",mysqlpass);
           
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(queryFINAL);
             
            while (rs.next()) {
               String eno = rs.getString("enroll_no");
                String FName = rs.getString("fname");
                String LName = rs.getString("lname");
                String Classs = rs.getString("class");
                String Sec = rs.getString("sec");
                String Sex = rs.getString("sex");
                String dob = rs.getString("dob");
                String FGName = rs.getString("f_g_name");
                String cat = rs.getString("category");
                String ani = rs.getString("anincome");
                String ocu = rs.getString("occupation");
                String nat = rs.getString("nationality");
                String stat = rs.getString("state");
                String Add = rs.getString("address");
                String phy = rs.getString("phych");
                String sib = rs.getString("sib");
                String hos = rs.getString("hostel");
                String conv = rs.getString("conveyence");
                String act = rs.getString("activity");
                String Pho = rs.getString("photo");
                
                
                
                studentinfo_textarea.append("Enroll no 	"+eno+"\n"+"First Name 	"+FName+"\n"+"Last Name 	"+LName+"\n"+"Class 	"+Classs+"\n"+"Sec 	"+Sec+"\n"+"Sex 	"+Sex+"\n"+"DOB	 "+dob+"\n"+"Father's Name	 "+FGName+"\n"+"Category 	"+cat+"\n"+"Annual Income	 "+ani+"\n"+"Occupation	 "+ocu+"\n"+"Nationality 	"+nat+"\n"+"State 	"+stat+"\n"+"Address	 "+Add+"\n"+"Physically Challenged	 "+phy+"\n"+"No of siblings	 "+sib+"\n"+"Hostel	 "+hos+"\n"+"Conveyence	 "+conv+"\n"+"Activity	 "+act+"\n");
           if(Pho.equals(""))
                {
                    img_label.setIcon(new javax.swing.ImageIcon(getClass().getResource("/nophoto.png")));
                }
                else
                {
                    String realphoto=Pho.replace("*","\\");
                    img_label.setIcon(new javax.swing.ImageIcon(realphoto));
                }
                
                jPanel1.setVisible(true);
                jPanel2.setVisible(false);
            }
        }
        
        catch(Exception e){
            JOptionPane.showMessageDialog(this,e.getMessage());
            JOptionPane.showMessageDialog(this,"Enter the correct enrollment number");
        }// TODO add your handling code here:
}//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Windows".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(StudentInformation.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(StudentInformation.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(StudentInformation.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(StudentInformation.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {

            public void run() {
                new StudentInformation().setVisible(true);
            }
        });
    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel img_label;
    private javax.swing.JButton jButton1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextField jTextField1;
    private javax.swing.JTextArea studentinfo_textarea;
    // End of variables declaration//GEN-END:variables
}
