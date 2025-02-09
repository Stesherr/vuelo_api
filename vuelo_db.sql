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

-- Insertar 50 usuarios
INSERT INTO usuarios (nombre, correo, contraseña) VALUES
('Usuario1', 'usuario1@example.com', 'pass1'),
('Usuario2', 'usuario2@example.com', 'pass2'),
('Usuario3', 'usuario3@example.com', 'pass3'),
('Usuario4', 'usuario4@example.com', 'pass4');

-- Insertar 50 vuelos
INSERT INTO vuelos (origen, destino, fecha, horario, disponibilidad) VALUES
('Lima', 'Bogotá', '2025-02-10', '08:00:00', 150),
('Bogotá', 'Madrid', '2025-02-11', '10:30:00', 200),
('Madrid', 'París', '2025-02-12', '15:00:00', 180),
('París', 'Roma', '2025-02-13', '12:45:00', 170);

INSERT INTO vuelos (origen, destino, fecha, horario, disponibilidad) VALUES
('Bogotá', 'Madrid', '2025-02-11', '16:30:00', 100);

