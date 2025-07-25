import mysql.connector
import random

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306",
    database = "automenu"
)

#print(conn)

cursor = conn.cursor()

#################################################################################################################################################################################

""" CREACIÓN DE BASE DE DATOS """

#dbCreation = """CREATE DATABASE AutoMenu"""
#cursor.execute(dbCreation)

#################################################################################################################################################################################

""" CREACIÓN DE TABLAS """
#tipos_Ingredientes = """CREATE TABLE Tipos_Ingredientes (id_Tipo_Ingrediente INT AUTO_INCREMENT PRIMARY KEY, nombre_Tipo_Ingrediente VARCHAR (255))"""
#cursor.execute(tipos_Ingredientes)

#ingredientes = """CREATE TABLE Ingredientes (id_Ingrediente INT AUTO_INCREMENT PRIMARY KEY, nombre_Ingrediente VARCHAR (255), unidad_Ingrediente VARCHAR (20), porcion_Ingrediente DECIMAL(6,2), 
#id_Tipo_Ingrediente INT, FOREIGN KEY (id_Tipo_Ingrediente) REFERENCES Tipos_Ingredientes(id_Tipo_Ingrediente))"""
#cursor.execute(ingredientes)

#platillos = """CREATE TABLE Platillos (id_Platillo INT AUTO_INCREMENT PRIMARY KEY, nombre_Platillo VARCHAR (255), descripcion_Platillo VARCHAR (225))"""
#cursor.execute(platillos)

#platillos_Ingredientes = """CREATE TABLE platillos_ingredientes (id_platillos_ingredientes INT AUTO_INCREMENT PRIMARY KEY, cantidad DECIMAL(5,2), id_Platillo INT, id_Ingrediente INT, 
#FOREIGN KEY (id_Platillo) REFERENCES Platillos (id_Platillo), FOREIGN KEY (id_Ingrediente) REFERENCES Ingredientes (id_Ingrediente))"""
#cursor.execute(platillos_Ingredientes)

#dias = """CREATE TABLE dias (id_Dia INT AUTO_INCREMENT PRIMARY KEY, dia VARCHAR (30))"""
#cursor.execute(dias)

#tipos_Comida = """CREATE TABLE tipos_Comida (id_Tipos_Comida INT AUTO_INCREMENT PRIMARY KEY, nombre_Tipo VARCHAR (30))"""
#cursor.execute(tipos_Comida)

#menus = """CREATE TABLE menus (id_Menu INT AUTO_INCREMENT PRIMARY KEY, id_Platillo INT, id_Dia INT, id_Tipos_Comida INT, 
#FOREIGN KEY (id_Platillo) REFERENCES Platillos (id_Platillo), 
#FOREIGN KEY (id_Dia) REFERENCES dias (id_Dia), 
#FOREIGN KEY(id_Tipos_Comida) REFERENCES tipos_Comida(id_Tipos_Comida))"""
#cursor.execute(menus)

# eh = """CREATE TABLE Ingredientes_Usados (
#   id_Registro INT AUTO_INCREMENT PRIMARY KEY,
#   fecha DATE NOT NULL,
#   momento VARCHAR(50) NOT NULL,
#   nombre_Ingrediente VARCHAR(255) NOT NULL
# );
# """
# cursor.execute(eh)

#################################################################################################################################################################################

"""INSERCIÓN DE TIPO_INGREDIENTES"""

#tipos = [
#    'Vegetales',
#    'Origen Animal',
#    'Leguminosas',
#    'Frutas',
#    'Cereales',
#    'Aceites y grasas',
#    'Lacteos',
#    'Grasas con proteina',
#    'Azucar'
#]
#
#query = "INSERT INTO Tipos_Ingredientes (nombre_Tipo_Ingrediente) VALUES (%s)"
#cursor.executemany(query, [(tipo,) for tipo in tipos])

"""INSERCIÓN DE LOS INGREDIENTS"""

"""Vegetales"""
#vegetales = [
#    ('Acelga cruda', 'taza', 2.00),
#    ('Acelga cocida', 'taza', 0.50),
#    ('Betabel crudo', 'pieza', 0.75),
#    ('Brócoli cocido', 'taza', 0.50),
#    ('Calabacita cocida', 'taza', 0.50),
#    ('Champiñón cocido rebanado', 'taza', 1.50),
#    ('Chayote cocido picado', 'taza', 0.50),
#    ('Chile poblano', 'pieza', 1.00),
#    ('Col cocida picada', 'taza', 0.50),
#    ('Coliflor cocida', 'taza', 0.50),
#    ('Ejotes cocidos picados', 'taza', 0.50),
#    ('Elotitos cambray', 'pieza', 8.00),
#    ('Espárragos', 'pieza', 6.00),
#    ('Espinaca cocida', 'taza', 0.50),
#    ('Espinaca cruda picada', 'taza', 1.00),
#    ('Flor de calabaza cocida', 'taza', 0.50),
#    ('Germen de alfalfa', 'taza', 3.00),
#    ('Hongos crudos', 'taza', 1.00),
#    ('Huazontle', 'taza', 1.00),
#    ('Huitlacoche cocido', 'taza', 0.50),
#    ('Jícama picada', 'taza', 0.50),
#    ('Jitomate bola', 'pieza', 1.00),
#    ('Jitomate cherry', 'pieza', 8.00),
#    ('Lechuga', 'taza', 1.00),
#    ('Zanahoria', 'taza', 1.00),
#    ('Nopal cocido', 'taza', 0.50),
#    ('Nopal crudo', 'pieza', 2.00),
#    ('Pepino con cáscara', 'taza', 1.00),
#    ('Pimiento morrón cocido', 'taza', 0.50),
#    ('Setas cocidas', 'taza', 0.50),
#    ('Verdolaga cocida', 'taza', 0.50),
#    ('Zanahoria miniatura', 'pieza', 3.00),
#    ('Zanahoria rallada cruda', 'taza', 0.33)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 1) for nombre, unidad, porcion in vegetales])

