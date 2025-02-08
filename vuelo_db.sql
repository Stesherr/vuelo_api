create database vuelo_db;
use vuelo_db;

create table usuarios (
	id INT auto_increment primary key,
    nombre varchar(255) not null,
    correo varchar(255) unique not null,
    contraseña varchar(255) not null
);

create table vuelos(
	id int auto_increment primary key,
    origen varchar(255) not null,
    destino varchar(255) not null,
    fecha date not null,
    horario time not null,
    disponibilidad int not null
);

create table reservas(
	id int auto_increment primary key,
    usuario_id int,
    vuelo_id int,
    estado varchar(50) default 'confirmada',
    foreign key (usuario_id) references usuarios(id),
    foreign key (vuelo_id) references vuelos(id)
);
