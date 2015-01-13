-- phpMyAdmin SQL Dump
-- version 3.4.3.1
-- http://www.phpmyadmin.net
--
-- Host: fdb13.runhosting.com
-- Generation Time: Dec 25, 2014 at 11:52 AM
-- Server version: 5.5.38
-- PHP Version: 5.3.27

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1780205_seekho`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth`
--

CREATE TABLE IF NOT EXISTS `auth` (
  `username` varchar(40) NOT NULL,
  `pswd` varchar(40) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='auth table';

--
-- Dumping data for table `auth`
--

INSERT INTO `auth` (`username`, `pswd`) VALUES
('tilak', 'c875b35t3bt541818d5f2d3f651171dc'),
('tilakpatidar', 't1t2725b8d51t57e1f3b71551b5ec6b1'),
('nidhiii', '6278e56tff755f485d157fe857d2ft6e'),
('tilakk', 't1t2725b8d51t57e1f3b71551b5ec6b1'),
('sagar', 'd4165eb17b51d3t76ccct52f18768146'),
('idealbhopal', 'f863fc4d1254d4t4d877eteddf51fef7');

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE IF NOT EXISTS `comment` (
  `comment_id` int(9) NOT NULL AUTO_INCREMENT,
  `comment_user` varchar(40) NOT NULL,
  `comment_desc` longtext NOT NULL,
  `comment_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `comment_course` int(11) NOT NULL,
  `comment_like` bigint(9) NOT NULL,
  `comment_liked` longtext NOT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`comment_id`, `comment_user`, `comment_desc`, `comment_time`, `comment_course`, `comment_like`, `comment_liked`) VALUES
(1, 'tilakpatidar', 'Great tutorial !', '2014-12-25 11:30:47', 13, 1, '[''tilakpatidar'']'),
(2, 'tilakpatidar', 'Great tutorial !', '2014-12-25 11:44:49', 1, 1, '[''tilakpatidar'']'),
(3, 'tilakpatidar', 'Great tutorial !', '2014-12-24 14:03:42', 2, 0, ''),
(4, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:04:51', 3, 0, ''),
(5, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:05:14', 4, 0, ''),
(6, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:05:26', 5, 0, ''),
(7, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:06:45', 5, 0, ''),
(8, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:07:01', 7, 0, ''),
(9, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:07:10', 8, 0, ''),
(10, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:07:29', 9, 0, ''),
(11, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:07:44', 10, 0, ''),
(12, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:08:50', 11, 0, ''),
(13, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:09:02', 12, 0, ''),
(14, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:09:45', 14, 0, ''),
(15, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:12:49', 15, 0, ''),
(16, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:13:08', 16, 0, ''),
(17, 'tilakpatidar', 'Great tutorial ! Really Helpful !!', '2014-12-24 14:13:36', 17, 0, ''),
(18, 'tilakpatidar', 'Really Good', '2014-12-24 14:20:20', 8, 0, ''),
(19, 'idealbhopal', 'Great work !!', '2014-12-25 11:31:30', 13, 1, '[''tilakpatidar'']');

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE IF NOT EXISTS `content` (
  `content_id` int(11) NOT NULL AUTO_INCREMENT,
  `content_title` varchar(200) NOT NULL,
  `content_desc` text NOT NULL,
  `content_text` longtext NOT NULL,
  `content_author` varchar(40) NOT NULL,
  PRIMARY KEY (`content_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `content`
--

INSERT INTO `content` (`content_id`, `content_title`, `content_desc`, `content_text`, `content_author`) VALUES
(1, 'Chemical Bonding Intro', 'wiki', 'A lesson on chemical bonding, and how atoms of elements fulfill the octet rule by forming bonds. Part 1 deals with Ionic Bonding', 'tilakpatidar'),
(2, 'jQuery Wiki', 'Description from wikipedia', 'jQuery, at its core, is a DOM manipulation library. The DOM is a tree structure representation of all the elements of a web-page, and jQuery makes finding, selecting, and manipulating these DOM elements simple and convenient. For example, jQuery can be used for finding an element in the document with a certain property (e.g. all elements with an h1 tag), changing one or more of its attributes (e.g. color, visibility), or making it respond to an event (e.g. a mouse click).\n\nBeyond basic DOM selecting and manipulation, jQuery provides a new paradigm for event handling in JavaScript. The event assignment and the event callback function definition are done in a single step in a single location in the code. jQuery also aims to incorporate other highly used JavaScript functionalities (e.g. fade ins and fade outs when hiding elements, animations by manipulating CSS properties).\n\nThe advantages of using jQuery are:\n\nSeparates JavaScript and HTML: Instead of using HTML attributes to call JavaScript functions for event handling, jQuery can be used to handle events purely in JavaScript. Thus, the HTML tags and JavaScript can be completely separated.\nBrevity and Clarity: jQuery promotes brevity and clarity with features like chain-able functions and shorthand function names.\nEliminates cross-browser incompatibilities: The JavaScript engines of different browsers differ slightly, so JavaScript code that works for one browser may not work on the other. jQuery handles all these cross-browser inconsistencies and provides a consistent interface that works across different browsers.\nExtensible: jQuery makes extending the framework very simple. New events, elements and methods can be easily added and then reused as a plugin.', 'tilakpatidar');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE IF NOT EXISTS `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_title` varchar(200) NOT NULL,
  `course_desc` longtext NOT NULL,
  `course_author` varchar(40) NOT NULL,
  `course_content` longtext NOT NULL,
  `course_category` varchar(100) NOT NULL,
  `course_duration` varchar(4) NOT NULL,
  `course_users` longtext NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COMMENT='stores course details' AUTO_INCREMENT=19 ;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`course_id`, `course_title`, `course_desc`, `course_author`, `course_content`, `course_category`, `course_duration`, `course_users`) VALUES
(1, 'Chemical Bonding', 'A lesson on chemical bonding, and how atoms of elements fulfill the octet rule by forming bonds. Part 1 deals with Ionic Bonding', 'tilakpatidar', '[''t1'', ''v2'',''f1'']', 'chem', '120', '[''tilakpatidar'']'),
(2, 'Algebra', 'Algebra (from Arabic al-jebr meaning "reunion of broken parts"[1]) is one of the broad parts of mathematics, together with number theory, geometry and analysis.', 'tilakpatidar', '[''v3'',''f1'']', 'code', '120', '[''tilakpatidar'', ''idealbhopal'']'),
(3, 'Python Programming', 'Python is a high-level, interpreted, interactive and object-oriented scripting language. Python was designed to be highly readable which uses English keywords frequently where as other languages use punctuation and it has fewer syntactical constructions than other languages.', 'tilakpatidar', '[''v4'', ''v5'', ''v6'',''f1'']', 'code', '120', '[''tilakpatidar'']'),
(4, 'Java Programming', 'Java is a high-level programming language originally developed by Sun Microsystems and released in 1995. Java runs on a variety of platforms, such as Windows, Mac OS, and the various versions of UNIX. This tutorial gives a complete understanding of Java.', 'tilakpatidar', '[''v7'',''f1'']', 'code', '120', '[''tilakpatidar'']'),
(5, 'Fourier Transform', 'The Fourier transform decomposes a function of time (a signal) into the frequencies that make it up.', 'tilakpatidar', '[''v8'', ''v9'',''f1'']', 'math', '120', ''),
(6, 'Laplace Transform', 'The Laplace transform is a widely used integral transform in mathematics and electrical engineering named after Pierre-Simon Laplace that transforms the ...', 'tilakpatidar', '[''v10'', ''v11'',''f1'']', 'math', '120', ''),
(7, 'Z Transform', 'In mathematics and signal processing, the Z-transform converts a discrete-time signal, which is a sequence of real or complex numbers, into a complex ...', 'tilakpatidar', '[''v12'', ''v13'',''f1'']', 'math', '120', ''),
(8, 'Maxwell Eqns', 'Maxwell''s equations are a set of partial differential equations that, together with the Lorentz force law, form the foundation of classical electrodynamics, classical ...', 'tilakpatidar', '[''v14'',''f1'']', 'phy', '120', ''),
(9, 'Electromagnetism', 'Electromagnetism is the study of the electromagnetic force which is a type of physical interaction that occurs between electrically charged particles. The electromagnetic force usually manifests as electromagnetic fields, such as electric fields, magnetic fields and light.', 'tilakpatidar', '[''v15'', ''v16'',''f1'']', 'phy', '120', ''),
(10, 'Acoustics', 'Acoustics is the interdisciplinary science that deals with the study of all mechanical waves in gases, liquids, and solids including topics such as vibration, sound, ...', 'tilakpatidar', '[''v17'', ''v18'',''f1'']', 'phy', '120', ''),
(11, 'Ionic Bonding', 'Ionic bonding is a type of chemical bond that involves the electrostatic attraction between oppositely charged ions. These ions represent atoms that have lost one or more electrons (known as cations) and atoms that have gained one or more electrons (known as an anions).', 'tilakpatidar', '[''v19'', ''v20'',''f1'']', 'chem', '120', '[''tilakpatidar'']'),
(12, 'Water Treatment', 'Water treatment is, collectively, the industrial-scale processes that makes water more acceptable for an end-use, which may be drinking, industry, or medicine.', 'tilakpatidar', '[''v21'',''f1'']', 'chem', '120', '[''tilakpatidar'']'),
(13, 'NodeJS', 'Node.js is an open source, cross-platform runtime environment for server-side and networking applications. Node.js applications are written in JavaScript, and ...', 'tilakpatidar', '[''f1'',''v27'',''v28'',''v29'']', 'code', '120', '[''tilakpatidar'', ''idealbhopal'']'),
(14, 'Algorithm Analysis', 'Algorithm analysis is an important part of a broader computational complexity theory, which provides theoretical estimates for the resources needed by any algorithm which solves a given computational problem. These estimates provide an insight into reasonable directions of search for efficient algorithms.', 'tilakpatidar', '[''v22'',''f1'']', 'code', '180', ''),
(15, 'Javascript Programming', 'JavaScript is classified as a prototype-based scripting language with dynamic typing and first-class functions. This mix of features makes it a multi-paradigm language, supporting object-oriented,[6] imperative, and functional[1][7] programming styles.', 'tilakpatidar', '[''v23'',''f1'']', 'code', '220', '[''tilakpatidar'']'),
(16, 'jQuery Tutorial', 'jQuery is a cross-platform JavaScript library designed to simplify the client-side scripting of HTML.[2] Used by over 60% of the 10,000 most visited websites,[3] jQuery is the most popular JavaScript library in use today.[4][5] jQuery is free, open source software, licensed under the MIT License.[1]', 'tilakpatidar', '[''t2'', ''v24'', ''v25'',''f1'']', 'code', '120', '[''tilakpatidar'']'),
(17, 'Probability', 'Probability is the measure of how likely an event is to occur. Each possible result of a probability experiment or situation is an outcome.', 'tilakpatidar', '[''v26'',''f1'']', 'code', '190', '[''tilakpatidar'']');

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE IF NOT EXISTS `file` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `file_title` varchar(200) NOT NULL,
  `file_desc` varchar(400) NOT NULL,
  `file_link` text NOT NULL,
  `file_author` varchar(40) NOT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`file_id`, `file_title`, `file_desc`, `file_link`, `file_author`) VALUES
