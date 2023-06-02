-- USE STUDENTSREG;
-- DROP TABLE TUTOR;
-- DROP TABLE STUDENT;
-- DROP TABLE MODULES;
-- DROP TABLE STUDENT_ENROLEMENT;
-- DROP TABLE TOPICS;
-- DROP TABLE LEARN_PREFERENCE;
-- SHOW databases; 
DROP DATABASE IF EXISTS STUDENTSREG;
CREATE DATABASE STUDENTSREG;
USE STUDENTSREG;


CREATE TABLE TUTOR (
  Tut_Id VARCHAR(10) NOT NULL,
  TName VARCHAR(45) NOT NULL,
  DoB DATE NOT NULL,
  HOURS DOUBLE,
  PRIMARY KEY (Tut_Id)
  );
  
CREATE TABLE STUDENT
(
SID VARCHAR(10) NOT NULL, 
PRIMARY KEY (SID),
SNAME VARCHAR(30),
EMAIL VARCHAR(30),
Tutor_Id VARCHAR (10) NULL, 
FOREIGN KEY (Tutor_Id)
  REFERENCES TUTOR (Tut_Id)
  ON DELETE SET NULL
  ON UPDATE CASCADE
);

CREATE TABLE MODULES
(
MID VARCHAR(15) NOT NULL, 
PRIMARY KEY (MID),
MNAME VARCHAR(40),
LEVEL VARCHAR(2),
TUTOR_Tut_Id VARCHAR(10), 
FOREIGN KEY(TUTOR_Tut_Id) REFERENCES TUTOR (Tut_Id) 
  ON UPDATE CASCADE 
    ON DELETE SET NULL
);

CREATE TABLE STUDENT_ENROLEMENT
(
SID VARCHAR(10) NOT NULL, 
FOREIGN KEY (SID) REFERENCES STUDENT(SID),
MID VARCHAR(15) NOT NULL, 
FOREIGN KEY (MID) REFERENCES MODULES(MID),
ACAD_YEAR VARCHAR(10),
PRIMARY KEY (SID, MID, ACAD_YEAR)
);

