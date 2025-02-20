create database LibOnline;
use LibOnline; 

create table Logins(
id_login INT auto_increment,
correo VARCHAR(40) NOT NULL,
contrasena VARCHAR(12) NOT NULL,
privilegio VARCHAR(15) NOT NULL,
UNIQUE KEY (correo),
PRIMARY KEY (id_login)
);

create table Usuarios(
id_usuario INT auto_increment,
id_direccion INT NOT NULL,
id_login INT NOT NULL,
nombre VARCHAR(30) NOT NULL,
apellidos VARCHAR(30) NOT NULL,
numero_telefonico NUMERIC(10) NOT NULL,
PRIMARY KEY(id_usuario)
);

ALTER TABLE Usuarios ADD FOREIGN KEY (id_direccion) REFERENCES Direcciones(id_direccion);
ALTER TABLE Usuarios ADD FOREIGN KEY (id_login) REFERENCES Logins(id_login);

create table Direcciones(
id_direccion INT auto_increment,
calle VARCHAR(25) NOT NULL,
estado VARCHAR(20) NOT NULL,
municipio VARCHAR(25) NOT NULL,
colonia VARCHAR(25) NOT NULL,
cp NUMERIC(5) NOT NULL,
num_interior NUMERIC(4),
num_exterior NUMERIC(4) NOT NULL,
PRIMARY KEY (id_direccion)
);

create table Compras (
id_compra INT auto_increment,
id_usuario INT NOT NULL,
id_libro INT NOT NULL,
estatus VARCHAR(20) NOT NULL,
fecha_pedido DATE NOT NULL,
total NUMERIC(6) NOT NULL,
PRIMARY KEY (id_compra)
);

ALTER TABLE Compras ADD FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario);
ALTER TABLE Compras ADD FOREIGN KEY (id_libro) REFERENCES Libros(id_libro);

create table Envios(
id_envio INT auto_increment,
id_compra INT NOT NULL,
id_usuario INT NOT NULL,
fecha_entrega DATETIME NOT NULL,
estatus VARCHAR(20) NOT NULL,
PRIMARY KEY (id_envio)
);

ALTER TABLE Envios ADD FOREIGN KEY (id_compra) REFERENCES Compras(id_compra);
ALTER TABLE Envios ADD FOREIGN KEY (id_usuario) REFERENCES Compra(id_usuario);

create table Libros(
id_libro VARCHAR(12) NOT NULL,
nombre VARCHAR(40) NOT NULL,
editorial VARCHAR(40) NOT NULL,
autor VARCHAR(40) NOT NULL,
stock NUMERIC(6) NOT NULL,
estatus VARCHAR(20) NOT NULL,
precio NUMERIC(5) NOT NULL,
PRIMARY KEY (id_libro)
);

show tables;
drop database libonline;
drop table Compras;