"""Origen Animal"""
#origen_animal = [
#    ('Atún', 'lata', 0.50),
#    ('Atún fresco', 'g', 30),
#    ('Bistec (res/cerdo)', 'g', 30),
#    ('Bola de ternera', 'g', 35),
#    ('Camarón cocido', 'pieza', 5),
#    ('Camarón gigante', 'pieza', 2),
#    ('Carne de res seca', 'g', 11),
#    ('Cecina', 'g', 25),
#    ('Huevo', 'pieza', 1),
#    ('Claras de huevo', 'pieza', 2),
#    ('Filete de pescado', 'g', 40),
#    ('Filete de res', 'g', 30),
#    ('Filete miñón', 'g', 30),
#    ('Jamón', 'rebanada', 2),
#    ('Milanesa de res', 'g', 30),
#    ('Pierna de pollo sin piel', 'pieza', 1),
#    ('Pechuga de pollo', 'g', 30),
#    ('Pulpo cocido', 'g', 25),
#    ('Quesillo', 'g', 30),
#    ('Queso cottage', 'cucharada', 3),
#    ('Queso panela', 'g', 40),
#    ('Requesón', 'cucharada', 3),
#    ('Salmón ahumado', 'g', 35),
#    ('Surimi', 'barra', 0.67)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 2) for nombre, unidad, porcion in origen_animal])

"""Leguminosas"""
#leguminosas = [
#    ('Alverjón cocido', 'taza', 0.50),
#    ('Chícharo cocido', 'taza', 0.50),
#    ('Frijol cocido', 'taza', 0.50),
#    ('Garbanzo cocido', 'taza', 0.50),
#    ('Haba seca cocida', 'taza', 0.50),
#    ('Hummus', 'cucharada', 5.00),
#    ('Lentejas cocidas', 'taza', 0.50),
#    ('Soya cocida', 'taza', 0.50)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 3) for nombre, unidad, porcion in leguminosas])

"""Frutas"""
#frutas = [
#    ('Agua de coco', 'taza', 1.50),
#    ('Arándano fresco', 'g', 125),
#    ('Blueberries', 'taza', 0.75),
#    ('Cereza', 'pieza', 20),
#    ('Ciruela', 'pieza', 3),
#    ('Dátil seco', 'pieza', 2),
#    ('Durazno', 'pieza', 2),
#    ('Frambuesa', 'taza', 1.00),
#    ('Fresa rebanada', 'taza', 1.00),
#    ('Guayaba', 'pieza', 3),
#    ('Higo', 'pieza', 2),
#    ('Jugo de naranja natural', 'taza', 0.50),
#    ('Kiwi', 'pieza', 1),
#    ('Lichis', 'pieza', 12),
#    ('Mamey', 'pieza', 0.33),
#    ('Mandarina', 'pieza', 2),
#    ('Mango manila', 'pieza', 1),
#    ('Mango petacón', 'pieza', 1),
#    ('Manzana', 'pieza', 1),
#    ('Maracuyá', 'pieza', 1),
#    ('Melón picado', 'taza', 1.00),
#    ('Moras', 'taza', 1.00),
#    ('Naranja', 'pieza', 2),
#    ('Nectarina', 'pieza', 1),
#    ('Papaya picada', 'taza', 1.00),
#    ('Pasitas', 'pieza', 10),
#    ('Pera', 'pieza', 0.50),
#    ('Piña', 'rebanada', 1),
#    ('Plátano', 'pieza', 1),
#    ('Sandía', 'taza', 1.00),
#    ('Toronja', 'pieza', 1),
#    ('Tuna', 'pieza', 3),
#    ('Uva', 'pieza', 10),
#    ('Zapote negro', 'pieza', 1),
#    ('Zarzamora', 'taza', 1.00)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 4) for nombre, unidad, porcion in frutas])

