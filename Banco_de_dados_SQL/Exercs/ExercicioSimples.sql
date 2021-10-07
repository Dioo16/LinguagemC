CREATE DATABASE LIVRARIA;
USE LIVRARIA;

CREATE TABLE LIVROS(
	NOMEL VARCHAR(30),
	NOMEA VARCHAR(30),
	SEXO CHAR(1),
	PAG VARCHAR(10000),
	NOMEE VARCHAR (200),
	VALOR VARCHAR(1000),
	EST CHAR(2),
	ANO INT(4)
);

INSERT INTO LIVROS(NOMEL,NOMEA,SEXO,PAG,NOMEE,VALOR,EST,ANO)VALUES('CAVALEIRO REAL','Ana Claudia','F','465','Atlas','49.9','RJ','2009'),
																  ('SQL PARA LEIGOS','JOÃO NUNES','M','450','ADDISON','98','SP','2018'),
																  ('RECEITAS CASEIRAS','CELIA TAVARES','F','210','Atlas','45','RJ','2008'),
																  ('PESSOAS EFETIVAS','EDUARDO SANTOS','M','390','BETA','78.99','RJ','2018'),
																  ('HABITOS SAUDÁVEIS','EDURADO SANTOS','M','630','BETA','150,98','RJ','2019'),
																  ('A CASA MARROM','HERMES MACEDO','M','250','BUBBA','60','MG','2016'),
																  ('ESTACIO QUERIDO','GERALDO FRANCISCO','M','310', 'INSIGNIA','100','ES','2011'),
																  ('PRA SEMPRE AMIGAS','LEDA SILVA','F','510','INSIGNIA', '78.98','ES','2011'),
																  ('COPAS INESQUECIVEIS','MARCOS ALCANTARA','M','200', 'LARSON', '130.98','RS','2018'),
																  ('O PODER DA MENTE','CLARA MAFRA','F','120','CONTINENTAL', '56.58','SP','2017')
																  
																                                                            
																															
SELECT NOMEL, EST FROM LIVROS WHERE EST = 'SP';
SELECT NOMEL, PAG FROM LIVROS WHERE SEXO = 'F';

SELECT NOMEA, SEXO FROM LIVROS WHERE SEXO = 'M' AND EST = 'SP' OR EST = 'RJ';
