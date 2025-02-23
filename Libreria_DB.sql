create database LibOnline;
use LibOnline; 


create table Usuarios(
id_usuario INT auto_increment,
id_direccion INT NOT NULL,
id_login INT NOT NULL,
nombre VARCHAR(30) NOT NULL,
apellidos VARCHAR(30) NOT NULL,
numero_telefonico VARCHAR(10) NOT NULL,
PRIMARY KEY(id_usuario)
);

create table Logins(
id_login INT auto_increment,
correo VARCHAR(256) NOT NULL,
contrasena VARCHAR(256) NOT NULL,
privilegio VARCHAR(15) NOT NULL,
UNIQUE KEY (correo),
PRIMARY KEY (id_login)
);

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



create table Envios(
id_envio INT auto_increment,
id_compra INT NOT NULL,
id_usuario INT NOT NULL,
fecha_entrega DATETIME NOT NULL,
estatus VARCHAR(20) NOT NULL,
PRIMARY KEY (id_envio)
);

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

create table Compras (
id_compra INT auto_increment,
id_usuario INT NOT NULL,
id_libro VARCHAR(12) NOT NULL,
estatus VARCHAR(20) NOT NULL,
fecha_pedido DATE NOT NULL,
total NUMERIC(6) NOT NULL,
PRIMARY KEY (id_compra),
FOREIGN KEY (id_libro) REFERENCES Libros(id_libro)
);



ALTER TABLE Usuarios ADD FOREIGN KEY (id_direccion) REFERENCES Direcciones(id_direccion);
ALTER TABLE Usuarios ADD FOREIGN KEY (id_login) REFERENCES Logins(id_login);
ALTER TABLE Envios ADD FOREIGN KEY (id_compra) REFERENCES Compras(id_compra);
ALTER TABLE Compras ADD FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario);
/*ALTER TABLE Compras ADD FOREIGN KEY (id_libro) REFERENCES Libros(id_libro);*/
ALTER TABLE Envios ADD FOREIGN KEY (id_usuario) REFERENCES Compras(id_usuario);


insert into logins(correo,contrasena, privilegio) values ("b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eYdm/VPLjttMYYTSVBSLrxCikTN0Gbwa'","b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eR12/Tvs.IJYWlf6eU14Tf/G0FsL0FL2'",'user');
/*
crico@utez.edu.mx encriptado:
b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eYdm/VPLjttMYYTSVBSLrxCikTN0Gbwa'
*/
insert into logins(correo,contrasena, privilegio) values ("b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eOxTNSN27aeP6RpdrqCZqw8kpeKlVVJq'","b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eR12/Tvs.IJYWlf6eU14Tf/G0FsL0FL2'",'admin');
/*
messi@utez.edu.mx encriptado:
b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eOxTNSN27aeP6RpdrqCZqw8kpeKlVVJq'
contraseña de ambos encriptados (1234):
b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eR12/Tvs.IJYWlf6eU14Tf/G0FsL0FL2'
*/


insert into direcciones(calle,estado,municipio,colonia,cp,num_exterior,num_interior) values ("1","2","3","4","5","6","7");
insert into direcciones(calle,estado,municipio,colonia,cp,num_exterior,num_interior) values ("7","6","5","4","3","2","1");

insert into usuarios(id_direccion, id_login,nombre,apellidos,numero_telefonico) values (1,1,"Cristobal Eduardo","Serrano Bahena", 7772689242);
insert into usuarios(id_direccion, id_login,nombre,apellidos,numero_telefonico) values (2,2,"Lionel Andrés","Messi", 7772689243);


DELIMITER $$
CREATE PROCEDURE VerificarUsuario(
	in chamo VARCHAR(256),
    in chamo2 VARCHAR(256)
)
BEGIN
    SELECT distinct * FROM Logins WHERE (correo = chamo AND contrasena=chamo2);
END$$
DELIMITER ;




call VerificarUsuario("b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eOxTNSN27aeP6RpdrqCZqw8kpeKlVVJq'","b'$2b$12$Bj2s7PI42QkpqlbJtkAH/eR12/Tvs.IJYWlf6eU14Tf/G0FsL0FL2'");

/*
show tables;
insert into Logins (correo,contrasena,privilegio) values ('20223tn999@utez.edu.mx','Cisco123','cliente');
select * from Logins;
insert into clientes 
  values ('Marcos Luis','marcosluis@gmail.com',aes_encrypt('5390700823285988','xyz123'));
drop database libonline;
drop table Compras;
*/
