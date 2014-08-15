/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package defaultpackage;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.List;
import java.awt.Point;
import java.awt.Toolkit;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.AccessDeniedException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import static java.nio.file.StandardCopyOption.REPLACE_EXISTING;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;



/**
 *
 * @author tilak
 */
public class MainFrame extends javax.swing.JFrame {
ArrayList<File> source=new ArrayList<File>();
ArrayList<File> dest=new ArrayList<File>();
ArrayList<List> sets=new ArrayList<List>();
ArrayList<String> pwd=new ArrayList<String>();
ArrayList<Integer> status=new ArrayList<Integer>();
ArrayList<String> dest_logger=new ArrayList<String>();
ArrayList<Integer> cancel=new ArrayList<Integer>();
Edit edit=null;
Thread t,pro;
jprogress show_progress=new jprogress();
int counter=0;
long totalsize=0;
long newsize=0;
String[] abs,rel;
       int ans_dest_full=-1;//default
      File d_space_check;
      File s_space_check;

int priority;

    /**
     * Creates new form NewJFrame
     */
    public MainFrame() {
          Dimension dim=Toolkit.getDefaultToolkit().getScreenSize();
       int w=dim.width;
       int h=dim.height;
      
       Dimension d=new Dimension();
       d.setSize(w/1.75, h/3);
       this.setPreferredSize(d);
       this.setLocation((w-w/2)/2, (h-h/2)/2);
       this.setTitle("File Copier");
        initComponents();
        jButton14.setVisible(false);
        hide_show_opt2(false);
        jPanel13.setVisible(false);
        jButton6.setEnabled(false);
        
    }
void files_copy(ArrayList<File> a,String cur)
{
    
    int j=0;
    int w=0;
    int flag=0;
    int q=pwd.size();
    
    while(j<q)
    {
        if(cur.equals(pwd.get(j)))     //code if two dir of smame pwd's are selected
        {
           w=1;
           flag=j;
           break;
        }
          j++;  
    }
    if(w==0)
    {
       pwd.add(cur); 
       source.addAll(a);
    List l=new List();
    jComboBox1.addItem(cur);
     
    for(File k:source)
    {
        
        String path;
        if(cur.equals(File.separator))
        path=k.toPath().toString();
        else if(cur.matches("^([a-zA-Z]):."))
             path=k.toPath().toString().replace(cur,File.separator);
       else
         path=k.toPath().toString().replace(cur,"");   
       
      // jComboBox1.addItem(k.toPath().toString());
        System.out.println(path);
        l.add(path);
        
        
    }
   
        sets.add(l);
        source.clear();
        
    }
    else if(w==1)
    {
        source.addAll(a);
        
        for(File k:source)
    {
        String path;
        if(cur.equals(File.separator))
        path=k.toPath().toString();
        else if(cur.matches("^([a-zA-Z]):."))
             path=k.toPath().toString().replace(cur,File.separator);
       else
         path=k.toPath().toString().replace(cur,"");   
       
        
       sets.get(flag).add(path);
        
        
    }
        
    }
   code_for_button14(false);
}
void files_dest(ArrayList<File> a)
{
    for(File k:a)
    {
        int flag=0;
            int count=jComboBox2.getItemCount();
            
            for(int g=0;g<count;g++)
            {
                if(jComboBox2.getItemAt(g).toString().equals(k.toPath().toString()))
                    flag=-1;
            }
        if(flag==0)
        {
            jComboBox2.addItem(k.toPath().toString());
        }
    }
    
}
void code_for_button14(boolean a)
{
     edit= new Edit(sets,pwd,this);
       edit.setVisible(a);   
        this.setEnabled(false);
}
void enable_show_while_copying(boolean a)
{
    jComboBox1.setEnabled(a);
    jComboBox2.setEnabled(a);
    jButton3.setEnabled(a);
    jButton4.setEnabled(a);
    jButton14.setEnabled(a);
    jButton.setEnabled(a);
    jButton2.setEnabled(a);
    radio_high.setEnabled(a);
    radio_med.setEnabled(a);
    radio_low.setEnabled(a);
}
void hide_show_opt2(boolean a)
{
jPanel17.setVisible(a);

opt2.setVisible(a);
jButton11.setVisible(a);
jButton12.setVisible(a);
jButton13.setVisible(a);
 }
int check_space(File f,File s)
{
    System.out.println("part free space"+f.getFreeSpace());
        System.out.println("file size "+s.length());
        
    if((f.getFreeSpace()>s.length())&&(f.getTotalSpace()!=0))
    {
        
        return 1;
    }
    
    else
    {
        return 0;
    }
  
}
class jprogress{
    