"""Cereales"""
#cereales = [
#    ('Alegría natural', 'cucharadita', 5),
#    ('Arroz cocido', 'taza', 0.50),
#    ('Avena cocida', 'taza', 0.75),
#    ('Avena en hojuelas', 'taza', 0.50),
#    ('Bísquet', 'pieza', 0.50),
#    ('Bagel', 'pieza', 0.33),
#    ('Bolillo', 'pieza', 0.50),
#    ('Camote cocido', 'taza', 0.33),
#    ('Crotones', 'taza', 0.75),
#    ('Elote blanco desgranado', 'taza', 0.50),
#    ('Espagueti', 'taza', 0.50),
#    ('Fécula de maíz', 'cucharada', 2),
#    ('Galletas de animalito', 'pieza', 6),
#    ('Galletas maría', 'pieza', 5),
#    ('Galletas de maíz horneadas (salmas)', 'pieza', 3),
#    ('Galletas habaneras', 'pieza', 4),
#    ('Hot-cake', 'pieza', 1),
#    ('Maíz palomero', 'g', 20),
#    ('Maíz pozolero', 'taza', 0.50),
#    ('Pambazo', 'pieza', 0.50),
#    ('Palomitas naturales', 'taza', 2.50),
#    ('Pan de caja', 'rebanada', 1),
#    ('Pan tostado', 'rebanada', 1),
#    ('Papa cocida', 'taza', 0.50),
#    ('Pasta cocida', 'taza', 0.50),
#    ('Puré de papa', 'taza', 0.33),
#    ('Tapioca', 'cucharada', 2),
#    ('Tortilla de maíz', 'pieza', 1),
#    ('Tortilla de harina', 'pieza', 0.50),
#    ('Tostada de maíz horneada', 'pieza', 2)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 5) for nombre, unidad, porcion in cereales])

"""Aceites y Grasas"""
#aceites_grasas = [
#    ('Aceite', 'cucharadita', 1),
#    ('Aceitunas', 'pieza', 5),
#    ('Aderezo tipo césar', 'cucharada', 0.50),
#    ('Aderezo de miel y mostaza', 'cucharada', 0.50),
#    ('Aderezo italiano', 'cucharada', 0.50),
#    ('Calahua', 'cucharada', 1),
#    ('Coco rallado', 'cucharadita', 1.50),
#    ('Coco fresco', 'g', 12),
#    ('Crema', 'cucharada', 1),
#    ('Crema para batir', 'cucharada', 1.50),
#    ('Crema para café', 'cucharada', 1),
#    ('Mantequilla', 'cucharadita', 1.50),
#    ('Margarina', 'cucharadita', 1),
#    ('Mayonesa', 'cucharadita', 1),
#    ('Media crema', 'cucharada', 2),
#    ('Tocino', 'rebanada', 1),
#    ('Vinagreta comercial', 'cucharada', 1.50)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 6) for nombre, unidad, porcion in aceites_grasas])

"""Lácteos"""
#lacteos = [
#    ('Leche de vaca', 'taza', 1.00),
#    ('Leche en polvo', 'cucharada', 4.00),
#    ('Yoghurt natural', 'taza', 1.00),
#    ('Jocoque seco', 'taza', 0.75),
#    ('Leche de soya', 'taza', 1.00),
#    ('Leche descremada', 'taza', 1.00)
#]
#
#query = """
#INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
#VALUES (%s, %s, %s, %s)
#"""
#cursor.executemany(query, [(nombre, unidad, porcion, 7) for nombre, unidad, porcion in lacteos])

"""Grasas con proteína"""
# grasas_con_proteina = [
#     ('Almendras', 'pieza', 10),
#     ('Avellana salada', 'pieza', 8),
#     ('Cacahuate tostado', 'pieza', 13),
#     ('Crema de almendras', 'cucharadita', 3),
#     ('Mantequilla de cacahuate', 'cucharadita', 2),
#     ('Nuez de castilla', 'pieza', 3),
#     ('Nuez de la india', 'pieza', 7),
#     ('Pepitas tostadas', 'cucharadita', 1),
#     ('Piñón', 'cucharadita', 1),
#     ('Pistache', 'pieza', 18),
#     ('Salsa pesto', 'cucharadita', 4),
#     ('Semilla de girasol tostada', 'cucharadita', 4)
# ]

# query = """
# INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
# VALUES (%s, %s, %s, %s)
# """
# cursor.executemany(query, [(nombre, unidad, porcion, 8) for nombre, unidad, porcion in grasas_con_proteina])

"""Azúcares"""
# azucar = [
#     ('Ate', 'cucharada', 1),
#     ('Azúcar', 'cucharadita', 2),
#     ('Cajeta', 'cucharadita', 1.5),
#     ('Gelatina', 'taza', 0.5),
#     ('Gomitas', 'pieza', 4),
#     ('Lechera', 'cucharadita', 2),
#     ('Miel', 'cucharadita', 2),
#     ('Mermelada', 'cucharadita', 2.5)
# ]

