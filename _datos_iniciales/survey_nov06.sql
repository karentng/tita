INSERT INTO "survey_survey" ("id", "name", "description") VALUES
(4,	'Encuesta a nuevos estudiantes',	':-o');
INSERT INTO "survey_question" ("id", "number", "text", "required", "category_id", "survey_id", "question_type", "choices") VALUES
(394,	'01',	'Jornada en la que estudias:',	't',	NULL,	4,	'select',	'Mañana
Tarde'),
(395,	'02',	'Nombre de tu institución educativa:',	't',	NULL,	4,	'select',	'INEM JORGE ISAACS
CECILIA MUÑOZ RICAURTE
LAS AMERICAS
CAMILO TORRES
CENTRO EDUCATIVO DEL NORTE
FRAY DOMINGO DE LAS CASAS
PABLO EMILIO
ANTONIO JOSE CAMACHO
REPUBLICA DEL PERU
MARCO FIDEL SUAREZ
OLGA LUCIA LLOREDA
NORMAL SUPERIOR FARALLONES DE CALI
JOAQUIN DE CAYZEDO Y CUERO
GOLONDRINAS
ANTONIO BARBERENA
CARLOS HOLGUIN MALLARINO
NIÑO JESUS DE ATOCHA
MIGUEL DE POMBO
MANUEL MARIA MALLARINO
LAURA VICUÑA
LOS PINOS
CARLOS HOLGUIN SARDI
EL DIAMANTE
JUAN PABLO II
EUSTAQUIO PALACIOS
LUIS LOPEZ MESA
CELANESE
MANUEL MARIA BUENAVENTURA
MARISCAL JORGE ROBLEDO
MIGUEL ANTONIO CARO
GENERAL ANZOATEGUI
TULIO ENRIQUE TASCON
SANTIAGO RENGIFO
SOFIA CAMARGO
JOSE MARIA CARBONELL
HONORIO VILLEGAS
IE BOYACA
MARICE SINISTERRA
FENALCO ASTURIAS
VIJES
LICEO DEPARTAMENTAL
IETI COMUNA 17
CELMIRA BUENO DE OREJUELA'),
(396,	'03',	'Tus nombre(s) y apellidos: ',	't',	NULL,	4,	'text',	''),
(397,	'04',	'Curso en el que estás: ',	't',	NULL,	4,	'text',	''),
(398,	'05',	'Edad: 
',	't',	NULL,	4,	'text',	''),
(399,	'0601',	'Día',	't',	NULL,	4,	'select',	'1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31'),
(400,	'0602',	'Mes',	't',	NULL,	4,	'select',	'Enero
Febrero
Marzo
Abril
Mayo
Junio
Julio
Agosto
Septiembre
Octubre
Noviembre
Diciembre'),
(401,	'0603',	'Año',	't',	NULL,	4,	'select',	'1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010'),
(402,	'07',	'¿En qué ciudad naciste?',	't',	NULL,	4,	'text',	''),
(403,	'08',	'Actualmente ¿en qué barrio vives?',	't',	NULL,	4,	'text',	''),
(404,	'09',	'1. Actualmente ¿con qué frecuencia utilizas el computador? Marca sólo una respuesta. ',	't',	NULL,	4,	'radio',	'De 4 a 7 días a la semana.  
De 2 a 3 días a la semana.
1 día a la semana. 
Casi nunca.
Nunca. '),
(405,	'10',	'2. Actualmente ¿con qué frecuencia te conectas a Internet? Marca sólo una respuesta. 
',	't',	NULL,	4,	'radio',	'De 4 a 7 días a la semana.
De 2 a 3 días a la semana.
1 día a la semana. 
Casi nunca.
Nunca. '),
(406,	'1101',	'Encuentras información interesante que no conocías.													',	't',	NULL,	4,	'select',	'Definitivamente sí
A veces		
Nunca me pasa eso'),
(407,	'1102',	'Aprendes cosas que no te habían enseñado en las clases. ',	't',	NULL,	4,	'select',	'Definitivamente sí
A veces		
Nunca me pasa eso'),
(408,	'1103',	'Terminas haciendo cosas que no tienen que ver con la tarea.											',	't',	NULL,	4,	'select',	'Definitivamente sí
A veces		
Nunca me pasa eso'),
(409,	'12',	'4.  ¿Cómo crees que serían tus clases si se utilizara Internet? Puedes marcar varias opciones.',	't',	NULL,	4,	'select-multiple',	'Serían más interesantes.
Le entenderías más al profesor.
Daría lo mismo.
Sería más difícil aprender.
Me distraería con más facilidad.'),
(410,	'1301',	'Matemáticas - Física
',	't',	NULL,	4,	'select',	'1
2
3'),
(411,	'1302',	'Inglés
',	't',	NULL,	4,	'select',	'1
2
3'),
(412,	'1303',	'Tecnología e Informàtica
',	't',	NULL,	4,	'select',	'1
2
3'),
(413,	'1304',	'Ciencias Sociales - Filosofía
',	't',	NULL,	4,	'select',	'1
2
3'),
(414,	'1305',	'Biología - Química
',	't',	NULL,	4,	'select',	'1
2
3'),
(415,	'1306',	'Educación Física
',	't',	NULL,	4,	'select',	'1
2
3'),
(416,	'1307',	'Lengua Castellana
',	't',	NULL,	4,	'select',	'1
2
3'),
(417,	'1308',	'Artes
',	't',	NULL,	4,	'select',	'1
2
3'),
(418,	'14',	'6. Para tus clases y hacer las tareas ¿qué programas informáticos usas? Puedes marcar varias opciones.',	't',	NULL,	4,	'select-multiple',	'Procesador de texto (Ejemplo: Word, Apache OpenOffice Writer, LibreOffice Writer).
Hoja de cálculo (Ejemplo: Excel, Apache OpenOffice Calc, LibreOffice Calc, StartOffice Calc).
Programas para hacer presentaciones (Ejemplo: Power Point, Prezi, Apache OpenOffice Impress).
Programas de dibujo (Ejemplo: Corel Draw, Adobe Flash, Microsoft Paint).
Programas para editar imágenes y fotografías (Ejemplo: Adobe Photoshop, GIMP).
Ninguno. '),
(419,	'1501',	'Enciclopedias o diccionarios digitales como ENCARTA. 											
										',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(420,	'1502',	'Revistas y periódicos en Internet. 											',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(421,	'1503',	'Sitios de consulta como Wikipedia. 											',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(422,	'1504',	'Sitios de tareas como el Rincón del Vago. 											',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(423,	'1505',	'Videos en You Tube. 											
',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(424,	'1506',	'Cursos en Internet. 										',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(425,	'1507',	'Plataforma virtual de aprendizaje como Moodle, Blackboard, Atutor, etc.	',	't',	NULL,	4,	'select',	'Siempre
A veces
Nunca'),
(426,	'16',	'8. ¿En qué sitios te conectas a Internet? Puedes marcar varias opciones.',	'f',	NULL,	4,	'select-multiple',	'En tu casa.
En la casa de tus amigos o familiares.
En tu colegio.
En un lugar de acceso público gratuito.  
En un lugar de acceso público con costo como un café Internet. 
En cualquier parte a través de Internet móvil.'),
(427,	'1701',	'Computador		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(428,	'170101',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(429,	'1702',	'Internet		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(430,	'170201',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(431,	'1703',	'Tablet		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(432,	'170301',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(433,	'1704',	'Celular		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(434,	'170401',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(435,	'1705',	'Videojuegos		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(436,	'170501',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(437,	'1706',	'Cámara fotográfica digital		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(438,	'170601',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(439,	'1707',	'Cámara de video		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(440,	'170701',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(441,	'1708',	'Grabadora digital		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(442,	'170801',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(443,	'1709',	'DVD/Blue-ray		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(444,	'170901',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(445,	'1720',	'Televisor		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(446,	'172001',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(447,	'1721',	'Radio		
',	't',	NULL,	4,	'select-multiple',	'Me ayuda a pasar el tiempo
Me permite registrar momentos
Me informa
Me enseña
Me permite conocer otros países, otras culturas
Me comunico con amigos y otras personas
No lo uso
No tengo'),
(448,	'172101',	'Lo uso para otra cosa. Dinos ¿cuál?',	'f',	NULL,	4,	'text',	''),
(449,	'1722',	'Otro dispositivo. ¿Cuál?',	'f',	NULL,	4,	'text',	''),
(454,	'18',	'10. ¿A qué redes sociales perteneces? Puedes marcar varias opciones.  					',	'f',	NULL,	4,	'select-multiple',	'Instagram 
You Tube
Google+
WhatsApp'),
(523,	'1801',	'Otra. ¿Cuál?',	'f',	NULL,	4,	'text',	''),
(455,	'19',	'11 ¿Con quién compartes la información que encuentras en Internet? Puedes marcar varias opciones. ',	't',	NULL,	4,	'select-multiple',	'Con tus padres. 
Con tus hermanos.
Con tus amigos.
Con tus profesores.
Con tus compañeros de estudio. 
Con nadie. '),
(456,	'20',	'12. ¿Con quién aprendes a usar el computador y la Internet? Puedes marcar varias opciones.',	't',	NULL,	4,	'select-multiple',	'Solo, cacharreando o averiguando en Internet. 
Con tus padres. 
Con tus hermanos.
Con tus amigos. 
Con tus profesores.
Con tus compañeros de estudio. 
Haciendo cursos.'),
(457,	'2001',	'¿Cuáles?
',	'f',	NULL,	4,	'text',	''),
(458,	'21',	'13. Cuando usas Internet ¿con quién prefieres hacerlo? Marca con sólo una respuesta. 
',	't',	NULL,	4,	'radio',	'Solo. 
Con tus padres o tus profesores. 
Con tus hermanos, amigos o compañeros de estudio.'),
(459,	'22',	'14. ¿Qué te gustaría hacer o aprender a hacer con Internet? Puedes marcar varias opciones.',	'f',	NULL,	4,	'select-multiple',	'Desarrollar programas informáticos.												
Construir páginas web.											
Crear videos y películas.											
Crear mejores fotografías.												
Escribir historias y cuentos.											
Hacer un video y subirlo a You Tube.												
Diseñar un videojuego.											
Construir un blog, un diario, un periódico, un programa de radio y música.												
Aprender un idioma que no conozco.											
Hacer amigos de mi edad.											
Componer música utilizando software especializado.
Intercambiar objetos.												
Vender o comprar creaciones propias (música, dibujos, cuentos, imágenes, artes).'),
(460,	'2201',	'Otra cosa. ¿Cuál?',	'f',	NULL,	4,	'text',	''),
(461,	'2301',	'Primer Dispositivo que Lamentaría',	't',	NULL,	4,	'select',	'Celular.
Computador. 
Tablet. 
Conexión a Internet.
DVD o Blue-ray.
Radio. 
Televisor. 
Video beam.'),
(462,	'2302',	'Segundo Dispositivo que Lamentaría',	't',	NULL,	4,	'select',	'Celular.
Computador. 
Tablet. 
Conexión a Internet.
DVD o Blue-ray.
Radio. 
Televisor. 
Video beam.'),
(463,	'2303',	'Tercer Dispositivo que Lamentaría',	't',	NULL,	4,	'select',	'Celular.
Computador. 
Tablet. 
Conexión a Internet.
DVD o Blue-ray.
Radio. 
Televisor. 
Video beam.'),
(464,	'24',	'16. Suponiendo que el escenario descrito al inicio es real, ¿qué crees que sucedería con el desempeño y el comportamiento de tus compañeros en clase? Marca sólo una respuesta.														',	't',	NULL,	4,	'radio',	'No creo que el desempeño escolar y el comportamiento de los estudiantes cambien mucho.
Creo que el desempeño escolar  puede mejorar, pero el comportamiento (atención, concentración, disciplina) puede deteriorarse.	
Creo que el desempeño escolar no necesariamente mejorará, pero el comportamiento (atención, concentración, disciplina) puede mejorar.
Creo que el desempeño escolar y el comportamiento de los estudiantes pueden mejorar mucho.'),
(465,	'25',	'17. Suponiendo que el escenario descrito al inicio es real, ¿qué crees que sucedería con la comunicación entre los padres de familia y la institución educativa? Marca sólo una respuesta.																					',	't',	NULL,	4,	'radio',	'Creo que habrá una comunicación más fluida y continua con los padres de familia, ellos estarán mejor enterados de lo que pasa con nosotros.
No creo que esto cambie mucho. Los padres y acudientes interesados en sus hijos mantienen comunicación constante con los profesores, con o sin un programa de computador que sirva para ello. Los que no están interesados no cambiarán, aunque tengan el un programa de computador para comunicarse con la institución educativa.
Un programa de computador que sirva para que los padres de familia se comuniquen con la institución educativa, permitirá que ellos estén al tanto del desempeño escolar de nosotros y muy probablemente eso implicará para los docentes mayor dedicación de tiempo para responder a  un número creciente de consultas de los padres.
Esto no va a funcionar porque los padres no están capacitados para manejar este tipo de programas o no cuentan con la dotación tecnológica necesaria para aprovecharlos.'),
(466,	'26',	'18. ¿Te gustó responder esta encuesta en computador?   
',	't',	NULL,	4,	'radio',	'Sí
No
Es igual a si la hubiese respondido en papel');