    void progress(int prog){
      jProgressBar2.setValue(prog);
      
    }
}

class progress implements Runnable
        {
    private File src,dest;
    progress(File s,File d)
    {
        this.src=s;
       this.dest=d;
    }
    
            public void run()
        {
            double bytes=src.length();
            
			double kilobytes = (bytes / 1024);
			double megabytes = (kilobytes / 1024);//in mbs
                        double osize=megabytes;
           
            
          double nsize = dest.length()/(1024*1024);
          double t1=0,t2=0;
            while(nsize!=osize){
                
                if(t2!=0){
                    if((t2-nsize)==0)
                        jLabel6.setText("Speed   "+"5"+" Mb/s");
                    else
                        jLabel6.setText("Speed   "+(t2-nsize)+" Mb/s");

                        
                }
                  
                
            nsize=dest.length()/(1024*1024);
            
            int prog=(int)((nsize/osize)*100);
         
          show_progress.progress(prog);
            
            
            
                try {
                  
                    Thread.sleep(1000);
                } catch (InterruptedException ex) {
                    Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                }
                t2=(dest.length()/(1024*1024));
            }
        }

        
        }

class Runcode_copy implements Runnable{
    public void run()
            {
                 enable_show_while_copying(false);
        int combos=edit.combo.length;//length of combos
        
        int length=jComboBox2.getItemCount()-1;
        File[] dest=new File[length];
        int y=0;
        while(y<length)
        {
            
            dest[y]=Paths.get(jComboBox2.getItemAt(y+1).toString()).toFile();
            y++;
        }
        
        int z=0,files=0;
        while(z<combos)
        {
            files=files+edit.combo[z].getItemCount();
            z++;
        }
       // System.out.println("Total no of files selected are :"+files);
        int main_count=0;
        main:
for(File d:dest)
{
  // System.out.println("Des path "+d.toPath().toString());
    for(int i=0;i<combos;i++){
       // System.out.println("combo no "+i);
        Path[] source;
       String pwd=edit.label[i].getText();     
      // System.out.println("pwd for combo no "+i+" "+pwd);//evaluates each combo
       int count=edit.combo[i].getItemCount();
      // System.out.println(" no of files in combo no "+i+" are"+count);
       int f=0;
       abs=new String[count];
       rel=new String[count];
       while(f<count)
       {
           abs[f]=pwd+edit.combo[i].getItemAt(f).toString();
           MainFrame.this.totalsize+=Paths.get(pwd+edit.combo[i].getItemAt(f)).toFile().length();
           System.out.println("Abs path "+abs[f]);
           rel[f]=edit.combo[i].getItemAt(f).toString();
           String temp=d.toPath().toString()+rel[f];
           dest_logger.add(temp);
          System.out.println("Rel path "+rel[f]);
           f++;
       }
      // System.out.println("Total size "+MainFrame.this.totalsize);
       

        
       source=new Path[count];
       for(int w=0;w<count;w++)
       {
           cancel.add(w,0);
            source[w]=Paths.get(abs[w]);
       }
       int u=0;
       file:
       while(u<count)
       {
           if((!Paths.get(d.toPath().toString()+rel[u]).toFile().exists())&&(cancel.get(u)==0)){
            int check=check_space(d,Paths.get(abs[u]).toFile());
            
            if(check==1){}
            else if(check==0)
            {
                d_space_check=d;
                s_space_check=Paths.get(abs[u]).toFile();
                Thread full=new Thread()
                {
                    public void run()
                    {
                       Dest_full temp=new Dest_full(d_space_check,s_space_check);
                       temp.setVisible(true);
                       while(ans_dest_full<0)
                       {
                           ans_dest_full=temp.ans;
                           if(ans_dest_full>0)
                               break;
                          
                          
                           try {
                               Thread.sleep(100);
                           } catch (InterruptedException ex) {
                               Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                           }
                       }
                       
                    }
                       
                      
                       
                        };
                    
               
                full.setPriority(priority);
                full.start();
                try {
                    full.join();
                } catch (InterruptedException ex) {
                    Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                }
                       if(ans_dest_full==0) //0 means retry
                       {
                           
                            ans_dest_full=-1;
                       }
                       else if(ans_dest_full==1)  //1 means skip this file
                       {
                           MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                           double a=(MainFrame.this.newsize)*(1024*1024);
            double b=(MainFrame.this.totalsize)*(1024*1024);
            int prog=(int)((a/b)*100);
            jLabel2.setText("Completed "+prog+"%");
             ans_dest_full=-1;
             status.add(u,2);
           jProgressBar1.setValue(prog);
           u++;
                              continue file; 
                       }
                       else if(ans_dest_full==2)  //2 means skip all
                       {
                           jLabel2.setText("Completed "+"100"+"%");
                           jProgressBar1.setValue(100);
                            jProgressBar2.setValue(100);
                             ans_dest_full=-1;
                             for(int k=u;k<count;k++)
                             status.add(k,2);
                           main_count++;
                           break main;
                       }
                
                
            }
            
               
               try {
                 
                   jLabel1.setText("Copying "+(u+1)+" of "+files);
                   jLabel5.setText(Paths.get(abs[u]).getFileName().toString());
                   progress obj=new progress(Paths.get(abs[u]).toFile(),Paths.get(d.toPath().toString()+rel[u]).toFile());
                   pro=new Thread(obj);
                    pro.start();
                    MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                   Files.copy(Paths.get(abs[u]),Paths.get(d.toPath().toString()+rel[u]));
                   status.add(u,1);
                   jProgressBar2.setValue(100);
                   pro.setPriority(priority);
                   pro.stop();
                     
               }
               catch (AccessDeniedException ex) {
                   if(Paths.get(abs[u]).toFile().canRead())
                   {
                       if(!Paths.get(d.toPath().toString()+rel[u]).toFile().canWrite())
                       {
                           JOptionPane.showMessageDialog(MainFrame.this,"Access Denied on "+d.toPath().toString()+rel[u]+" !");
                       }
                   }
                       else
                       {
                        JOptionPane.showMessageDialog(MainFrame.this,"Access Denied on "+abs[u]+" !");
                       }
            
                   status.add(u,9);
               }
                catch (IOException ex) {
                   Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                   status.add(u,0);
               }
           }
           else if(cancel.get(u)==0)
           {
               
               int check=check_space(d,Paths.get(abs[u]).toFile());
             int check1;
               check1 = check_space(d,Paths.get(abs[u]).toFile());
            if(check1==1){}
            else if(check1==0)
            {
                d_space_check=d;
                s_space_check=Paths.get(abs[u]).toFile();
                Thread full=new Thread()
                {
                    public void run()
                    {
                       Dest_full temp=new Dest_full(d_space_check,s_space_check);
                       temp.setVisible(true);
                       while(ans_dest_full<0)
                       {
                           ans_dest_full=temp.ans;
                           if(ans_dest_full>0)
                               break;
                          
                          
                           try {
                               Thread.sleep(100);
                           } catch (InterruptedException ex) {
                               Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                           }
                       }
                       
                    }
                       
                      
                       
                        };
                    
               full.setPriority(priority);
                
                full.start();
                try {
                    full.join();
                } catch (InterruptedException ex) {
                    Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                }
                       if(ans_dest_full==0) //0 means retry
                       {
                           ans_dest_full=-1;
                       }
                       else if(ans_dest_full==1)  //1 means skip this file
                       {
                           MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                           double a=(MainFrame.this.newsize)*(1024*1024);
            double b=(MainFrame.this.totalsize)*(1024*1024);
            int prog=(int)((a/b)*100);
            jLabel2.setText("Completed "+prog+"%");
             ans_dest_full=-1;
           jProgressBar1.setValue(prog);
           u++;
                              continue file; 
                       }
                       else if(ans_dest_full==2)  //2 means skip all
                       {
                           jLabel2.setText("Completed "+"100"+"%");
                           jProgressBar1.setValue(100);
                            jProgressBar2.setValue(100);
                             ans_dest_full=-1;
                           main_count++;
                           break main;
                       }
                
               
            }
               
               
           jLabel1.setText("File Operations "+(u+1)+" of "+files);
              
                int a=JOptionPane.showConfirmDialog(MainFrame.this,"File "+Paths.get(abs[u]).getFileName()+" already exists.\n In destination "+d.toPath().toString()+rel[u]+"\n Do you want to replace ?");
                         if(a==JOptionPane.YES_OPTION||a==5) //yes//a=5 if yes to all//a=-5 no to all
                            {
                         try { 
                             
                             jLabel5.setText(Paths.get(abs[u]).getFileName().toString());
                             
                            progress obj=new progress(Paths.get(abs[u]).toFile(),Paths.get(d.toPath().toString()+rel[u]).toFile());
                    pro=new Thread(obj);
                    pro.setPriority(priority);
                    pro.start();
                             MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                        Files.copy(Paths.get(abs[u]),Paths.get(d.toPath().toString()+rel[u]),REPLACE_EXISTING);
                        status.add(u,1);
                         jProgressBar2.setValue(100);
                     pro.stop();
                        
                          
                        
                        
                     } catch (IOException ex) {
                         Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                         status.add(u,0);
                     } 
               
               
           } 
          
            
           
           } 
           u++;
           double a=(MainFrame.this.newsize)*(1024*1024);
            double b=(MainFrame.this.totalsize)*(1024*1024);
            int prog=(int)((a/b)*100);
            jLabel2.setText("Completed "+prog+"%");
           jProgressBar1.setValue(prog);
          // JOptionPane.showMessageDialog(MainFrame.this,"Number of Operations "+(main_count+1)+"\n Performed Successfully !");
       }
      
     
    }
    jLabel2.setText("Completed "+100+"%");
    jProgressBar1.setValue(100);
    jProgressBar2.setValue(0);
    main_count++;
}
jProgressBar1.setValue(100);
enable_show_while_copying(true);
jLabel6.setText("Speed     0 Mbps");
       
            }
}
class runcode_move implements Runnable{
    public void run()
            {
                ArrayList<File> delete_them=new ArrayList<File>();
                 enable_show_while_copying(false);
        int combos=edit.combo.length;//length of combos
        
        int length=jComboBox2.getItemCount()-1;
        File[] dest=new File[length];
        int y=0;
        while(y<length)
        {
            
            dest[y]=Paths.get(jComboBox2.getItemAt(y+1).toString()).toFile();
            y++;
        }
        
        int z=0,files=0;
        while(z<combos)
        {
            files=files+edit.combo[z].getItemCount();
            z++;
        }
       // System.out.println("Total no of files selected are :"+files);
for(File d:dest)
{
   System.out.println("Des path "+d.toPath().toString());
    for(int i=0;i<combos;i++){
       // System.out.println("combo no "+i);
        Path[] source;
       String pwd=edit.label[i].getText();     
       //System.out.println("pwd for combo no "+i+" "+pwd);//evaluates each combo
       int count=edit.combo[i].getItemCount();
       //System.out.println(" no of files in combo no "+i+" are"+count);
       int f=0;
       abs=new String[count];
       rel=new String[count];
       while(f<count)
       {
           abs[f]=pwd+edit.combo[i].getItemAt(f).toString();
           MainFrame.this.totalsize+=Paths.get(pwd+edit.combo[i].getItemAt(f)).toFile().length();
          // System.out.println("Abs path "+abs[f]);
           rel[f]=edit.combo[i].getItemAt(f).toString();
          // System.out.println("Rel path "+rel[f]);
           f++;
       }
       //System.out.println("Total size "+MainFrame.this.totalsize);
       

        
       source=new Path[count];
       for(int w=0;w<count;w++)
       {
            source[w]=Paths.get(abs[w]);
       }
       int u=0;
       while(u<count)
       {
           if(!Paths.get(d.toPath().toString()+rel[u]).toFile().exists()){
            
               try {
                 
                   jLabel1.setText("Moving "+(u+1)+" of "+files);
                   jLabel5.setText(Paths.get(abs[u]).getFileName().toString());
                   progress obj=new progress(Paths.get(abs[u]).toFile(),Paths.get(d.toPath().toString()+rel[u]).toFile());
                   pro=new Thread(obj);
                    pro.start();
                    MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                   Files.copy(Paths.get(abs[u]),Paths.get(d.toPath().toString()+rel[u]));
                   delete_them.add(Paths.get(abs[u]).toFile());
                   if(Paths.get(d.toPath().toString()+rel[u]).toFile().exists())
                   Files.delete(Paths.get(abs[u]));
                   jProgressBar2.setValue(100);
                   pro.stop();
                     
               } catch (IOException ex) {
                   Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
               }
           }
           else
           {
           jLabel1.setText("Moving "+(u+1)+" of "+files);
              
                int a=JOptionPane.showConfirmDialog(MainFrame.this,"File "+Paths.get(abs[u]).getFileName()+" already exists.\n In destination "+d.toPath().toString()+rel[u]+"\n Do you want to replace ?");
                         if(a==JOptionPane.YES_OPTION||a==5) //yes//a=5 if yes to all//a=-5 no to all
                            {
                         try { 
                             
                             jLabel5.setText(Paths.get(abs[u]).getFileName().toString());
                             
                            progress obj=new progress(Paths.get(abs[u]).toFile(),Paths.get(d.toPath().toString()+rel[u]).toFile());
                    pro=new Thread(obj);
                    pro.start();
                             MainFrame.this.newsize+=Paths.get(abs[u]).toFile().length();
                        Files.copy(Paths.get(abs[u]),Paths.get(d.toPath().toString()+rel[u]),REPLACE_EXISTING);
                        delete_them.add(Paths.get(abs[u]).toFile());
                          if(Paths.get(d.toPath().toString()+rel[u]).toFile().exists())
                   Files.delete(Paths.get(abs[u]));
                         jProgressBar2.setValue(100);
                   pro.stop();
                       
                          
                        
                        
                     } catch (IOException ex) {
                         Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
                     } 
               
               
           } 
          
            
           
           } 
           u++;
           double a=(MainFrame.this.newsize)*(1024*1024);
            double b=(MainFrame.this.totalsize)*(1024*1024);
            int prog=(int)((a/b)*100);
            jLabel2.setText("Completed "+prog+"%");
           jProgressBar1.setValue(prog);
       }
      
     
    }
}
int len=delete_them.size();
for(int p=0;p<len;p++)
{
    if(delete_them.get(p).exists())
    {
        try {
            Files.delete(delete_them.get(p).toPath());
        } catch (IOException ex) {
            Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
        }
        
}
    else{
        delete_them.get(p).delete();
    }
}
delete_them.clear();
jProgressBar1.setValue(100);
enable_show_while_copying(true);
jLabel6.setText("Speed     0 Mbps");
       
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

        buttonGroup1 = new javax.swing.ButtonGroup();
        jPanel2 = new javax.swing.JPanel();
        jPanel6 = new javax.swing.JPanel();
        jComboBox1 = new javax.swing.JComboBox();
        jComboBox2 = new javax.swing.JComboBox();
        jPanel5 = new javax.swing.JPanel();
        jPanel15 = new javax.swing.JPanel();
        jPanel16 = new javax.swing.JPanel();
        opt1 = new javax.swing.JPanel();
        jButton14 = new javax.swing.JButton();
        jPanel17 = new javax.swing.JPanel();
        opt2 = new javax.swing.JPanel();
        jButton11 = new javax.swing.JButton();
        jButton12 = new javax.swing.JButton();
        jButton13 = new javax.swing.JButton();
        jPanel14 = new javax.swing.JPanel();
        jButton = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jPanel1 = new javax.swing.JPanel();
        jPanel4 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jPanel3 = new javax.swing.JPanel();
        jProgressBar2 = new javax.swing.JProgressBar();
        jLabel3 = new javax.swing.JLabel();
        jProgressBar1 = new javax.swing.JProgressBar();
        jPanel7 = new javax.swing.JPanel();
        jPanel8 = new javax.swing.JPanel();
        jPanel19 = new javax.swing.JPanel();
        jPanel18 = new javax.swing.JPanel();
        jLabel4 = new javax.swing.JLabel();
        radio_high = new javax.swing.JRadioButton();
        radio_med = new javax.swing.JRadioButton();
        radio_low = new javax.swing.JRadioButton();
        jPanel20 = new javax.swing.JPanel();
        jButton3 = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        jPanel9 = new javax.swing.JPanel();
        jPanel10 = new javax.swing.JPanel();
        jPanel21 = new javax.swing.JPanel();
        jPanel22 = new javax.swing.JPanel();
        jButton6 = new javax.swing.JButton();
        jPanel11 = new javax.swing.JPanel();
        jPanel13 = new javax.swing.JPanel();
        jLabel6 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new java.awt.GridLayout(3, 0, 0, 15));

