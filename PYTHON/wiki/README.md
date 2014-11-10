# Wikipedia Parsing Scripts

Folder **parseWikiXMLDump** contains python scripts to parse the wiki xml dump which can be downloaded from https://dumps.wikimedia.org/enwiki/.
It has the following files:
It has the following files:

    -parse.py :just a module to parse articles from dump
    -split.py to split the big 49 GB XML dump into small chunks
    
Folder **getWikiInfoBox** contains python scripts to get the infobox from the extracted data from xml dump.

It has the following files:

    -temp.py :just a module to parse infobox from the wiki body
    -infobox.py:main module to get the infobox and store in mysql
    
Folder **getRedirects** contains python scripts to get the number for redirects for each article which can be used to rank wiki pages having similar titles.
It has the following files:

    -redirect.py :just a module to scrap redirects from article info page
    
It has the following files:

    -temp.py :just a module to parse infobox from the wiki body
    -infobox.py:main module to get the infobox and store in mysql

### Version
1.0.1


### Instructions

First split the wiki dump into small chunks of say 50000 lines by using the split.py
Put all the splitted files in the same dir as parse.py also create a new folder done in which all the files which are processed are moved.

### Author
Tilak Patidar

**Free Software, Hell Yeah!**
