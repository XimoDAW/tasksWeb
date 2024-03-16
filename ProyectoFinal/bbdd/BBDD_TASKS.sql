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
	status BOOLEAN,
	FOREIGN KEY(id_posit) REFERENCES posit(id),
	FOREIGN KEY(id_management) REFERENCES management(id)
	);