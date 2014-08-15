/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package defaultpackage;

import java.awt.Component;
import java.awt.Dimension;
import java.lang.Exception.*;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import static java.awt.image.ImageObserver.WIDTH;
import java.nio.file.Paths;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JTable;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author tilak
 */
public class Loggerr extends javax.swing.JFrame {
MainFrame mframe;
String[] file_dest;
Object[] status;
JButton b[];

    /**
     * Creates new form Logger
     */
    public Loggerr(MainFrame frame,String[] files_abs,Object[] s) {
                Dimension dim=Toolkit.getDefaultToolkit().getScreenSize();
       int w=dim.width;
       int h=dim.height;
      
      
       this.setTitle("File Copier :  Logger");
        mframe=frame;
        file_dest=files_abs;
        status=s;
        initComponents();
        jTable1.setModel(new MyModel());
   
       jTable1.setDefaultRenderer(JButton.class,  new Renderer());
       jPanel1.setLayout(new java.awt.GridLayout(file_dest.length+1,1));
     
       int i=0;
       
    
       pack();
    }

 
public class Renderer extends DefaultTableCellRenderer{
 
        public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected,
         boolean hasFocus, int row, int column)
     {
 
        if(value instanceof JButton){
           
             JButton Button = (JButton)value;
            //you can add the image here
             
            return (JButton)value;
        }
       
       
 
        else{
            return super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
        }
     }
}
class MyModel extends javax.swing.table.DefaultTableModel{
 
    Object[][] row = new Object[file_dest.length][2];

    Object[] col = {"File Name", "Status"};
    JButton temp,temp1[];
 
    public MyModel (){
      //  temp1=new JButton[file_dest.length];
          b=new JButton[file_dest.length];
          temp1=new JButton[file_dest.length];
          JLabel opt=new JLabel("Option");
       
          jPanel1.add(opt);
 for(int k=0;k<file_dest.length;k++)
 {
     try{
     row[k][0]=file_dest[k].toString();
     //System.out.println(Paths.get(status[k].toString()));
     if(status[k].toString().equals("1")){ //1 means done
         temp1[k]=new JButton("Done");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/done.png")));
     row[k][1]=temp1[k];
     }
     else if(status[k].toString().equals("0")) //0 means wait
     {
         if(mframe.cancel.get(k).toString().equals("1")) //1 means cancelled
     {
     temp1[k]=new JButton("Cancelled");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/cancelled.png")));
     row[k][1]=temp1[k];
     }
         else
         {
     temp1[k]=new JButton("Waiting");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/wait.png")));
     row[k][1]=temp1[k];
         }
     }
     else if(status[k].toString().equals("2")) //2 means skipped
     {
     temp1[k]=new JButton("Skipped");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/skip.png")));
     row[k][1]=temp1[k];
     }
     else if(status[k].toString().equals("9")) //9 means access denied
     {
     temp1[k]=new JButton("Access Denied");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/denied.png")));
     row[k][1]=temp1[k];
     }
     else if(status[k].toString().equals("-1")) //-1 means failed
     {
     temp1[k]=new JButton("Fail");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/fail.png")));
     row[k][1]=temp1[k];
     }
     
      }
     catch(Exception ArrayOutOfBoundsException)
     {
         System.out.println(ArrayOutOfBoundsException.getMessage());
         if(mframe.cancel.get(k).toString().equals("1")) //1 means cancelled
     {
     temp1[k]=new JButton("Cancelled");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/cancelled.png")));
     row[k][1]=temp1[k];
     }
         else
         {
     temp1[k]=new JButton("Waiting");
     temp1[k].setEnabled(false);
     temp1[k].setContentAreaFilled(false);
     temp1[k].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/wait.png")));
     row[k][1]=temp1[k];
         }
     }
     
           try{
               b[k]=new JButton();
           b[k].setText("Cancel");
           if(temp1[k].getText().equals("Done"))
           {
                b[k].setEnabled(false);
           }
           else if(temp1[k].getText().equals("Access Denied"))
           {
               b[k].setEnabled(false);
           }
           else if(temp1[k].getText().equals("Waiting"))
           {
               b[k].setEnabled(true);
           }
           else if(temp1[k].getText().equals("Skipped"))
           {
               b[k].setEnabled(false);
           }
           else if(temp1[k].getText().equals("Fail"))
           {
               b[k].setEnabled(false);
           }
             else if(temp1[k].getText().equals("Cancelled"))
           {
               b[k].setEnabled(false);
           }
              
             class listen1 implements java.awt.event.ActionListener {
              int w;
              @Override
            public void actionPerformed(java.awt.event.ActionEvent evt) {
              //  System.out.println("fg");
                temp1[w]=new JButton("Cancelled");
                 temp1[w].setContentAreaFilled(false);
                 temp1[w].setEnabled(false);
                 temp1[w].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/cancelled.png")));
           b[w].setEnabled(false);
                 //    mframe.status.set(w, 3);
                 mframe.cancel.set(w,1);
                     new Loggerr(mframe,mframe.abs,mframe.status.toArray()).setVisible(true); 
                 Loggerr.this.setVisible(false);
            }
            public void dumm(int a)
            {
                w=a;
            }

          }
          listen1 df1=new listen1();
          df1.dumm(k);
          b[k].addActionListener(df1);
           jPanel1.add(b[k]);
           
           }
           catch(Exception NullPointerException)
           {
               
                   b[k]=new JButton();
           b[k].setText("Cancel");
         
               b[k].setEnabled(true);
                class listen1 implements java.awt.event.ActionListener {
              int w;
              @Override
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                
               temp1[w]=new JButton("Cancelled");
                 temp1[w].setContentAreaFilled(false);
                 temp1[w].setEnabled(false);
                 temp1[w].setIcon(new ImageIcon(getClass().getResource("/defaultpackage/cancelled.png")));
           b[w].setEnabled(false);
                 //    mframe.status.set(w, 3);
                 mframe.cancel.set(w,1);
                 new Loggerr(mframe,mframe.abs,mframe.status.toArray()).setVisible(true); 
                 Loggerr.this.setVisible(false);
                    
            }
            public void dumm(int a)
            {
                w=a;
            }

          }
          listen1 df1=new listen1();
          df1.dumm(k);
          b[k].addActionListener(df1);
           jPanel1.add(b[k]);
           
           }
     /*temp1[k]=new JButton("Cancel");
  temp1[k].setEnabled(true);
   temp1[k].addActionListener(new java.awt.event.ActionListener() {
            @Override
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                buttonActionPerformed(evt);
            }

         private void buttonActionPerformed(ActionEvent evt) {
             throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
         }
     });
     row[k][2]=temp1[k];
     */
         
 }
   Dimension t=jTable1.getSize();
       Dimension p=jPanel1.getSize();
          opt.setSize(b[0].getSize().width,(b[0].getSize().height)*(3/4));
      jTable1.setRowHeight(b[0].getPreferredSize().height);
   jTable1.setSize(t.width,p.height);
     
