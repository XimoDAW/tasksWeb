DROP DATABASE tasks;

CREATE DATABASE tasks;

USE tasks;

CREATE TABLE management (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	usr VARCHAR(15),
	pass VARCHAR(30)
	);
	
CREATE TABLE posit (
	id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	NAME VARCHAR(30),
	id_management INT,
	FOREIGN KEY (id_management) REFERENCES management(id)
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