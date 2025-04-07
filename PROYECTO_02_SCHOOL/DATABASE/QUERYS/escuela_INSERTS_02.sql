USE escuela --DATOS GENERADOS CON IA-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------ESTADO--------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO estado (nEstado, descripcion) VALUES
('Matriculado', 'Estudiante inscrito formalmente en el sistema escolar'),
('No Matriculado', 'Estudiante no registrado en el sistema escolar'),
('Aprobado', 'Estudiante que ha cumplido con los requisitos académicos'),
('Reprobado', 'Estudiante que no alcanzó los objetivos del curso'),
('Activo', 'Estado de actividad regular en el sistema escolar'),
('Inactivo', 'Estudiante que no está participando actualmente en el sistema'),
('Enfermo', 'Estudiante con condición médica temporal o permanente'),
('Pendiente', 'Estado en espera de confirmación o decisión final');
GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------EMPLEADO------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO empleado (id_persona, id_cargo) VALUES
-- Maestros asignados por grado 
(153, 3), -- Maestro de Matemáticas
(97, 4), -- Maestro de Ciencias
(162, 5), -- Maestro de Sociales
(45, 6), -- Maestro de Lenguaje
(89, 7), -- Maestro de Inglés

(102, 3), -- Maestro de Matemáticas
(171, 4), -- Maestro de Ciencias
(15, 5), -- Maestro de Sociales
(74, 6), -- Maestro de Lenguaje
(193, 7), -- Maestro de Inglés

(34, 3), -- Maestro de Matemáticas
(118, 4), -- Maestro de Ciencias
(56, 5), -- Maestro de Sociales
(190, 6), -- Maestro de Lenguaje
(79, 7), -- Maestro de Inglés

-- Maestros de otras asignaturas o talleres
(94, 19), -- Maestro de Arte
(200, 20), -- Maestro de Historia
(48, 21), -- Maestro de Educación Física
(101, 22), -- Maestro de Idiomas (Francés)
(176, 23), -- Maestro de Tecnología
(142, 15), -- Maestro Ciencias Naturales

(25, 19), -- Maestro de Arte
(154, 20), -- Maestro de Historia
(71, 21), -- Maestro de Educación Física
(199, 22), -- Maestro de Idiomas (Francés)
(140, 23), -- Maestro de Tecnología
(69, 15), -- Maestro Ciencias Naturales

(81, 19), -- Maestro de Arte
(27, 20), -- Maestro de Historia
(107, 21), -- Maestro de Educación Física
(116, 22), -- Maestro de Idiomas (Francés)
(52, 23), -- Maestro de Tecnología

-- Personal administrativo 
(120, 1), -- Director
(64, 2), -- Subdirector
(11, 9), -- Secretario
(88, 10), -- Tesorero
(43, 17), -- Coordinador académico
(143, 16), -- Técnico Informático
(198, 11), -- Encargado de Ornato
(157, 12), -- Conserje
(29, 13), -- Vigilante
(66, 14), -- Enfermero

--- Personal administrativo adicional
(3, 11), -- Encargado de Ornato
(109, 12), -- Conserje
(163, 13), -- Vigilante
(75, 14), -- Enfermero
(192, 31), -- Operador de Equipo
(96, 8), -- Bibliotecario
(59, 33), -- Encargado de Laboratorio
(130, 34), -- Contador
(182, 35), -- Encargado de Inventario
(20, 36), -- Recepcionista
(169, 49), -- Ayudante de Cocina
(50, 38), -- Auxiliar de Enfermería
(147, 39), -- Asistente Técnico
(1, 48), -- Cocinera(o)
(37, 13), -- Vigilante
(110, 11), -- Encargado de Ornato
(77, 14), -- Enfermero
(91, 13), -- Vigilante
(124, 11), -- Encargado de Ornato

(6, 49), -- Ayudante de Cocina
(123, 38), -- Auxiliar de Enfermería
(26, 49), -- Ayudante de Cocina
(188, 49); -- Ayudante de Cocina
GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------MATERIA-------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO materia (id_empleado, nMateria, Descripcion) VALUES
-- Asignación de materias básicas
(6, 'Matemáticas', 'Estudio de conceptos matemáticos y numéricos'),
(7, 'Ciencias', 'Exploración de fenómenos naturales y físicos'),
(8, 'Sociales', 'Análisis de historia y organización social'),
(9, 'Lenguaje', 'Habilidades de lectura, escritura y expresión oral'),
(10, 'Inglés', 'Estudio del idioma inglés y su gramática'),

(11, 'Matemáticas', 'Resolución de problemas matemáticos y álgebra'),
(12, 'Ciencias', 'Estudio de biología y química básica'),
(13, 'Sociales', 'Temas históricos y geográficos'),
(14, 'Lenguaje', 'Fomentar la comunicación oral y escrita'),
(15, 'Inglés', 'Desarrollo de habilidades en inglés'),

(1, 'Matemáticas', 'Álgebra, geometría y cálculo'),
(2, 'Ciencias', 'Física, electrónica y anatomía general'),
(3, 'Sociales', 'Análisis histórico-social'),
(4, 'Lenguaje', 'Enseñanza avanzada de escritura y gramática'),
(5, 'Inglés', 'Práctica del idioma inglés en comunicación'),

-- Asignación de materias adicionales
(26, 'Arte', 'Desarrollo de la creatividad y técnicas artísticas'),
(27, 'Historia', 'Estudio de historia universal y local'),
(28, 'Educación Física', 'Promoción de la actividad física y el deporte'),
(29, 'Francés', 'Introducción al idioma francés y cultura'),
(30, 'Tecnología', 'Uso de herramientas tecnológicas y digitales'),
(31, 'Ciencias Nat.', 'Física, química y biología integradas'),

(37, 'Arte', 'Prácticas artísticas y expresión visual'),
(33, 'Historia', 'Aprendizaje histórico-social'),
(34, 'Educación Física', 'Desarrollo físico y deportivo'),
(40, 'Francés', 'Gramática y comunicación en francés'),
(36, 'Tecnología', 'Educación en informática y sistemas digitales'),
(65, 'Ciencias Nat.', 'Física, química y biología integradas'),

(26, 'Arte', 'Diseño y técnicas visuales en arte'),
(38, 'Historia', 'Estudio crítico de eventos históricos'),
(39, 'Educación Física', 'Fomento de hábitos físicos saludables'),
(35, 'Francés', 'Enseñanza práctica del idioma francés'),
(41, 'Tecnología', 'Habilidades avanzadas en informática y tecnología');
GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

GO
-------------------------------------------------------------------------------------------------------------------------------------------------------------

