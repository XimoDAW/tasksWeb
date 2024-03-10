DROP DATABASE tasks;

CREATE DATABASE tasks;

USE tasks;
	
CREATE TABLE posit (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(30)
	);
	
CREATE TABLE management (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT
	);
	
CREATE TABLE task (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(30),
	description VARCHAR(300),
	id_posit INT,
	id_management INT,
	init DATE,
	END DATE,
	FOREIGN KEY(id_posit) REFERENCES posit(id),
	FOREIGN KEY(id_management) REFERENCES management(id)
	);
	
CREATE TABLE STATUS (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(20)
	);
	
CREATE TABLE task_status (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	id_task INT,
	id_status INT,
	FOREIGN KEY (id_task) REFERENCES task(id),
	FOREIGN KEY (id_status) REFERENCES STATUS(id)
	);