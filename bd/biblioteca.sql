
create table editorial(
	id_ed serial primary key not null,
	nom_ed varchar(50) not null,
	pais_ed varchar(50) not null,
	telefono_ed varchar(50) not null
);

create table tipo_libro(
	id_tipo_libro serial primary key not null,
	nombre_tipo varchar(50) not null
);

create table libro(
	id_libro serial primary key not null,
	titulo varchar(50) not null,
	autor varchar(50)not null,
	id_ed integer not null,
	isbn varchar(50) unique,
	paginas real not null,
	id_tipo_libro integer not null,
	disponible varchar(50) not null,
	FOREIGN KEY (id_ed) REFERENCES editorial(id_ed),
	FOREIGN KEY (id_tipo_libro) REFERENCES tipo_libro(id_tipo_libro)
);

create table usuarios(
	id_usuario serial primary key not null,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	dni varchar(50) not null,
	pwd varchar(50) not null
);

create table prestamos(
	id_prestamo serial primary key not null,
	id_usuario integer not null,
	id_libro integer not null,
	fecha_prestamo date,
	fecha_devolucion date,
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
	FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
);

insert into tipo_libro(nombre_tipo) values('ciencia');
insert into tipo_libro(nombre_tipo) values('matematica');
insert into tipo_libro(nombre_tipo) values('novela');
insert into tipo_libro(nombre_tipo) values('fisica');

insert into editorial(nom_ed, pais_ed, telefono_ed) values('bruño', 'peru', '333-6666');
insert into editorial(nom_ed, pais_ed, telefono_ed) values('parson', 'peru', '333-6666');
insert into editorial(nom_ed, pais_ed, telefono_ed) values('cuzcano', 'peru', '333-6666');
insert into editorial(nom_ed, pais_ed, telefono_ed) values('librodebolsillo', 'peru', '333-6666');

insert into libro(
	titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
	) values(
	'calculo1',
	'kafu',
	'2',
	'111aaa',
	'300',
	'2',
	'disponible'
);

insert into libro(
	titulo, autor, id_ed, isbn, paginas, id_tipo_libro, disponible
	) values(
	'ciencias y ambiente',
	'kafu',
	'1',
	'111bbb',
	'300',
	'1',
	'disponible'
);