(1, 'Some File.', 'File is just to show that site supports google docs.', '<iframe src="https://docs.google.com/viewer?authuser=0&amp;srcid=0B4eqHdDuxv_0OHBSeHlyWWtWaE0&amp;\npid=explorer&amp;a=v&amp;chrome=false&amp;embedded=true" height="1380" width="640"></iframe>', 'tilakpatidar');

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE IF NOT EXISTS `info` (
  `username` varchar(40) NOT NULL,
  `profile_pic` text NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `email` varchar(48) NOT NULL,
  `mob` varchar(12) NOT NULL,
  `sex` varchar(6) NOT NULL,
  `dob` date NOT NULL,
  `college` varchar(100) NOT NULL,
  `courses` mediumtext NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `email_2` (`email`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email_3` (`email`),
  UNIQUE KEY `email_4` (`email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`username`, `profile_pic`, `fname`, `lname`, `email`, `mob`, `sex`, `dob`, `college`, `courses`) VALUES
('admin', 'admin.png', 'Admin', 'Admin', 'admin@gmail.com', '919985868485', 'Male', '2014-05-05', '', ''),
('ffgf', 'ffgf.png', 'Dsjfhjkh', 'Patidar', 'jkljsdl@gmal.com', '919986859698', 'Male', '2014-05-16', '', ''),
('nidhi', 'nidhi.png', 'Nidhi', 'Patidar', 'nidhioatidar@gmail.com', '989952415632', 'Female', '2014-05-02', '', ''),
('sdfg', 'sdfg.png', 'Dshfskjh', 'Patidar', 'kkjjklsjfl@gdfds.com', '989956325632', 'Male', '2014-05-16', '', ''),
('sdfre', 'sdfre.jpg', 'Sdfhkj', 'Patidar', 'jdlkfjskldf@gdfgd.com', '989956235689', 'Male', '2014-05-15', '', ''),
('tilakpatidar', '', 'Tilak', 'Patidar', 'tilakpatidar@gmail.com', '', 'male', '2012-12-22', 'srm', '[''13'', ''4'', ''15'', ''16'', ''3'', ''1'', ''17'', ''11'', ''12'', ''2'']'),
('tilak0', 'tilak0.png', 'Hjkh', 'Hjkhjk', 'sahdakj@sgsd.com', '919986595698', 'Male', '2014-05-02', '', ''),
('tyuii', 'tyuii.jpg', 'Sjdfk', 'Patidar', 'jhjkhjkhds@gmail.com', '989956856985', 'Male', '2014-05-03', '', ''),
('tyuui', 'tyuui.png', 'Jlk', 'Jkj', 'jklsjdfkls@gsfs.com', '979962365236', 'Male', '2014-05-05', '', ''),
('vineet', 'user.png', 'Vineet', 'Patidar', 'vineet@gmail.com', '919963524152', 'Male', '2014-05-09', '', ''),
('nidhiii', '', 'Tilak', 'Patidar', 'nidhi@gmail.com', '', 'female', '2014-12-22', 'SRM', ''),
('tilakk', '', 'Tilak', 'Patidar', 'tilak@gmail.com', '', 'male', '2014-12-24', 'SRM', ''),
('sagar', '', 'Sagar', 'Sahni', 'hello.sagarsahni@gmail.com', '', 'male', '1996-06-19', 'SRM ', ''),
('idealbhopal', '', 'Subhash', 'Patidar', 'idealbhopal@gmail.com', '', 'male', '2014-12-24', 'HOLKAR', '[''13'', ''2'']');

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE IF NOT EXISTS `session` (
  `sid` varchar(45) NOT NULL,
  `username` varchar(40) NOT NULL,
  PRIMARY KEY (`sid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`sid`, `username`) VALUES
('ac507992ee780bc76a7e2abcdad50e2ea72fc69f', 'sagar'),
('c117e15393613bc93eaa73c3f0899eebd1cb78d6', 'idealbhopal'),
('2c8a4c082be650149db35579ee0b5892559ebee0', 'tilakpatidar');

-- --------------------------------------------------------

--
-- Table structure for table `video`
--

CREATE TABLE IF NOT EXISTS `video` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `video_title` varchar(200) NOT NULL,
  `video_desc` varchar(400) NOT NULL,
  `video_link` text NOT NULL,
  `video_author` varchar(40) NOT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

--
-- Dumping data for table `video`
--

INSERT INTO `video` (`video_id`, `video_title`, `video_desc`, `video_link`, `video_author`) VALUES
(2, 'Chemistry 4.1 Chemical Bonding (Part 1 of 2)', 'A lesson on chemical bonding, and how atoms of elements fulfill the octet rule by forming bonds. Part 1 deals with Ionic Bonding between metals and nonmetals.', 'https://www.youtube.com/watch?v=ppjnCNuaqbc', 'tilakpatidar'),
(3, 'Interstellar Soundtrack - Day One Dark', 'Hans Zimmer - Day One Dark (Interstellar Soundtrack)(Bonus Track)', 'http://www.youtube.com/watch?v=PHYKpLN1kio', 'tilakpatidar'),
(4, 'Python Beginner Tutorial 1 (For Absolute Beginners)', 'This Python Programming Tutorial covers the instillation python and setting up the python development environment. This video covers setting up a system variable for using python from the windows command prompt and also covers using python from the built in IDLE IDE. After setting up the development an environment this video demonstrates how to create and run your first python script (Hello World)', 'https://www.youtube.com/watch?v=cpPG0bKHYKc', 'tilakpatidar'),
(5, 'Google Python Class Day 1 Part 1', 'Google Python Class Day 1 Part 1:\nIntroduction and Strings.\n \nBy Nick Parlante.\n \nSupport materials and exercises:\nhttps://developers.google.com/edu/python/introduction', 'https://www.youtube.com/watch?v=tKTZoB2Vjuk', 'tilakpatidar'),
(6, 'Python for Programmers: A Project-Based Tutorial', 'Alexandra Strong, Katharine Jarmul, Christine Cheung\nAre you a Python-curious programmer? Learn by writing your first project! You''ll build a complete quiz creation web application. We will cover topics from data structures and classes, to debugging', 'https://www.youtube.com/watch?v=Nc16qeGBtMU', 'tilakpatidar'),
(7, 'Java Programming - Step by Step tutorial', 'Easy to follow step by step Java programming tutorial.\nBuy the full 4 hour video at http://www.patrickvideos.com\nThe direct download link at https://gumroad.com/l/WloP\n\nIn 4 hrs you will learn all the important concepts of Java, each explained using small simple programs. The teaching method used, will be the easiest way to learn Java, that you will ever find.\n\nReproducing the previously top  rate', 'https://www.youtube.com/watch?v=3u1fu6f8Hto', 'tilakpatidar'),
(8, 'Lecture 1 | The Fourier Transforms and its Applications', 'Lecture by Professor Brad Osgood for the Electrical Engineering course, The Fourier Transforms and its Applications (EE 261).  Professor Osgood provides an overview of the course, then begins lecturing on Fourier series.\r\n\r\nThe Fourier transform is a tool for solving physical problems. In this course the emphasis is on relating the theoretical principles to solving practical engineering and scienc', 'https://www.youtube.com/watch?v=gZNm7L96pfY', 'tilakpatidar'),
(9, 'Lecture 2 | The Fourier Transforms and its Applications', 'Lecture by Professor Brad Osgood for the Electrical Engineering course, The Fourier Transforms and its Applications (EE 261).  Professor Osgood''s lecture addresses the question- How can we use such simple functions, sin(t) and cos(t) to model such periodic phenomenon? He takes the students through the first steps in analyzing general periodic phenomenon.\r\n\r\nThe Fourier transform is a tool for solv', 'https://www.youtube.com/watch?v=1rqJl7Rs6ps', 'tilakpatidar'),
(10, 'Lecture 20, The Laplace Transform | MIT RES.6.007 Signals and Systems, Spring 2011', 'Lecture 20, The Laplace Transform\nInstructor: Alan V. Oppenheim\nView the complete course: http://ocw.mit.edu/RES-6.007S11\n\nLicense: Creative Commons BY-NC-SA\nMore information at http://ocw.mit.edu/terms\nMore courses at http://ocw.mit.edu', 'https://www.youtube.com/watch?v=pSN7t79RxC4', 'tilakpatidar'),
(11, '(1:2) Where the Laplace Transform comes from (Arthur Mattuck, MIT)', 'Next Part: http://www.youtube.com/watch?v=hqOboV2jgVo\r\n\r\nProf. Arthur Mattuck, of the Department of Mathematics at MIT, explains the derivation of the Laplace Transform.\r\n\r\nThis clip was taken from Prof. Mattuck''s class "18.03 Differential Equations" and can be found at:\r\nhttp://ocw.mit.edu/18-03S06\r\n\r\nThe complete version of this specific lecture can be viewed at:\r\nhttp://www.youtube.com/watch?v=', 'https://www.youtube.com/watch?v=zvbdoSeGAgI', 'tilakpatidar'),
(12, 'Lecture - 11 DFT (Contd.) Introduction to Z Transform', 'Lecture Series on Digital Signal Processing by Prof.S. C Dutta Roy, Department of Electrical Engineering, IIT Delhi. For More details on NPTEL visit http://nptel.iitm.ac.in', 'https://www.youtube.com/watch?v=qPpNYGAQf20', 'tilakpatidar'),
(13, 'Lecture-44 Inverse Z Transform', 'Lecture Series on Signals and System by Prof. K.S. Venktesh, Department of Electrical Engineering , IIT Kanpur For more details on NPTEL visit http://nptel.iitm.ac.in', 'https://www.youtube.com/watch?v=Uc5SFRp6ex0', 'tilakpatidar'),
(14, 'Maxwell''s Equations of Electromagnetism', 'http://www.aklectures.com/lecture/maxwells-equations-of-electromagnetism\n\nThe website organizes the videos into clear and structured chapters that you can use to watch the videos in sequential and logical order as taught by most educational institutions. Each lecture contains a description along with a customized comment section that you can use to ask questions regarding the topic. Posting questi', 'https://www.youtube.com/watch?v=yZNgF5c0oT8', 'tilakpatidar'),
(15, 'Electromagnetism - LECTURE 01 Part 01/01 - by Prof Robert de Mello Koch', 'This video forms part of a course on Electromagnetism by Prof Robert de Mello Koch held at AIMS South Africa in 2013.\n\nPlease visit https://sites.google.com/a/aims.ac.za/electromagnetism/ to download the supporting course notes.\n\nThe concept of a field is introduced and the necessity of a description in terms of fields is explained.\nThe interaction between static charges, using the superposition p', 'https://www.youtube.com/watch?v=an8fWwECJVM', 'tilakpatidar'),
(16, 'Electromagnetism - LECTURE 12 Part 01/04 - by Prof Robert de Mello Koch', 'This video forms part of a course on Electromagnetism by Prof Robert de Mello Koch held at AIMS South Africa in 2013.\n\nPlease visit https://sites.google.com/a/aims.ac.za/electromagnetism/ to download the supporting course notes.\n\nThe concept of a field is introduced and the necessity of a description in terms of fields is explained.\nThe interaction between static charges, using the superposition p', 'https://www.youtube.com/watch?v=w-KLwOwuyvo', 'tilakpatidar'),
(17, '[Lecture 1-1: String vibration and wave] Introduction to Acoustics by Prof. Yang-Hann Kim', 'This movie clip is a part of the first lecture on Acoustics at KAIST, 2009 Spring Semester. - Vibration and waves', 'https://www.youtube.com/watch?v=0kdecLMnqZA', 'tilakpatidar'),
(18, 'Acoustics. Introduction. Lecture 1, Part A.', 'An 11 lecture series on linear acoustics.  This is a study of the creation, propagation and reception of sound.  Impedance. Comparison of major features of acoustics hydrodynamics, subsonic wing theory and supersonic piston theory.', 'https://www.youtube.com/watch?v=D1pu0zrMlw4', 'tilakpatidar'),
(19, 'Ionic Bonding Lecture', 'Why do cations and anions bond-  Polyatomic ions included!', 'https://www.youtube.com/watch?v=sAGW7ddoTSg', 'tilakpatidar'),
(20, 'Chemical Bonds: Covalent vs. Ionic', 'Mr. Andersen shows you how to determine if a bond is nonpolar covalent, polar covalent, or ionc.\n\nIntro Music Atribution\nTitle: I4dsong_loop_main.wav\nArtist: CosmicD\nLink to sound: http://www.freesound.org/people/CosmicD/sounds/72556/\nCreative Commons Atribution License', 'https://www.youtube.com/watch?v=7DjsD7Hcd9U', 'tilakpatidar'),
(21, 'Water and Wastewater Treatment Lecture', 'Video put together for the MSc in Environmental Technology at Imperial College London', 'https://www.youtube.com/watch?v=JL3y1CWhirQ', 'tilakpatidar'),
(22, 'Analysis and Design of Algorithms', 'Analysis and Design of Algorithms  By Prof. Sibi Shaji, Dept. of Computer Science, Garden City College, Bangalore', 'https://www.youtube.com/watch?v=Qe6PUzVu2pk', 'tilakpatidar'),
(23, 'JavaScript Video Tutorial Pt 1', 'Best JavaScript Book : http://goo.gl/zodRHD\n\nHere I teach you how to write JavaScript programs in just 30 minutes. I specifically cover : JavaScript Datatypes, Embedding JavaScript, Linking to JavaScript, Conditional Statements, Looping, Arrays, Strings, Functions and much more.\n\nArticle is Here: http://bit.ly/fUvtp8\nCode is Here: http://bit.ly/hoF0Fe', 'https://www.youtube.com/watch?v=_cLvpJY2deo', 'tilakpatidar'),
(24, 'jQuery Tutorial #1 - jQuery Tutorial for Beginners', 'This jQuery Tutorial for beginners will help you get jQuery on your page and get up-to-speed with how to use basic jQuery commands.\n\nWhat is jQuery?  As you''ll see in this tutorial, even beginners to javascript can write jQuery within minutes.  It''s also the most universally used javascript library in the world at present, so odds are your next employer will be using it.\n\nThe first thing we''ll be ', 'https://www.youtube.com/watch?v=hMxGhHNOkCU', 'tilakpatidar'),
(25, 'jQuery Tutorial #2 - Event Binding - jQuery Tutorial for Beginners', 'This second part of the jQuery Tutorial for beginners will show you how to do event binding with jQuery.  Events happen whenever a user clicks, hovers, drags, types, or does pretty much anything to interact with an HTML element.\n\njQuery allows the web developer to easily write a program to listen to these javavscript events and modify the webpage in realtime.  This is often called a dynamic websit', 'https://www.youtube.com/watch?v=G-POtu9J-m4', 'tilakpatidar'),
(26, 'Basic Probability Tutorial', 'This unit describes basic probability definitions and concepts and covers experimental, theoretical, and geometric probability.', 'https://www.youtube.com/watch?v=VqndHpCfUWA', 'tilakpatidar'),
(27, 'Node.js Tutorial with Ryan Dahl, creator of Node.js', 'You''ve learned how to write code, but how do you actually launch your website or app? LearnStreet courses and tutorials have ...', 'https://www.youtube.com/watch?v=eqlZD21DME0', 'tilakpatidar'),
(28, 'Learn Node.js (Level 1)', 'Play the entire course: http://bit.ly/LearnNodejs Learn Node.js and start building lightweight, real-time applications. Our interactive ...', 'https://www.youtube.com/watch?v=GJmFG4ffJZU', 'tilakpatidar'),
(29, 'Hands on with Node.js / Beginner Guide / Getting Started', 'Node.js is an exciting new platform for building web applications in JavaScript. With its unique I/O model, it excels at the sort of ...', 'https://www.youtube.com/watch?v=_l96hPlqzcI', 'tilakpatidar');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