CREATE TABLE TOPICS (
  TId INT NOT NULL,
  Tdesc VARCHAR(100) NULL,
  Mod_Id VARCHAR(15) NULL,
  PRIMARY KEY (TId),
  CONSTRAINT MID
    FOREIGN KEY (Mod_Id) REFERENCES MODULES (MID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    );
    
CREATE TABLE LEARN_PREFERENCE (
  TPreference VARCHAR(50) NULL,
  APreference VARCHAR(50) NULL,
  Stud_Id VARCHAR(10) NULL,  
  CONSTRAINT SID
    FOREIGN KEY (Stud_Id) REFERENCES STUDENT (SID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    );
    
INSERT INTO  TUTOR  VALUES 
  (1000,'David Wyatt','1982/01/01',4),
  (1001,'Raj Ramachandran','1987/02/03',3),
  (1002,'Kamran Soomro','1985/04/13',4),
  (1003,'David Ludlow','1950/01/16',1),
  (1004,'Zaheer Khan','1979/08/31',null),
  (1005,'Djamel Djnouri','1981/06/30',null),
  (1006,'Elias Piminides','1969/03/27',null),
  (1007,'Kamran Soomro','1965/11/05',null),
  (1008,'Barkha Javed','1995/11/11', null),
  (1009,'James Lear','1993/02/12',null); 


INSERT INTO  STUDENT VALUES 
(1000,'Abdul Basit Chaudhry','abc@abc.com',1003),
(1001,'Daniel Everret Fernandes','def@def.com',1000),
(1002,'Gigi Hadi Ingram','ghi@ghi.com',1001),
(1003,'Jacob Knowle Lewis','jkl@jkl.com',1002),
(1004,'Martin Newton Oolu','mno@mno.com',1002),
(1005,'Patrick Quinn Rogers','pqr@pqr.com',1002),
(1006,'Shabaz Tanveer Ucch','stu@stu.com',1001),
(1007,'Umar Victor Qayyum','uvq@stu.com',1001),
(1008,'Qais Russell Stuart','qrs@qrs.com',1000),
(1009,'Rachel Shaw Trump','rst@rst.com',1000),
(1010,'Tania Uno Victoria','tuv@tuv.com',1000),
(1011,'Umber Vishal Xavier','uvx@uvx.com',1002),
(1012,'James Baker','jb@jb.com',null);


INSERT INTO MODULES VALUES
(101,'Web Programming',1,1004),
(102,'Web Design',1,1000),
(103,'CMS',1,1000),
(104,'E-Commerce',1,1000),
(105,'Advanced Programming',2,1002),
(106,'Advanced Databases',2,1006),
(107,'Artificial Intelligence',2,1005),
(108,'Machine Learning',2,1005),
(109,'Data Science',2,1002),
(110,'Project Workshops',3,1006),
(111,'Data Analytics and Visualisation',3,1002),
(112,'Distributed and Parallel computing',3,1004),
(114,'Cyber Security',3,1006),
(115,'Deep Learning',3,1002),
(116,'Computing Project',3,1004),
(117,'Placement',3,1001),
(118,'Requirements Engineering',3,1001),
(119,'Web Development and DB',1,null),
(120,'Networks',3,null);


INSERT INTO STUDENT_ENROLEMENT VALUES
(1000,101,'2014-2015'),
(1000,102,'2014-2015'),
(1001,101,'2014-2015'),
(1001,103,'2014-2015'),
(1001,104,'2014-2015'),
(1002,104,'2014-2015'),
(1000,105,'2015-2016'), 
(1000,106,'2015-2016'),
(1001,107,'2015-2016'),
(1001,108,'2015-2016'),
(1002,103,'2015-2016'),
(1002,105,'2015-2016'),
(1003,110,'2015-2016'),
(1003,111,'2015-2016'),
(1004,103,'2015-2016'),
(1004,105,'2015-2016'),
(1004,110,'2015-2016'),
(1004,115,'2015-2016'),
(1005,117,'2016-2017'),
(1006,117,'2017-2018'),
(1007,117,'2017-2018'),
(1005,116,'2018-2019'),
(1007,116,'2018-2019'),
(1007,115,'2018-2019'),
(1007,114,'2018-2019');


INSERT INTO TOPICS VALUES
(1,'conceputal datamodel',106),
(2,'logical datamodel',106),
(3,'physical datamodel',106),
(4,'relational datamodel',106),
(5,'SQL',106),
(6,'NoSQL',106),
(7,'Flask',101),
(8,'HTML',101),
(9,'JavaScript',101),
(10,'OOP',105),
(11,'Web Security',101),
(12,'Responsive Design',102),
(13,'Responsive Design',101),
(14,'Lambda Functions',105),
(15,'SDLC',110),
(16,'Data management',103),
(17,'Data management',104),
(18,'Data management',106),
(19,'Data management',107),
(20,'Data management',108),
(21,'Data management',109),
(22,'Data management',111),
(23,'Data management',114),
(24,'Data management',115),
(25,'Data management',118),
(26,'Project management',117),
(27,'Software processes',117),
(28,'Software processes',116),
(29,'HTTP request and response',null);


INSERT INTO LEARN_PREFERENCE VALUES
('Online','No Exam',1000),
('Online','Project',1001),
('F-2-F','Project',1002),
('Blended','No Exam',1003),
('F-2-F','Coursework',1004);



-- CREATE A VIEW of MNAMES FOR TUTOR ID 1006   - Vertical View
CREATE VIEW TUTORMODULE
AS SELECT MNAME 
  FROM MODULES
  WHERE TUTOR_Tut_Id = 1006;

-- CREATE A VIEW of Module details for TUTOR ID 1006  - Horizontal View
CREATE VIEW TUTORMODULEDET
AS SELECT * 
  FROM MODULES
    WHERE TUTOR_Tut_Id = 1006;


-- Create a view that list all students who were enrolled on "Web Programming" in academic year 2014-15
CREATE VIEW WebStudents201415
AS SELECT s.SID, s.SName, e.ACAD_YEAR, m.MID, m.MName
  FROM STUDENT s, MODULES m, STUDENT_ENROLEMENT e
  WHERE s.SID = e.SID AND e.MID = m.MID AND m.MNAME = 'Web Programming' AND e.ACAD_YEAR =  '2014-2015'
  ORDER By s.SID;



-- Create a student view showing student id and name and how many modules that student is enrolled on in each academic year
CREATE VIEW StudentsModuleYear
AS SELECT s.SID, s.SName, e.ACAD_YEAR, COUNT(e.MID) AS cnt
  FROM STUDENT s JOIN STUDENT_ENROLEMENT e ON s.SID = e.SID
  GROUP By s.SID, s.SName, e.ACAD_YEAR  
  ORDER By s.SID;
    


-- Deleting View
-- DROP VIEW studentsmoduleyear;

-- View restrictions
-- a. Query this view and list all students where count is > 2.
-- Select * FROM StudentsModuleYear WHERE cnt > 2;
-- Select COUNT(cnt) FROM StudentsModuleYear;

-- CREATE A VIEW of Module details for TUTOR ID 1006  - Horizontal View - with check option
CREATE VIEW TUTORMODULEWCHOP
AS SELECT * 
  FROM MODULES
  WHERE TUTOR_Tut_Id = 1006
WITH CHECK OPTION;



-- a. Show that ‘with check option’ works by updating tutor id from 1006 to 10061
-- UPDATE TUTORMODULEWCHOP SET TUTOR_Tut_Id = 10061 WHERE TUTOR_Tut_Id=1006; 
-- #Error Code: 1369. CHECK OPTION failed 'studentsreg.tutormodulewchop'



CREATE VIEW TUTORMODULEWCHOPV1
AS SELECT * 
  FROM MODULES
  WHERE TUTOR_Tut_Id = 1006
WITH CHECK OPTION;

Commit;
-- UPDATE TUTORMODULEWCHOP SET TUTOR_Tut_Id = 1007 WHERE TUTOR_Tut_Id=1006; 
-- INSERT INTO TUTORMODULEWCHOP VALUES (121,'Network Design',3,1007);


    