# query = """
# INSERT INTO Ingredientes (nombre_Ingrediente, unidad_Ingrediente, porcion_Ingrediente, id_Tipo_Ingrediente)
# VALUES (%s, %s, %s, %s)
# """
# cursor.executemany(query, [(nombre, unidad, porcion, 9) for nombre, unidad, porcion in azucar])

"""PLATILLOS"""

"Desayunos"
# desayunos_semana3 = [
#     ('Manzana picada con amaranto', '2/3 manzana picada (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal)'),
#     ('Pera picada con amaranto', '2/3 pera picada (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal)'),
#     ('Avena cocida con manzana en trozos', '1/2 taza de avena cocida (1 porción de cereal), 2/3 manzana en trozos (2 porciones de fruta)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, desayunos_semana3)



"""Batidos"""
# batidos_extra = [
#     ('Batido de plátano con amaranto y almendras', '1 plátano mediano (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 10 almendras (1 porción de grasa con proteína)'),
#     ('Batido de mango con avena y chía', '1 mango chico (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 1 cucharadita de chía (1 porción de grasa con proteína)'),
#     ('Batido de papaya con linaza y amaranto', '1 taza de papaya en cubos (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 1 cucharadita de linaza (1 porción de grasa con proteína)'),
#     ('Batido de piña con avena y nueces', '1 taza de piña picada (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 3 nueces (1 porción de grasa con proteína)'),
#     ('Batido de manzana con linaza y amaranto', '2/3 manzana picada (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 1 cucharadita de linaza (1 porción de grasa con proteína)'),
#     ('Batido de pera con chía y avena', '2/3 pera en cubos (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 1 cucharadita de chía (1 porción de grasa con proteína)'),
#     ('Batido de durazno con linaza y amaranto', '1 durazno picado (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 1 cucharadita de linaza (1 porción de grasa con proteína)'),
#     ('Batido de fresa con avena y pepitas tostadas', '8 fresas (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 1 cucharadita de pepitas tostadas (1 porción de grasa con proteína)'),
#     ('Batido de manzana con amaranto y pistaches', '2/3 manzana (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 18 pistaches (1 porción de grasa con proteína)'),
#     ('Batido de plátano con linaza y avena', '1 plátano mediano (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 1 cucharadita de linaza (1 porción de grasa con proteína)'),
#     ('Batido de mango con amaranto y cacahuates', '1 mango chico (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 13 cacahuates (1 porción de grasa con proteína)'),
#     ('Batido de pera con amaranto y crema de almendras', '2/3 pera (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 1 cucharadita de crema de almendras (1 porción de grasa con proteína)'),
#     ('Batido de piña con amaranto y pistaches', '1 taza de piña picada (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 18 pistaches (1 porción de grasa con proteína)'),
#     ('Batido de durazno con avena y semillas de girasol', '1 durazno (2 porciones de fruta), 1/4 taza de avena cocida (1 porción de cereal), 1 cucharadita de semillas de girasol tostadas (1 porción de grasa con proteína)'),
#     ('Batido de fresa con amaranto y mantequilla de cacahuate', '8 fresas (2 porciones de fruta), 1 cucharada de amaranto (1 porción de cereal), 1 cucharadita de mantequilla de cacahuate (1 porción de grasa con proteína)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, batidos_extra)

"""Almuerzos"""
# almuerzos_equilibrados = [
#     ('Wrap de jamón y queso con espinaca y aguacate',
#      '1 tortilla integral + 1/4 taza de arroz cocido (2 cereales), 1 rebanada de jamón + 1 rebanada de queso panela (2 origen animal), 1/2 taza de espinaca cocida (1 vegetal), 1/8 aguacate (1 grasa con proteína)'),

#     ('Sándwich de atún con huevo, lechuga y mayonesa',
#      '2 rebanadas de pan integral (2 cereales), 1 cucharada de atún + 1 huevo cocido (2 origen animal), 2 hojas de lechuga (1 vegetal), 1 cucharadita de mayonesa (1 grasa con proteína)'),

#     ('Bowl de pollo deshebrado con tortilla, verduras y almendras',
#      '2 tortillas pequeñas (2 cereales), 1/4 taza de pollo deshebrado + 1 cucharada de queso cottage (2 origen animal), 1/4 taza de zanahoria rallada (1 vegetal), 10 almendras (1 grasa con proteína)'),

#     ('Ensalada tibia de arroz, carne molida y espinaca con nuez',
#      '1/2 taza de arroz cocido + 1 tostada horneada (2 cereales), 1/4 taza de carne molida cocida + 1 cucharada de queso fresco (2 origen animal), 1/4 taza de espinaca salteada (1 vegetal), 3 nueces (1 grasa con proteína)'),

#     ('Molletes con jamón, queso, jitomate y aguacate',
#      '2 mitades de bolillo integral (2 cereales), 1 rebanada de jamón + 1 rebanada de queso amarillo (2 origen animal), 2 rebanadas de jitomate (1 vegetal), 1/8 aguacate (1 grasa con proteína)'),

