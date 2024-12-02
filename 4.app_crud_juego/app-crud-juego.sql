CREATE DATABASE IF NOT EXISTS app_crud_juego;
USE app_crud_juego;

CREATE TABLE IF NOT EXISTS juegos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL
);

INSERT INTO juegos(nombre,descripcion,precio)
VALUES('Zelda','Juego de rol',50000);