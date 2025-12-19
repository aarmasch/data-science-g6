-- FILTROS
SELECT * FROM empleado WHERE pais = 'Peru';

SELECT * FROM empleado WHERE salario > 5000;

SELECT * FROM empleado WHERE salario > 5000 AND pais = 'Peru';

SELECT * FROM empleado WHERE salario > 5000 AND (pais = 'Peru' OR pais = 'Colombia');

SELECT * FROM empleado WHERE pais in ('Chile', 'Argentina');

SELECT * FROM empleado WHERE salario BETWEEN 10000 AND 15000;