#     ('Tacos de huevo y salchicha con nopales y pistaches',
#      '2 tortillas pequeñas (2 cereales), 1 huevo cocido + 1/2 salchicha (2 origen animal), 1/2 taza de nopales cocidos (1 vegetal), 18 pistaches (1 grasa con proteína)'),

#     ('Burrito de atún con zanahoria y crema de cacahuate',
#      '1 tortilla integral + 1/4 taza de avena cocida (2 cereales), 1 cucharada de atún + 1 rebanada de queso panela (2 origen animal), 1/4 taza de zanahoria rallada (1 vegetal), 1 cucharadita de crema de cacahuate (1 grasa con proteína)'),

#     ('Sándwich de pollo con espinaca y linaza',
#      '2 rebanadas de pan de avena (2 cereales), 1/4 taza de pollo deshebrado + 1 cucharada de queso cottage (2 origen animal), 1/4 taza de espinaca cruda (1 vegetal), 1 cucharadita de linaza (1 grasa con proteína)'),

#     ('Tostadas de huevo con jitomate y pepitas',
#      '2 tostadas horneadas (2 cereales), 1 huevo cocido + 1 cucharada de queso fresco (2 origen animal), 2 rebanadas de jitomate (1 vegetal), 1 cucharadita de pepitas tostadas (1 grasa con proteína)'),

#     ('Wrap de carne molida con verduras y almendras',
#      '1 tortilla integral + 1/4 taza de arroz integral (2 cereales), 1/4 taza de carne molida cocida + 1 rebanada de queso amarillo (2 origen animal), 1/4 taza de zanahoria cocida (1 vegetal), 10 almendras (1 grasa con proteína)'),

#     ('Molletes de atún y queso con jitomate y pistaches',
#      '2 mitades de bolillo (2 cereales), 1 cucharada de atún + 1 rebanada de queso (2 origen animal), 2 rebanadas de jitomate (1 vegetal), 18 pistaches (1 grasa con proteína)'),

#     ('Sándwich de huevo cocido y jamón con lechuga y nuez',
#      '2 rebanadas de pan integral (2 cereales), 1 huevo cocido + 1 rebanada de jamón (2 origen animal), 2 hojas de lechuga (1 vegetal), 3 nueces (1 grasa con proteína)'),

#     ('Burrito de salchicha y queso con espinaca y pepitas',
#      '1 tortilla de avena + 1/4 taza de arroz (2 cereales), 1 salchicha cocida + 1 rebanada de queso (2 origen animal), 1/4 taza de espinaca cocida (1 vegetal), 1 cucharadita de pepitas (1 grasa con proteína)'),

#     ('Tacos de jamón y huevo con jitomate y linaza',
#      '2 tortillas pequeñas (2 cereales), 1 rebanada de jamón + 1 huevo cocido (2 origen animal), 2 rebanadas de jitomate (1 vegetal), 1 cucharadita de linaza (1 grasa con proteína)'),

#     ('Wrap de pollo, queso y espinaca con cacahuates',
#      '1 tortilla integral + 1/4 taza de avena cocida (2 cereales), 1/4 taza de pollo deshebrado + 1 cucharada de queso cottage (2 origen animal), 1/4 taza de espinaca cruda (1 vegetal), 13 cacahuates (1 grasa con proteína)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, almuerzos_equilibrados)


"""Comidas"""
# comidas_nuevas = [
#     ('Ensalada mediterránea con pollo, espinaca, jitomate y couscous + aguacate + mango',
#      '1/4 taza de pollo cocido + 1 rebanada de queso feta + 1 cucharada de yogur natural (3 O.Animal), 1/2 taza de espinaca + 1/2 taza de jitomate (2 Vegetal), 1/4 taza de couscous + 1 pan tostado (2 Cereal), 1/8 aguacate + 1 cucharadita de linaza + 3 almendras (3 Grasa), 1/2 mango picado (1 Fruta)'),

#     ('Sopa de cebada con carne de res y zanahoria + ensalada de hojas verdes con nuez + plátano',
#      '1/4 taza de carne de res cocida + 1 rebanada de queso + 1 cucharada de yogur natural (3 O.Animal), 1/2 taza de zanahoria + 1/2 taza de hojas verdes (2 Vegetal), 1/2 taza de cebada cocida + 1 tostada horneada (2 Cereal), 3 nueces + 1 cucharadita de linaza + 1 cucharadita de aceite de oliva (3 Grasa), 1 plátano pequeño (1 Fruta)'),

#     ('Bowl de arroz salvaje con atún, espárragos y pimientos + aguacate + durazno',
#      '1 cucharada de atún + 1 rebanada de queso + 1 huevo cocido (3 O.Animal), 1/2 taza de espárragos + 1/2 taza de pimiento (2 Vegetal), 1/2 taza de arroz salvaje + 1 pan integral (2 Cereal), 1/8 aguacate + 1 cucharadita de linaza + 3 pistaches (3 Grasa), 1 durazno (1 Fruta)'),