        jPanel2.setLayout(new java.awt.GridLayout(1, 2, 20, 0));

        jPanel6.setLayout(new java.awt.GridLayout(2, 1, 0, 10));

        jComboBox1.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        jComboBox1.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "Directories from which files are selected" }));
        jComboBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox1ActionPerformed(evt);
            }
        });
        jPanel6.add(jComboBox1);

        jComboBox2.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        jComboBox2.setModel(new javax.swing.DefaultComboBoxModel(new String[] { "Destination Directories" }));
        jComboBox2.setToolTipText("");
        jComboBox2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox2ActionPerformed(evt);
            }
        });
        jPanel6.add(jComboBox2);

        jPanel2.add(jPanel6);

        jPanel5.setLayout(new java.awt.GridLayout(1, 2, 30, 10));

        jPanel15.setLayout(new java.awt.GridLayout(2, 0, 0, 10));

        jPanel16.setLayout(new java.awt.GridLayout(1, 0, 20, 50));

        opt1.setLayout(new java.awt.GridLayout(1, 0, 15, 30));

        jButton14.setFont(new java.awt.Font("Calibri", 0, 12)); // NOI18N
        jButton14.setText("Advanced Edit");
        jButton14.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton14ActionPerformed(evt);
            }
        });
        opt1.add(jButton14);

        jPanel16.add(opt1);

        jPanel15.add(jPanel16);

        jPanel17.setLayout(new java.awt.GridLayout(1, 0));

        opt2.setLayout(new java.awt.GridLayout(1, 0, 2, 30));

        jButton11.setFont(new java.awt.Font("Calibri", 0, 10)); // NOI18N
        jButton11.setText("Remove");
        jButton11.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton11ActionPerformed(evt);
            }
        });
        opt2.add(jButton11);

        jButton12.setFont(new java.awt.Font("Calibri", 0, 10)); // NOI18N
        jButton12.setText("Edit");
        jButton12.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton12ActionPerformed(evt);
            }
        });
        opt2.add(jButton12);

        jButton13.setFont(new java.awt.Font("Calibri", 0, 10)); // NOI18N
        jButton13.setText("Clear All");
        jButton13.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton13ActionPerformed(evt);
            }
        });
        opt2.add(jButton13);

        jPanel17.add(opt2);

        jPanel15.add(jPanel17);

        jPanel5.add(jPanel15);

        jPanel14.setLayout(new java.awt.GridLayout(2, 0, 10, 10));

        jButton.setFont(new java.awt.Font("Calibri", 1, 14)); // NOI18N
        jButton.setText("Source File");
        jButton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonActionPerformed(evt);
            }
        });
        jPanel14.add(jButton);

        jButton2.setFont(new java.awt.Font("Calibri", 1, 14)); // NOI18N
        jButton2.setText("Destination");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        jPanel14.add(jButton2);

        jPanel5.add(jPanel14);

        jPanel2.add(jPanel5);

        getContentPane().add(jPanel2);

        jPanel1.setLayout(new java.awt.GridLayout(1, 2, 0, 20));

        jPanel4.setLayout(new java.awt.GridLayout(2, 1));

        jLabel1.setFont(new java.awt.Font("Calibri", 0, 18)); // NOI18N
        jLabel1.setText("Copying  of");
        jPanel4.add(jLabel1);

        jLabel5.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        jLabel5.setHorizontalAlignment(javax.swing.SwingConstants.LEFT);
        jPanel4.add(jLabel5);

        jLabel2.setFont(new java.awt.Font("Calibri", 0, 18)); // NOI18N
        jLabel2.setText("Completed <>%");
        jPanel4.add(jLabel2);
        jPanel4.add(jLabel7);

        jPanel1.add(jPanel4);

        jPanel3.setLayout(new java.awt.GridLayout(3, 1));
        jPanel3.add(jProgressBar2);
        jPanel3.add(jLabel3);
        jPanel3.add(jProgressBar1);

        jPanel1.add(jPanel3);

        getContentPane().add(jPanel1);

        jPanel7.setLayout(new java.awt.GridLayout(1, 0, 10, 0));

        jPanel8.setLayout(new java.awt.GridLayout(2, 0, 20, 5));

        jPanel19.setLayout(new java.awt.GridLayout(1, 0));

        jPanel18.setLayout(new java.awt.GridLayout(1, 0));

        jLabel4.setFont(new java.awt.Font("Calibri", 0, 18)); // NOI18N
        jLabel4.setText("Priority");
        jPanel18.add(jLabel4);

        buttonGroup1.add(radio_high);
        radio_high.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        radio_high.setText("High");
        radio_high.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                radio_highActionPerformed(evt);
            }
        });
        jPanel18.add(radio_high);

        buttonGroup1.add(radio_med);
        radio_med.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        radio_med.setSelected(true);
        radio_med.setText("Medium");
        jPanel18.add(radio_med);

        buttonGroup1.add(radio_low);
        radio_low.setFont(new java.awt.Font("Calibri", 0, 14)); // NOI18N
        radio_low.setText("Low");
        radio_low.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                radio_lowActionPerformed(evt);
            }
        });
        jPanel18.add(radio_low);

        jPanel19.add(jPanel18);

        jPanel8.add(jPanel19);

        jPanel20.setLayout(new java.awt.GridLayout(1, 0));

        jButton3.setFont(new java.awt.Font("Calibri", 1, 18)); // NOI18N
        jButton3.setText("Move");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });
        jPanel20.add(jButton3);

        jButton4.setFont(new java.awt.Font("Calibri", 1, 18)); // NOI18N
        jButton4.setText("Copy");
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });
        jPanel20.add(jButton4);

        jPanel8.add(jPanel20);

        jPanel7.add(jPanel8);

        jPanel9.setLayout(new java.awt.GridLayout(1, 0, 20, 0));

        jPanel10.setLayout(new java.awt.GridLayout(2, 0));

        javax.swing.GroupLayout jPanel21Layout = new javax.swing.GroupLayout(jPanel21);
        jPanel21.setLayout(jPanel21Layout);
        jPanel21Layout.setHorizontalGroup(
            jPanel21Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 662, Short.MAX_VALUE)
        );
        jPanel21Layout.setVerticalGroup(
            jPanel21Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 65, Short.MAX_VALUE)
        );

        jPanel10.add(jPanel21);

        jPanel22.setLayout(new java.awt.GridLayout(1, 0));

        jButton6.setFont(new java.awt.Font("Calibri", 1, 18)); // NOI18N
        jButton6.setText("Logger");
        jButton6.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton6ActionPerformed(evt);
            }
        });
        jPanel22.add(jButton6);

        jPanel10.add(jPanel22);

        jPanel9.add(jPanel10);

        jPanel11.setLayout(new java.awt.GridLayout());

        jPanel13.setLayout(new java.awt.GridLayout(1, 0, 10, 0));

        jLabel6.setFont(new java.awt.Font("Dialog", 1, 14)); // NOI18N
        jLabel6.setText("Speed     0 Mbps");
        jPanel13.add(jLabel6);

        jPanel11.add(jPanel13);

        jPanel9.add(jPanel11);

        jPanel7.add(jPanel9);

        getContentPane().add(jPanel7);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButtonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButtonActionPerformed
