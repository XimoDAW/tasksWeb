USE tasks;

INSERT INTO status VALUES(1, 'Pendiente');
INSERT INTO status VALUES(2, 'Finalizada');
INSERT INTO status VALUES(3, 'Fuera de plazo');

INSERT INTO posit VALUES (1, 'Escuela');
INSERT INTO management VALUES (1);


INSERT INTO task VALUES (1, 'Ejercicio de programacion', 'Recorrer una lista mediante un bucle for', 1, 1, NOW(), '2024-06-10');
INSERT INTO task_status VALUES (1, 1, 1);