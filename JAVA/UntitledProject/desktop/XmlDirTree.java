/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package desktop;

import java.io.File;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

/**
 *
 * @author tilak
 */
public class XmlDirTree {
    private File path;
    XmlDirTree(){
        
    }
    XmlDirTree(String path){
        this.path=new File(path);
    }
    public String getPath(){
        return this.path.toString();
    }
    public void setPath(String s){
        this.path=new File(s);
    }
    public String xmlTree(){
        File node=new File(this.getPath());
        //Traverses to depth two
        HashMap<String,HashSet> map=new HashMap<>();
		if(node.isDirectory()){
                    HashSet<String> set=new HashSet<>();
                        if(!map.containsKey(node.toString())){
                            String[] subNote = node.list();
                            set.addAll(Arrays.asList(subNote));
                            map.put(node.toString(),set);
                        }
                }
                Iterator i=map.keySet().iterator();
                while(i.hasNext()){
                    File temp=new File(i.next().toString());
                    if(temp.isDirectory()){
                        HashSet<String> set=new HashSet<>();
                        if(!map.containsKey(temp.toString())){
                            String[] subNote = node.list();
                          
                            set.addAll(Arrays.asList(subNote));
                            map.put(temp.toString(),set);
                        }
                    }
                }
                Iterator<String> j=map.keySet().iterator();
                String xml="<root id=\""+node.toString()+"\">";
                while(j.hasNext()){
                    String key=j.next();
                    xml+="<one id=\""+key+"\">";
                    Iterator<String> k=map.get(key).iterator();
                    while(k.hasNext()){
                        xml+="<two id=\""+k.next()+"\"></two>";
                    }
                    xml+="</one>";
                }
                xml+="</root>";
                return xml;
    }
    public static void main(String[] args){
        XmlDirTree xml=new XmlDirTree(System.getProperty("user.home"));
        System.out.println(xml.xmlTree());
    }
}