this.setEnabled(false);
        new FileChooser_for_source(this).setVisible(true);  
       // TODO add your handling code here:
    }//GEN-LAST:event_jButtonActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
this.setEnabled(false);
        new FileChooser_for_dest(this).setVisible(true);   
      // TODO add your handling code here:
    }//GEN-LAST:event_jButton2ActionPerformed

    private void jComboBox1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox1ActionPerformed
jButton14.setVisible(true);
        

// TODO add your handling code here:
    }//GEN-LAST:event_jComboBox1ActionPerformed

    private void jButton14ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton14ActionPerformed
code_for_button14(true);
      
    
   
    }//GEN-LAST:event_jButton14ActionPerformed

    private void jButton11ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton11ActionPerformed
int index=jComboBox2.getSelectedIndex();
        
        if(index!=0)
        {
            jComboBox2.removeItemAt(index);
        }// TODO add your handling code here:
    }//GEN-LAST:event_jButton11ActionPerformed

    private void jButton12ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton12ActionPerformed

 int index=jComboBox2.getSelectedIndex();
 if(index==0)
 {
   JOptionPane.showMessageDialog(this," ' "+jComboBox2.getItemAt(index).toString()+" 'Cannot be edited !");  
 }
 else
 {
    String input= JOptionPane.showInputDialog("Enter new destination path :");
    
    if(!input.equals(""))
    {
        jComboBox2.setSelectedIndex(0);
    jComboBox2.addItem(input);
      jComboBox2.removeItemAt(index); 
    }
 }



