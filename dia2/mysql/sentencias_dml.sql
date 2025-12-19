-- SENTENCIAS DML
-- CRUD
-- C - INSERT
-- R - SELECT
-- U - UPDATE
-- D - DELETE

--INSERT
INSERT INTO alumno(nro_documento, nombre) VALUES('100','Adriano Armas');

--INSERTAR VARIOS REGISTROS
INSERT INTO alumno(nro_documento, nombre)
VALUES
('200','Beatriz Lopez'),
('300','Carlos Perez'),
('400','Diana Gomez'),
('500','Monica Tejada'),
('600','Raul Rivera'),
('700','Andrea Valencia'),
('800','Sofia Mamani'),
('900','Carlos Perez'),
('1000','Jesus Concha');

-- ACTUALIZAR REGISTRO
UPDATE alumno SET
email = 'codigo@gmail.com'

-- UPDATE CON WHERE
UPDATE alumno SET email = 'aarmas@gmail.com' WHERE id = 1;

UPDATE alumno 
SET email = CONCAT(LOWER(REPLACE(nombre,' ','')),'@gmail.com') WHERE id > 1;

-- SELECT
SELECT * FROM alumno;

SELECT nombre, email FROM alumno;

SELECT nombre FROM alumno WHERE id > 5;

SELECT * FROM alumno ORDER BY nombre ASC;

--DELETE
DELETE FROM alumno WHERE id = 10;

--TRUNCATE -- elimina definitivamente todos los registros de una tabla
TRUNCATE TABLE alumno;