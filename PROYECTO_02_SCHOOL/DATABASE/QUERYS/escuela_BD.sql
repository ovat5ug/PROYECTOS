USE escuela
-----PERSONA---------------------------------------------------------------
create table persona(
    id_persona int identity (1,1) primary key,
    primer_nombre varchar(10),
    segundo_nombre varchar(10),
    apellido_paterno varchar(10),
    apellido_materno varchar(10),
    direccion varchar(100),
    correo_electronico varchar(50),
    telefono varchar(10)
)
GO
-----GRADO-----------------------------------------------------------------
create table grado(
    id_grado int identity (1,1) primary key,
    nGrado varchar(20),
    aula varchar(20),
    ubicacion varchar(50),
    descripcion varchar(50)
)
GO
-----CARGO----------------------------------------------------------------
create table cargo(
    id_cargo int identity (1,1) primary key,
    ncargo varchar(30),
    descripcion varchar(100)
)
GO
-----ESTADO---------------------------------------------------------------
create table estado(
    id_estado int identity (1,1) primary key,
    nEstado varchar(20),
    descripcion varchar(100)
)
GO
-----EMPLEADO-------------------------------------------------------------
create table empleado(
	id_empleado int identity (1,1) primary key,
    id_persona int,
	id_cargo int
	foreign key (id_persona) references persona(id_persona),
	foreign key (id_cargo) references cargo(id_cargo)
)
GO
-----MATERIA--------------------------------------------------------------
create table materia(
	id_materia int identity (1,1) primary key,
    id_empleado int,
    nMateria varchar(20),
    Descripcion varchar(100)
	foreign key (id_empleado) references empleado(id_empleado)
)
GO
-----ESTUDIANTE-----------------------------------------------------------
create table estudiante(
    -- id_estudiante int identity (1,1) primary key,
    id_estudiante int primary key,
    id_grado int,
	carnet varchar(15),
	primer_nombre varchar(10),
    segundo_nombre varchar(10),
    apellido_paterno varchar(10),
    apellido_materno varchar(10),
    correo_electronico varchar(50),
	foreign key (id_grado) references grado(id_grado)
)
GO
-----MATRICULA-------------------------------------------------------------
create table matricula(
    id_matricula int identity (1,1) primary key,
    id_estado int
	foreign key (id_estado) references estado(id_estado)
)
GO
alter table estudiante
add constraint fk_id_estudiante
foreign key (id_estudiante)
references matricula(id_matricula)
GO
-----INSCRIPCION-----------------------------------------------------------
create table inscripcion(
	id_inscripcion int identity (1,1) primary key,
    id_matricula int,
    id_materia int,
    horario varchar(15)
	foreign key (id_matricula) references matricula(id_matricula),
	foreign key (id_materia) references materia(id_materia)
)
GO
-----PADRES DE FAMILIA-----------------------------------------------------
create table padres_estudiantes(
	id_padres int identity (1,1) primary key,
    id_persona int,
    id_estudiante int
	foreign key (id_persona) references persona(id_persona),
	foreign key (id_estudiante) references estudiante(id_estudiante)
)
GO
-----CALIFICACIONES--------------------------------------------------------
create table calificaciones(
	id_calificaciones int identity (1,1) primary key,
    id_materia int,
    id_estudiante int,
	nMes varchar(15),
	n_actividades numeric(4,2),
	n_laboratorio numeric(4,2),
	n_examen numeric(4,2),
	n_prom_final numeric(4,2)
	foreign key (id_materia) references materia(id_materia),
	foreign key (id_estudiante) references estudiante(id_estudiante)
)