// TODO add your handling code here:
    }//GEN-LAST:event_jButton12ActionPerformed

    private void jComboBox2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox2ActionPerformed
hide_show_opt2(true);        // TODO add your handling code here:
    }//GEN-LAST:event_jComboBox2ActionPerformed

    private void jButton13ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton13ActionPerformed
jComboBox2.removeAllItems();

jComboBox2.addItem("Destination Directories");// TODO add your handling code here:
    }//GEN-LAST:event_jButton13ActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
if(jComboBox1.getItemCount()>1&&jComboBox2.getItemCount()>1)
{
    
    if(radio_high.isSelected())
    {
        priority=10;
    }
    else if(radio_med.isSelected())
    {
        priority=7;
    }
    else if(radio_low.isSelected())
    {
        priority=5;
    }
           
    
        jProgressBar1.setValue(0);
jProgressBar2.setValue(0);
        Runcode_copy code=new Runcode_copy();
        jPanel13.setVisible(true);
        jButton6.setEnabled(true);
        
        t=new Thread(code);
t.setPriority(priority);

        t.start();
}
else{
    if(jComboBox1.getItemCount()<=1)
    {
        JOptionPane.showMessageDialog(this,"Please select atleast one file for copying !");
    }
     if(jComboBox2.getItemCount()<=1)
    {
        JOptionPane.showMessageDialog(this,"Please select atleast one destination for copying !");
    }
}

        // TODO add your handling code here:
    }//GEN-LAST:event_jButton4ActionPerformed

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
if(jComboBox1.getItemCount()>1&&jComboBox2.getItemCount()>1)
{
     if(radio_high.isSelected())
    {
        priority=10;
    }
    else if(radio_med.isSelected())
    {
        priority=7;
    }
    else if(radio_low.isSelected())
    {
        priority=5;
    }
        jProgressBar1.setValue(0);
jProgressBar2.setValue(0);
        runcode_move code=new runcode_move();
        jButton6.setEnabled(true);
        jPanel13.setVisible(true);
        t=new Thread(code);
t.setPriority(priority);
        t.start();
}
else{
    if(jComboBox1.getItemCount()<=1)
    {
        JOptionPane.showMessageDialog(this,"Please select atleast one file for moving !");
    }
     if(jComboBox2.getItemCount()<=1)
    {
        JOptionPane.showMessageDialog(this,"Please select atleast one destination for moving !");
    }
}
        // TODO add your handling code here:
    }//GEN-LAST:event_jButton3ActionPerformed

    private void jButton6ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton6ActionPerformed