#     ('Guisado de alverjón con chayote y zanahoria + tortillas + fruta',
#      '1 cucharada de alverjón cocido + 1 cucharada de queso fresco + 1 huevo cocido (3 O.Animal), 1/2 taza de chayote + 1/2 taza de zanahoria (2 Vegetal), 2 tortillas pequeñas + 1/4 taza de avena cocida (2 Cereal), 1 cucharadita de aceite vegetal + 3 nueces + 1 cucharadita de linaza (3 Grasa), 1 manzana pequeña (1 Fruta)'),

#     ('Albóndigas de lenteja con avena y espinaca + pan integral + naranja',
#      '1 cucharada de lentejas cocidas + 1 rebanada de queso panela + 1 cucharada de yogur natural (3 O.Animal), 1/2 taza de espinaca + 1/2 taza de jitomate (2 Vegetal), 1 pan integral + 1/4 taza de arroz cocido (2 Cereal), 1 cucharadita de linaza + 3 almendras + 1 cucharadita de aceite de oliva (3 Grasa), 1 naranja (1 Fruta)'),

#     ('Filete de tilapia con ensalada tibia de brócoli y elote + arroz + papaya',
#      '1 filete de tilapia + 1 cucharada de queso + 1 cucharada de yogur (3 O.Animal), 1/2 taza de brócoli + 1/2 taza de elote (2 Vegetal), 1/2 taza de arroz integral + 1 pan tostado (2 Cereal), 3 nueces + 1 cucharadita de linaza + 1 cucharadita de aceite vegetal (3 Grasa), 1 taza de papaya (1 Fruta)'),

#     ('Bowl mexicano de carne de cerdo, nopal, cebolla y arroz + aguacate + mandarina',
#      '1/4 taza de cerdo cocido + 1 rebanada de queso + 1 cucharada de yogur (3 O.Animal), 1/2 taza de nopal cocido + 1/2 taza de cebolla salteada (2 Vegetal), 1/2 taza de arroz cocido + 1 tostada horneada (2 Cereal), 1/8 aguacate + 3 nueces + 1 cucharadita de linaza (3 Grasa), 1 mandarina (1 Fruta)'),

#     ('Calabacitas rellenas de pollo y requesón + arroz salvaje + ensalada + pera',
#      '1/4 taza de pollo deshebrado + 1 cucharada de requesón + 1 rebanada de queso (3 O.Animal), 1/2 taza de calabacitas + 1/2 taza de lechuga (2 Vegetal), 1/2 taza de arroz salvaje + 1 pan tostado (2 Cereal), 1 cucharadita de aceite vegetal + 1 cucharadita de linaza + 3 pistaches (3 Grasa), 1/2 pera picada (1 Fruta)'),

#     ('Guiso de garbanzo con carne y espinaca + tortilla + arroz + fresa',
#      '1 cucharada de garbanzo + 1/4 taza de carne cocida + 1 rebanada de queso fresco (3 O.Animal), 1/2 taza de espinaca cocida + 1/2 taza de jitomate (2 Vegetal), 2 tortillas pequeñas + 1/4 taza de arroz cocido (2 Cereal), 3 nueces + 1 cucharadita de aceite vegetal + 1 cucharadita de linaza (3 Grasa), 6 fresas (1 Fruta)'),

#     ('Sopa de avena con huevo y queso + ensalada de zanahoria y pepino + pan integral + uvas',
#      '1 huevo cocido + 1 rebanada de queso + 1 cucharada de yogur (3 O.Animal), 1/2 taza de zanahoria + 1/2 taza de pepino (2 Vegetal), 1/4 taza de avena cocida + 1 pan integral (2 Cereal), 3 almendras + 1 cucharadita de linaza + 1 cucharadita de aceite vegetal (3 Grasa), 10 uvas (1 Fruta)'),

#     ('Arroz primavera con pollo, calabaza, elote y champiñones + tostada + durazno',
#      '1/4 taza de pollo cocido + 1 rebanada de queso + 1 cucharada de yogur natural (3 O.Animal), 1/2 taza de calabaza + 1/2 taza de champiñones (2 Vegetal), 1/2 taza de arroz cocido + 1 tostada horneada (2 Cereal), 1 cucharadita de linaza + 3 nueces + 1 cucharadita de aceite vegetal (3 Grasa), 1 durazno (1 Fruta)'),

#     ('Tacos de salmón con ensalada de pimiento y pepino + arroz integral + plátano',
#      '1 fajita de salmón + 1 rebanada de queso + 1 cucharada de requesón (3 O.Animal), 1/2 taza de pimiento + 1/2 taza de pepino (2 Vegetal), 2 tortillas pequeñas + 1/4 taza de arroz integral (2 Cereal), 1/8 aguacate + 1 cucharadita de linaza + 3 almendras (3 Grasa), 1 plátano pequeño (1 Fruta)'),

