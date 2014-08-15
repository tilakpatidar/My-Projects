
COPY PASTE  THE FOLLOWING IN YOUR MYSQL TERMINAL
************************************************************************************************************
create database library;
use library;
 create table book
     (book_code varchar(20) PRIMARY KEY,
     isbn int(25),
     book_name varchar(25),
     author_name varchar(25),
     publisher_name varchar(25),
     edition int(4),
     price int(5),
     quantity int(3));
create table password
    (password varchar(50) NOT NULL);
INSERT INTO password VALUES('tilak');
ALTER TABLE BOOK
     ADD COLUMN issue varchar(5) DEFAULT 'NO';
ALTER TABLE BOOK
     ADD COLUMN issued_to int(10) DEFAULT NULL;
ALTER TABLE BOOK
     ADD COLUMN issued_date date DEFAULT NULL;

    alter table book
    add column category  varchar(50) NOT NULL;
insert into BOOK (book_code,isbn,book_name,author_name,publisher_name,edition,price,quantity,category)
     values('456891','45689','MATLAB','Harrison','Pearson','2011','526','1','General Reference');

insert into book (book_code,isbn,book_name,author_name,publisher_name,edition,price,quantity,category)
    values('466891','46689','MATLAB','Tarrison','Dearson','2051','526','1','General Reference');
CREATE TABLE MEMBER
    (id int(5) PRIMARY KEY AUTO_INCREMENT,
    name varchar(25),
    dob date,
    sex varchar(10),
    age int(2),
    address varchar(70),
    contact_no int(10),
    image text);
ALTER TABLE MEMBER
    ADD COLUMN BOOK1 int(10) DEFAULT 0;
ALTER TABLE MEMBER
    ADD COLUMN issue_status int(1)  DEFAULT '0';