/*Thread logg=new Thread()
{
    public void run(){*/
        new Loggerr(MainFrame.this,MainFrame.this.abs,MainFrame.this.status.toArray()).setVisible(true); 
        
    /*}
};
logg.start();*/
               // TODO add your handling code here:
    }//GEN-LAST:event_jButton6ActionPerformed

    private void radio_lowActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_radio_lowActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_radio_lowActionPerformed

    private void radio_highActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_radio_highActionPerformed
JOptionPane.showMessageDialog(this,"High Priority enables maximum speed \n but may reduce speed of other running apps !");        // TODO add your handling code here:
    }//GEN-LAST:event_radio_highActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswinig/lookandfeel/plaf.html 
         */
        String OS = System.getProperty("os.name").toLowerCase();

     if(OS.equalsIgnoreCase("windows"))
       {
         try {
             UIManager.setLookAndFeel("Windows");
         } catch (ClassNotFoundException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (InstantiationException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (IllegalAccessException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (UnsupportedLookAndFeelException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         }
       
            
         
       }
       else if(OS.equals("linux"))
       {
         try {      
             UIManager.setLookAndFeel(javax.swing.UIManager.getSystemLookAndFeelClassName());
         } catch (ClassNotFoundException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (InstantiationException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (IllegalAccessException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (UnsupportedLookAndFeelException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         }
                      
          
          
             }
    
    else
       {
         try {      
             UIManager.setLookAndFeel(javax.swing.UIManager.getSystemLookAndFeelClassName());
         } catch (ClassNotFoundException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (InstantiationException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (IllegalAccessException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         } catch (UnsupportedLookAndFeelException ex) {
             Logger.getLogger(MainFrame.class.getName()).log(Level.SEVERE, null, ex);
         }
       }
         
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainFrame().setVisible(true);
            }
        });
    
    }
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.ButtonGroup buttonGroup1;
    private javax.swing.JButton jButton;
    private javax.swing.JButton jButton11;
    private javax.swing.JButton jButton12;
    private javax.swing.JButton jButton13;
    private javax.swing.JButton jButton14;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JButton jButton6;
    private javax.swing.JComboBox jComboBox1;
    private javax.swing.JComboBox jComboBox2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel10;
    private javax.swing.JPanel jPanel11;
    private javax.swing.JPanel jPanel13;
    private javax.swing.JPanel jPanel14;
    private javax.swing.JPanel jPanel15;
    private javax.swing.JPanel jPanel16;
    private javax.swing.JPanel jPanel17;
    private javax.swing.JPanel jPanel18;
    private javax.swing.JPanel jPanel19;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel20;
    private javax.swing.JPanel jPanel21;
    private javax.swing.JPanel jPanel22;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JPanel jPanel6;
    private javax.swing.JPanel jPanel7;
    private javax.swing.JPanel jPanel8;
    private javax.swing.JPanel jPanel9;
    private javax.swing.JProgressBar jProgressBar1;
    private javax.swing.JProgressBar jProgressBar2;
    private javax.swing.JPanel opt1;
    private javax.swing.JPanel opt2;
    private javax.swing.JRadioButton radio_high;
    private javax.swing.JRadioButton radio_low;
    private javax.swing.JRadioButton radio_med;
    // End of variables declaration//GEN-END:variables
}