#     ('Guisado de pavo con brócoli y jitomate + pan + arroz + papaya',
#      '1/4 taza de pavo cocido + 1 rebanada de queso amarillo + 1 cucharada de yogur (3 O.Animal), 1/2 taza de brócoli + 1/2 taza de jitomate (2 Vegetal), 1 pan integral + 1/4 taza de arroz cocido (2 Cereal), 3 nueces + 1 cucharadita de linaza + 1 cucharadita de aceite vegetal (3 Grasa), 1 taza de papaya picada (1 Fruta)'),

#     ('Hojaldre relleno de carne y vegetales + ensalada fresca + fruta',
#  '1/4 taza de carne molida cocida + 1 rebanada de queso + 1 cucharada de requesón (3 O.Animal), 1/4 taza de espinaca + 1/4 taza de pimiento picado (2 Vegetal), 1 hojaldre individual + 1 pan tostado (2 Cereal), 3 nueces + 1 cucharadita de aceite vegetal + 1 cucharadita de linaza (3 Grasa), 1 durazno picado (1 Fruta)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, comidas_nuevas)

"""Colaciones"""
# colaciones = [
#     ('Pepino con limón + nueces + plátano',
#      '1/2 taza de pepino (1 vegetal), 3 nueces (1 grasa con proteína), 1 plátano mediano (2 frutas)'),

#     ('Jitomate cherry + crema de cacahuate + manzana picada',
#      '5 jitomates cherry (1 vegetal), 1 cucharadita de crema de cacahuate (1 grasa con proteína), 2/3 manzana picada (2 frutas)'),

#     ('Zanahoria baby + pistaches + pera en cubos',
#      '1/2 taza de zanahoria baby (1 vegetal), 18 pistaches (1 grasa con proteína), 2/3 pera en cubos (2 frutas)'),

#     ('Palitos de apio + linaza + durazno picado',
#      '1/2 taza de apio en tiras (1 vegetal), 1 cucharadita de linaza (1 grasa con proteína), 1 durazno picado (2 frutas)'),

#     ('Jícama con chile + almendras + mango',
#      '1/2 taza de jícama (1 vegetal), 10 almendras (1 grasa con proteína), 1/2 mango picado (2 frutas)'),

#     ('Rollitos de lechuga + aguacate + mandarina',
#      '2 hojas de lechuga (1 vegetal), 1/8 aguacate (1 grasa con proteína), 1 mandarina (2 frutas)'),

#     ('Tiras de pimiento + semillas de calabaza + papaya',
#      '1/2 taza de pimiento en tiras (1 vegetal), 1 cucharadita de semillas de calabaza (1 grasa con proteína), 1 taza de papaya (2 frutas)'),

#     ('Ensalada rápida de pepino + linaza + uvas',
#      '1/2 taza de pepino en cubos (1 vegetal), 1 cucharadita de linaza (1 grasa con proteína), 10 uvas (2 frutas)'),

#     ('Zanahoria rallada + nueces + fresas',
#      '1/2 taza de zanahoria rallada (1 vegetal), 3 nueces (1 grasa con proteína), 8 fresas (2 frutas)'),

#     ('Palitos de apio + mantequilla de almendra + pera',
#      '1/2 taza de apio en bastones (1 vegetal), 1 cucharadita de mantequilla de almendra (1 grasa con proteína), 2/3 pera rebanada (2 frutas)'),

#     ('Jícama en palitos + linaza + piña',
#      '1/2 taza de jícama en palitos (1 vegetal), 1 cucharadita de linaza (1 grasa con proteína), 3/4 taza de piña picada (2 frutas)'),

#     ('Tiras de pimiento morrón + crema de cacahuate + durazno',
#      '1/2 taza de pimiento morrón (1 vegetal), 1 cucharadita de crema de cacahuate (1 grasa con proteína), 1 durazno (2 frutas)'),

#     ('Lechuga picada + pistaches + guayaba',
#      '1/2 taza de lechuga (1 vegetal), 18 pistaches (1 grasa con proteína), 2 guayabas pequeñas rebanadas (2 frutas)'),

#     ('Jitomate picado + nueces + arándanos',
#      '1/2 taza de jitomate en cubos (1 vegetal), 3 nueces (1 grasa con proteína), 1 cucharada de arándanos deshidratados (2 frutas equivalentes)'),

#     ('Zanahoria baby + chía + plátano en rodajas',
#      '1/2 taza de zanahoria baby (1 vegetal), 1 cucharadita de chía (1 grasa con proteína), 1 plátano mediano en rodajas (2 frutas)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, colaciones)

"""Cenas"""
# cenas = [
#     ('Pan tostado con queso panela y manzana en rebanadas',
#      '1 rebanada de pan integral (1 cereal), 1 rebanada de queso panela (1 origen animal), 1/2 manzana en rebanadas (1 fruta)'),

#     ('Tostada con atún y rodajas de plátano',
#      '1 tostada horneada (1 cereal), 1 cucharada de atún (1 origen animal), 1/2 plátano mediano en rodajas (1 fruta)'),