       pack();
    //Adding columns
        for(Object c: col)
            this.addColumn(c);
 
    //Adding rows
        for(Object[] r: row)
            addRow(r);
 //jTable1.setEditingColumn(2);
    }
 
    @Override
 
    public Class getColumnClass(int columnIndex) {
        if(columnIndex == 1)return getValueAt(0, columnIndex).getClass();
       //  if(columnIndex == 0)return getValueAt(0, columnIndex).getClass();
        // if(columnIndex == 2)return getValueAt(0, columnIndex).getClass();
        else return super.getColumnClass(columnIndex);
    
          
 
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

        jButton1 = new javax.swing.JButton();
        jScrollPane3 = new javax.swing.JScrollPane();
        jPanel2 = new javax.swing.JPanel();
        jSplitPane1 = new javax.swing.JSplitPane();
        jScrollPane1 = new javax.swing.JScrollPane();
        jPanel1 = new javax.swing.JPanel();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTable1 = new javax.swing.JTable();

        setResizable(false);

        jButton1.setFont(new java.awt.Font("Calibri", 1, 18)); // NOI18N
        jButton1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/defaultpackage/refresh.png"))); // NOI18N
        jButton1.setText("Refresh");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jScrollPane1.setHorizontalScrollBarPolicy(javax.swing.ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        jScrollPane1.setVerticalScrollBarPolicy(javax.swing.ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER);

        jPanel1.setLayout(new java.awt.GridLayout(1, 0));
        jScrollPane1.setViewportView(jPanel1);

        jSplitPane1.setRightComponent(jScrollPane1);

        jScrollPane2.setVerticalScrollBarPolicy(javax.swing.ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER);
        jScrollPane2.setAutoscrolls(true);

        jTable1.setFont(new java.awt.Font("Droid Sans", 1, 10)); // NOI18N
        jTable1.setModel(new DefaultTableModel());
        jTable1.setEditingColumn(2);
        jTable1.setEnabled(false);
        jTable1.setFillsViewportHeight(true);
        jScrollPane2.setViewportView(jTable1);

        jSplitPane1.setLeftComponent(jScrollPane2);

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jSplitPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 664, Short.MAX_VALUE)
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jSplitPane1)
        );

        jScrollPane3.setViewportView(jPanel2);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 682, javax.swing.GroupLayout.PREFERRED_SIZE)
            .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, 682, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 43, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, 204, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
/*Thread logg=new Thread()
{*/
  //  public void run(){
        new Loggerr(mframe,mframe.abs,mframe.status.toArray()).setVisible(true); 
        
    //}
    
//};
//logg.start();   
this.setVisible(false);
// TODO add your handling code here:
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
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Loggerr.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Loggerr.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Loggerr.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Loggerr.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
           //     new Loggerr(Object[] a,Object[] ).setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JSplitPane jSplitPane1;
    private javax.swing.JTable jTable1;
    // End of variables declaration//GEN-END:variables
}
