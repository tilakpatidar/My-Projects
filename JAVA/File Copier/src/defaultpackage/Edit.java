/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package defaultpackage;

import java.awt.Component;
import java.awt.Dimension;
import java.awt.List;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.nio.file.Paths;
import java.util.ArrayList;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;

/**
 *
 * @author tilak
 */
public class Edit extends javax.swing.JFrame {
ArrayList sets,pwd;
JPanel panel[],popt[],jPanel2;
JLabel label[],ilabel[];
JButton b1[],b2[],b3[];
JScrollPane jScrollPane1;
 

JComboBox combo[];
MainFrame f;
   
      
      
    /**
     * Creates new form Edit
     */
    public Edit(ArrayList<List> s,ArrayList p,MainFrame frame) {
        Dimension dim=Toolkit.getDefaultToolkit().getScreenSize();
       int w=dim.width;
       int h=dim.height;
       Dimension d=new Dimension();
          d.setSize(w, h);
          jPanel2=new JPanel(); 
        jScrollPane1=new JScrollPane();
 

       this.setPreferredSize(d);
     
        //jPanel2.setSize(d);
      // this.setLocation((w-w/2)/2, (h-h/2)/2);
       this.setTitle("File Copier");
       this.setLayout(new java.awt.GridLayout(1, 0));
       int l=p.size();
        int n=(int)Math.sqrt(l);
         
         if(n<3)
         {
             n=3;
         }
    //System.out.println("n is "+n);
        jPanel2.setLayout(new java.awt.GridLayout(n+1, n));
      // jScrollPane1.setViewportView(jPanel2);

       // getContentPane().add(jScrollPane1);
         
       addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentHidden(java.awt.event.ComponentEvent evt) {
                formComponentHidden(evt);
            }
        });
        addWindowStateListener(new java.awt.event.WindowStateListener() {
            public void windowStateChanged(java.awt.event.WindowEvent evt) {
                formWindowStateChanged(evt);
            }
        });
        getContentPane().setLayout(new java.awt.GridLayout());
         
      
       
   //initComponents();
        
     
       f=frame;
      
      
        b1=new JButton[l];
        b2=new JButton[l];
        b3=new JButton[l];
      panel=new JPanel[l];
      popt=new JPanel[l];
        label=new JLabel [l];
     //   ilabel=new JLabel [l];
        combo=new JComboBox [l];
       
       
       int i=0;
       
       // jScrollPane1.add(jPanel2);
        
        
        while(i<l)
        {
            label[i]=new JLabel();
            
           // ilabel[i]=new JLabel();
            panel[i]=new JPanel();
            combo[i]=new JComboBox();
           
            b1[i]=new JButton();
             b2[i]=new JButton();
             b3[i]=new JButton();
            popt[i]=new JPanel();
            combo[i].setEditable(true);
        /*
            Dimension size=new Dimension();
            Dimension bsize=new Dimension();
            Dimension psize=new Dimension();
            size.setSize(w/2,h/200);
            psize.setSize(w/2,h/3);
            bsize.setSize(w/6, h/200);
            combo[i].setPreferredSize(size);
            label[i].setPreferredSize(size);
            popt[i].setPreferredSize(psize);
            jScrollPane1.setPreferredSize(psize);
            b1[i].setPreferredSize(bsize);
            b2[i].setPreferredSize(bsize);
            b3[i].setPreferredSize(bsize);
            */
            panel[i].setLayout(new java.awt.GridLayout(3,1));
            label[i].setIcon(new javax.swing.ImageIcon(getClass().getResource("/defaultpackage/icon.png")));
           // panel[i].add(ilabel[i]);
           panel[i].add(label[i]);
           panel[i].add(combo[i]);
           popt[i].setLayout(new java.awt.GridLayout(1,3));
           b1[i].setText("Add");
           b2[i].setText("Remove");
           b3[i].setText("Clear");
           popt[i].add(b1[i]);
           popt[i].add(b2[i]);
           popt[i].add(b3[i]);
           
           panel[i].add(popt[i]);
           jPanel2.add(panel[i]);
          class listen1 implements java.awt.event.ActionListener {
              int w;
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                
                 String input=JOptionPane.showInputDialog(Edit.this,"Enter new path :");
                   
                  
                   if(!input.equals(""))
                        combo[w].addItem(input);
                   
                    
            }
            public void dumm(int a)
            {
                w=a;
            }

          }
          listen1 df1=new listen1();
          df1.dumm(i);
                  
      
          b1[i].addActionListener(df1);
          class listen2 implements java.awt.event.ActionListener {
              int w;
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                
                 int index=combo[w].getSelectedIndex();
                   combo[w].removeItemAt(index);
                    
            }
            public void dumm(int a)
            {
                w=a;
            }

          }
          listen2 df2=new listen2();
          df2.dumm(i);
                  
      
          b2[i].addActionListener(df2);
           
 class listen3 implements java.awt.event.ActionListener {
              int w;
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                
                 combo[w].removeAllItems();
                    
            }
            public void dumm(int a)
            {
                w=a;
            }

          }
          listen3 df3=new listen3();
          df3.dumm(i);
                  
      
          b3[i].addActionListener(df3);
           
       
            
           //  jPanel2.add(label[i]);
           // jPanel2.add(combo[i]);
            label[i].setText(p.get(i).toString());
           String[] b=s.get(i).getItems();
           int len=b.length;
            
           int j=0;
           while(j<len)
           {
               
                combo[i].addItem(b[j]);  
               j++;
           }
           combo[i].setSelectedIndex(0);
           int count=combo[i].getItemCount();
            ArrayList<String> list = new ArrayList<String>();
            for(int g=0;g<count;g++)
                {
                if (!list.contains(combo[i].getItemAt(g).toString()))
                    {
                    list.add(combo[i].getItemAt(g).toString());
                    }
                }
           combo[i].removeAllItems();
           int q=list.size();
           for(int z=0;z<q;z++)
            combo[i].addItem(list.get(z));
            i++;
       } 
        
        
        this.add(jPanel2);
       pack();
        
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        setAlwaysOnTop(true);
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosed(java.awt.event.WindowEvent evt) {
                formWindowClosed(evt);
            }
        });
        addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentHidden(java.awt.event.ComponentEvent evt) {
                formComponentHidden(evt);
            }
        });
        addWindowStateListener(new java.awt.event.WindowStateListener() {
            public void windowStateChanged(java.awt.event.WindowEvent evt) {
                formWindowStateChanged(evt);
            }
        });
        getContentPane().setLayout(new java.awt.GridLayout(1, 0));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void formWindowClosed(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowClosed
//f.setVisible(true);  
// TODO add your handling code here:
    }//GEN-LAST:event_formWindowClosed

    private void formWindowStateChanged(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowStateChanged
//f.setEnabled(true);        // TODO add your handling code here:
    }//GEN-LAST:event_formWindowStateChanged

    private void formComponentHidden(java.awt.event.ComponentEvent evt) {//GEN-FIRST:event_formComponentHidden
 f.setEnabled(true);    
 f.edit.setVisible(false);// TODO add your handling code here:
    }//GEN-LAST:event_formComponentHidden

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
            java.util.logging.Logger.getLogger(Edit.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Edit.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Edit.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Edit.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Edit(null,null,null).setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    // End of variables declaration//GEN-END:variables
}