#     ('Bolillo con rebanada de jamón y mandarina',
#      '1/2 bolillo integral (1 cereal), 1 rebanada de jamón de pavo (1 origen animal), 1 mandarina pelada (1 fruta)'),

#     ('Galletas saladas con queso amarillo y durazno en cubos',
#      '3 galletas saladas (1 cereal), 1 rebanada de queso amarillo (1 origen animal), 1/2 durazno en cubos (1 fruta)'),

#     ('Pan de avena con requesón y papaya',
#      '1 rebanada de pan de avena (1 cereal), 1 cucharada de requesón (1 origen animal), 1/2 taza de papaya picada (1 fruta)'),

#     ('Tostada con huevo cocido y rebanadas de pera',
#      '1 tostada horneada (1 cereal), 1 huevo cocido (1 origen animal), 2/3 pera rebanada (1 fruta)'),

#     ('Pan integral con salchicha cocida y guayaba',
#      '1 rebanada de pan integral (1 cereal), 1/2 salchicha cocida (1 origen animal), 1 guayaba pequeña (1 fruta)'),

#     ('Galleta de arroz con queso fresco y fresas',
#      '1 galleta de arroz (1 cereal), 1 cucharada de queso fresco (1 origen animal), 6 fresas rebanadas (1 fruta)'),

#     ('Pan pita mini con huevo revuelto y mango',
#      '1 mini pan pita (1 cereal), 1 huevo pequeño revuelto (1 origen animal), 1/2 mango picado (1 fruta)'),

#     ('Tortilla pequeña con atún y piña',
#      '1 tortilla pequeña (1 cereal), 1 cucharada de atún (1 origen animal), 3/4 taza de piña picada (1 fruta)'),

#     ('Pan multigrano con jamón de pavo y melón',
#      '1 rebanada de pan multigrano (1 cereal), 1 rebanada de jamón de pavo (1 origen animal), 1 taza de melón picado (1 fruta)'),

#     ('Tostada integral con requesón y uvas',
#      '1 tostada integral (1 cereal), 1 cucharada de requesón (1 origen animal), 10 uvas (1 fruta)'),

#     ('Pan de centeno con queso cottage y durazno',
#      '1 rebanada de pan de centeno (1 cereal), 1 cucharada de queso cottage (1 origen animal), 1/2 durazno en cubos (1 fruta)'),

#     ('Tortilla de maíz con huevo cocido y papaya',
#      '1 tortilla de maíz (1 cereal), 1 huevo cocido (1 origen animal), 1/2 taza de papaya picada (1 fruta)'),

#     ('Pan de avena con queso fresco y pera',
#      '1 rebanada de pan de avena (1 cereal), 1 rebanada de queso fresco (1 origen animal), 2/3 pera en rebanadas (1 fruta)')
# ]

# query = """
# INSERT INTO Platillos (nombre_Platillo, descripcion_Platillo)
# VALUES (%s, %s)
# """
# cursor.executemany(query, cenas)


"""DIAS"""

# dias = [
#     ('Lunes',),
#     ('Martes',),
#     ('Miércoles',),
#     ('Jueves',),
#     ('Viernes',),
#     ('Sábado',),
#     ('Domingo',)
# ]

# query = "INSERT INTO dias (dia) VALUES (%s)"
# cursor.executemany(query, dias)

"""Tipos comidas"""

# tipos_comida = [
#     ('Desayuno',),
#     ('Batido',),
#     ('Almuerzo',),
#     ('Comida',),
#     ('Colación',),
#     ('Cena',)
# ]

# query = "INSERT INTO tipos_Comida (nombre_Tipo) VALUES (%s)"
# cursor.executemany(query, tipos_comida)
# conn.commit()

"""Menus"""

# Rangos por tipo de comida
rango_ids = {
    1: list(range(1, 16)),      # Desayuno
    2: list(range(16, 31)),     # Batido
    3: list(range(31, 46)),     # Almuerzo
    4: list(range(46, 74)),     # Comida
    5: list(range(74, 89)),     # Colación
    6: list(range(89, 104))     # Cena
}

used_ids = {tipo: set() for tipo in rango_ids}
menus_semanales = []

for dia_id in range(1, 8):  # Lunes a Domingo (id_Dia del 1 al 7)
    for tipo in range(1, 7):  # Tipos de comida del 1 al 6
        disponibles = list(set(rango_ids[tipo]) - used_ids[tipo])
        if not disponibles:
            raise ValueError(f"No hay más platillos disponibles para el tipo {tipo}")

        platillo_id = random.choice(disponibles)
        used_ids[tipo].add(platillo_id)
        menus_semanales.append((platillo_id, dia_id, tipo))

query = """
INSERT INTO menus (id_Platillo, id_Dia, id_Tipos_Comida)
VALUES (%s, %s, %s)
"""
cursor.executemany(query, menus_semanales)


#################################################################################################################################################################################

conn.commit()

conn.close()