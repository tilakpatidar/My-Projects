package cpu;


import java.awt.Dimension;
import java.awt.Toolkit;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author tilak
 */
public class Jackpot extends javax.swing.JFrame {
flash obj=new flash();
int prev;
    Thread thread=new Thread(obj);


    /**
     * Creates new form Jackpot
     */
    public Jackpot() {
        initComponents();
         Dimension dim = Toolkit.getDefaultToolkit().getScreenSize();
       int w = this.getSize().width;
        int h = this.getSize().height;
        int x = (dim.width-w)/2;
        int y = (dim.height-h)/2;
        this.setLocation(x, y);
        thread.start();
        
        
    }
    public class flash implements Runnable{
        int randomSet()
        {
            int r=0;
            int a=(int)(Math.random()*10);
             if(a>10 || a<0)
                    {
                        randomSet();
                        
                    }
             else{
                 
                 r=a; 
             }
            return r;
            
        }
int random(){
    int r = 0;
    int a=(int)(Math.random()*10);
   
    if(a>5 || a<0)
                    {
                        random();
                    }
    else{
      
    r=a;
    }
   return r;
    
}
        @Override
        public void run() {
            while(true){
                try {
                    Thread.sleep(50);
                    int s=randomSet();
                    int[] num;
                    num = new int[6];
                   
                   /* if(s==100)
                    {
                        continue;
                    }*/
                    if(s==1)
                    {
                       num[0]=0;
                       num[1]=1;
                       num[2]=2;
                       num[3]=50;
                       num[4]=4;
                       num[5]=5;
                    }
                    if(s==2)
                    {
                         num[0]=6;
                       num[1]=0;
                       num[2]=7;
                       num[3]=8;
                       num[4]=9;
                       num[5]=10;
                    }
                    if(s==3)
                    {
                         num[0]=11;
                       num[1]=12;
                       num[2]=0;
                       num[3]=13;
                       num[4]=14;
                       num[5]=15;
                    }
                    if(s==4)
                    {
                         num[0]=16;
                       num[1]=17;
                       num[2]=18;
                       num[3]=0;
                       num[4]=19;
                       num[5]=20;
                    }
                    if(s==5)
                    {
                         num[0]=21;
                       num[1]=22;
                       num[2]=23;
                       num[3]=24;
                       num[4]=0;
                       num[5]=25;
                    }
                    if(s==6)
                    {
                         num[0]=26;
                       num[1]=27;
                       num[2]=28;
                       num[3]=29;
                       num[4]=30;
                       num[5]=3;
                    }
                    if(s==7)
                    {
                         num[0]=31;
                       num[1]=32;
                       num[2]=33;
                       num[3]=34;
                       num[4]=0;
                       num[5]=35;
                    }
                    if(s==8)
                    {
                         num[0]=36;
                       num[1]=37;
                       num[2]=38;
                       num[3]=50;
                       num[4]=39;
                       num[5]=40;
                    }
                    if(s==9)
                    {
                         num[0]=41;
                       num[1]=42;
                       num[2]=21;
                       num[3]=43;
                       num[4]=44;
                       num[5]=45;
                    }
                    if(s==10)
                    {
                         num[0]=46;
                       num[1]=48;
                       num[2]=23;
                       num[3]=48;
                       num[4]=49;
                       num[5]=50;
                    }
                    int t=random();
                 /*  if(t==100){
                       continue;
                   }*/
                        int n;
                         
                    n=num[t];
                      System.out.println(n);
                    String temp=""+n;
                    int l=temp.length();
                    if(l==1)
                    {
                        jButton1.setText(""+0);
                        jButton2.setText(""+n);
                        System.out.println("SINGLE DIGIT "+n);
                    }
                    else if(l==2)
                    {
                        jButton1.setText(""+temp.charAt(0));
                        jButton2.setText(""+temp.charAt(1));
                        System.out.println(" first digit "+temp.charAt(0));
                        System.out.println(" second digit "+temp.charAt(1));
                    }
                    
                   
                        
                    
                   
                
                   
                  
                   
                    
                } catch (Exception ex) {
                    
                    Logger.getLogger(Jackpot.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jPanel1.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jButton1.setFont(new java.awt.Font("Times New Roman", 1, 48)); // NOI18N
        jButton1.setText("0");
        jButton1.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton1.setContentAreaFilled(false);
        jButton1.setEnabled(false);
        jButton1.setFocusPainted(false);
        jPanel1.add(jButton1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 30, 60, -1));

        jButton2.setFont(new java.awt.Font("Times New Roman", 1, 48)); // NOI18N
        jButton2.setText("0");
        jButton2.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton2.setContentAreaFilled(false);
        jButton2.setEnabled(false);
        jButton2.setFocusPainted(false);
        jPanel1.add(jButton2, new org.netbeans.lib.awtextra.AbsoluteConstraints(110, 30, 60, -1));

        jButton3.setFont(new java.awt.Font("Ubuntu Mono", 1, 48)); // NOI18N
        jButton3.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        jButton3.setContentAreaFilled(false);
        jButton3.setEnabled(false);
        jButton3.setFocusPainted(false);
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton3, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 30, 130, 60));

        jButton4.setText("Jackpot");
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton4, new org.netbeans.lib.awtextra.AbsoluteConstraints(50, 110, 110, -1));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(35, 35, 35)
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 209, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(47, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(23, 23, 23)
                .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, 154, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(30, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
      // TODO add your handling code here:
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
   thread.stop();  
   String n1=jButton1.getText();
  
   String n2=jButton2.getText();
   String n=n1+n2;
   JOptionPane.showMessageDialog(this,"Your Jackpot prize is "+n);
   int prize=Integer.parseInt(n);
   System.exit(0);
// TODO add your handling code here:
    }//GEN-LAST:event_jButton4ActionPerformed

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
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Jackpot.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Jackpot.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Jackpot.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Jackpot.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Jackpot().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JPanel jPanel1;
    // End of variables declaration//GEN-END:variables
}
