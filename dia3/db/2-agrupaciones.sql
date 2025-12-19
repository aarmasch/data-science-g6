USE db_g6;

--FUNCIONES DE AGRUPACION
SELECT MAX(salario) FROM empleado;
SELECT MIN(salario) FROM empleado;
SELECT AVG(salario) FROM empleado;

SELECT MAX(salario), MIN(salario), AVG(salario) FROM empleado;

SELECT DISTINCT pais FROM empleado;

--SELECCIONAR EL TOTAL DE EMPLEADOS POR PAIS
SELECT pais, COUNT(*) FROM empleado GROUP BY pais ORDER BY COUNT(*) DESC;

SELECT pais, area, COUNT(*), MAX(salario), MIN(salario), AVG(salario) FROM empleado WHERE salario > 5000 GROUP BY pais, area ORDER BY pais, area;

SELECT pais, COUNT(*) FROM empleado GROUP BY pais HAVING COUNT(*) > 100;