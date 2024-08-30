
CREATE DATABASE IF NOT EXISTS School;
USE school;
CREATE  IF NOT EXISTS Students ( sid INT PRIMARY, sname VARCHAR(30), gender CHAR(1), mark DECIMAL(4,2)) ;
INSERT INTO students VALUES (101,"Neha","F",97);
INSERT INTO students VALUES (111,"Ria","F",67);
INSERT INTO students VALUES (231,"Mohan","M",78);
INSERT INTO students VALUES (124,"Rohan","M",94);
INSERT INTO students VALUES (121,"Misha","F",92);