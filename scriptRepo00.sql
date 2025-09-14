#CREACIÓN DE LA BASE DE DATOS

CREATE DATABASE DB_TRABAJO01;


CREATE TABLE `DB_TRABAJO01`.`estados` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);

CREATE TABLE `DB_TRABAJO01`.`personas` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `cedula` VARCHAR(50) NOT NULL UNIQUE,
    `nombre` VARCHAR(250) NOT NULL,
	`estado` INT NOT NULL,
	`fecha` DATETIME NOT NULL,
	`activo` BIT NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_personas__estados` FOREIGN KEY (`estado`) REFERENCES `estados`(`id`)
);

INSERT INTO `DB_TRABAJO01`.`estados` (`nombre`) VALUES ('Solter@s');
INSERT INTO `DB_TRABAJO01`.`personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) 
VALUES ('6546465', 'Pepito Perez', 1, NOW(), 1);

CREATE USER 'user_trabajo01'@'localhost' IDENTIFIED BY '1234';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_trabajo01'@'localhost' WITH GRANT OPTION;