import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306",
    database = "test"
)

#print(conn)

cursor = conn.cursor()

#################################################################################################################################################################################

""" CREACIÓN DE TABLAS """
#tableCreation = """CREATE TABLE Meals (id_Meal INT AUTO_INCREMENT PRIMARY KEY, meal_Name VARCHAR (255), meal_Description VARCHAR (255), id_Meal_Type INT, FOREIGN KEY (id_Meal_Type) REFERENCES #meal_types (id_Meal_Type))"""
#cursor.execute(tableCreation)
#conn.commit()

#cursor.execute("SHOW TABLES")
#for dato in cursor:
#    print(dato)

#################################################################################################################################################################################

""" 1. Ingredient_Types """
#insert_ingredient_types = """
#    INSERT INTO Ingredients_Types (Ingredient_Type) VALUES 
#        ('Vegetales'), 
#        ('O. Animal'), 
#        ('Verdura'), """ YA NO HAY ID 3 """
#        ('Leguminosas'), 
#        ('Frutas'),
#        ('Cereal'),
#        ('Aceites y grasas'),
#        ('Grasas con proteinas'),
#        ('Lacteos'),
#        ('Azucar')
#    """
#cursor.execute(insert_ingredient_types)

""" 2. Ingredients """ 
#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(1, 'Acelga cruda', '2 tazas'),
#(1, 'Acelga cocida', '½ taza'),
#(1, 'Betabel crudo', '¼ pieza'),
#(1, 'Brócoli cocido', '½ taza'),
#(1, 'Calabacita cocida', '½ taza'),
#(1, 'Champiñón cocido rebanado', '1 ½ tazas'),
#(1, 'Chayote cocido picado', '½ taza'),
#(1, 'Chile poblano', '1 pieza'),
#(1, 'Col cocida picada', '½ taza'),
#(1, 'Coliflor cocida', '¼ taza'),
#(1, 'Ejotes cocidos picados', '8 piezas'),
#(1, 'Elotitos cambray', '6 piezas'),
#(1, 'Espárragos', '½ taza'),
#(1, 'Espinaca cocida', '2 tazas'),
#(1, 'Espinaca cruda picada', '1 taza'),
#(1, 'Flor de calabaza cocida', '3 tazas'),
#(1, 'Germen de alfalfa', '1 taza'),
#(1, 'Hongos crudos', '½ taza'),
#(1, 'Huazontle', '1/3 taza'),
#(1, 'Huitlacoche cocido', '½ taza'),
#(1, 'Jicama picada', '1 pieza'),
#(1, 'Jitomate bola', '4 piezas'),
#(1, 'Jitomate cherry', '3 tazas'),
#(1, 'Lechuga', '½ taza'),
#(1, 'Zanahoria', '1 taza'),
#(1, 'Nopal cocido', '2 piezas'),
#(1, 'Nopal crudo', '1 taza'),
#(1, 'Pepino con cáscara', '½ taza'),
#(1, 'Pimiento morrón cocido', '1 taza'),
#(1, 'Setas cocidas', '3 piezas'),
#(1, 'Verdolaga cocida', '½ taza'),
#(1, 'Zanahoria miniatura', '1 taza'),
#(1, 'Zanahoria rallada cruda', '½ taza')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(2, 'Atún fresco', '½ lata'),
#(2, 'Bistec (res/cerdo)', '30g'),
#(2, 'Bola de ternera', '30g'),
#(2, 'Camarón cocido', '35g'),
#(2, 'Camarón gigante', '5 piezas'),
#(2, 'Carne de res seca', '2 piezas'),
#(2, 'Cecina', '11g'),
#(2, 'Huevo', '1 pieza'),
#(2, 'Claras de huevo', '2 piezas'),
#(2, 'Filete de pescado', '40g'),
#(2, 'Filete de res', '30g'),
#(2, 'Filete mignón', '30g'),
#(2, 'Jamón', '2 rebanadas'),
#(2, 'Milanesa de res', '30g'),
#(2, 'Pierna de pollo s/piel', '1 pieza'),
#(2, 'Pechuga de pollo', '30g'),
#(2, 'Pulpo cocido', '25g'),
#(2, 'Quesillo', '30g'),
#(2, 'Queso cottage', '3 cucharadas'),
#(2, 'Queso panela', '40g'),
#(2, 'Requesón', '3 cucharadas'),
#(2, 'Salmón ahumado', '35g'),
#(2, 'Surimi', '⅔ barra')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(4, 'Alverjón cocido', '1/2 taza'),
#(4, 'Chicharo cocido', '1/2 taza'),
#(4, 'Frijol cocido', '1/2 taza'),
#(4, 'Garbanzo cocido', '1/2 taza'),
#(4, 'Haba seca cocida', '1/2 taza'),
#(4, 'Hummus', '5 cucharadas'),
#(4, 'Lentejas cocidas', '1/2 taza'),
#(4, 'Soya cocida', '1/2 taza')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(5, 'Agua de coco', '1 1/2 taza'),
#(5, 'Arándano fresco', '125g'),
#(5, 'Blueberries', '1/4 taza'),
#(5, 'Cereza', '20 piezas'),
#(5, 'Ciruela', '3 piezas'),
#(5, 'Dátil seco', '2 piezas'),
#(5, 'Durazno', '2 piezas pequeñas'),
#(5, 'Frambuesa', '1 taza'),
#(5, 'Fresa rebanada', '1 taza'),
#(5, 'Guayaba', '3 piezas'),
#(5, 'Higo', '2 piezas'),
#(5, 'Jugo de naranja natural', '1/2 taza'),
#(5, 'Kiwi', '1 pieza'),
#(5, 'Lichis', '12 piezas'),
#(5, 'Mamey', '1/3 pieza'),
#(5, 'Mandarina', '2 piezas'),
#(5, 'Mango manila', '1 pieza'),
#(5, 'Mango petacón', '1/2 pieza'),
#(5, 'Manzana', '1 pieza'),
#(5, 'Maracuyá', '3 piezas'),
#(5, 'Melón picado', '1 taza'),
#(5, 'Moras', '1/4 taza'),
#(5, 'Naranja', '2 piezas'),
#(5, 'Nectarina', '1 pieza'),
#(5, 'Papaya picada', '1 taza'),
#(5, 'Pastas', '10 piezas'),
#(5, 'Pera', '1/2 pieza'),
#(5, 'Piña', '1 rebanada'),
#(5, 'Plátano', '1/2 pieza'),
#(5, 'Sandía', '1 taza'),
#(5, 'Toronja', '1 pieza'),
#(5, 'Tuna', '2 piezas'),
#(5, 'Uva', '18 piezas'),
#(5, 'Zapote negro', '1/2 pieza'),
#(5, 'Zarzamora', '1/4 taza')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(7, 'Aceite', '1 cucharadita'),
#(7, 'Aceitunas', '5 piezas'),
#(7, 'Aderezo tipo césar', '1 cucharada'),
#(7, 'Aderezo de miel y mostaza', '2 piezas'),
#(7, 'Aderezo italiano', '3 piezas'),
#(7, 'Aguacate', '4 cucharadas'),
#(7, 'Calamahua', '5 piezas'),
#(7, 'Coco rallado', '6 cucharadas'),
#(7, 'Coco fresco', '7 cucharadas'),
#(7, 'Crema para batir', '1 cucharada'),
#(7, 'Crema para café', '2 piezas'),
#(7, 'Guacamole', '3 piezas'),
#(7, 'Mantequilla', '4 cucharadas'),
#(7, 'Margarina', '5 piezas'),
#(7, 'Mayonesa', '6 cucharadas'),
#(7, 'Media crema', '7 cucharadas'),
#(7, 'Tocino', '1 cucharada'),
#(7, 'Vinagreta comercial', '2 piezas')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(8, 'Almendras', '10 piezas'),
#(8, 'Avellana salada', '8 piezas'),
#(8, 'Cacahuate tostado', '13 piezas'),
#(8, 'Crema de almendras', '3 cucharaditas'),
#(8, 'Mantequilla de cacahuate', '2 cucharaditas'),
#(8, 'Nuez de castilla', '3 piezas'),
#(8, 'Nuez de la India', '7 piezas'),
#(8, 'Pepitas tostadas', '1 cucharadita'),
#(8, 'Piñón', '1 cucharada'),
#(8, 'Pistache', '18 piezas'),
#(8, 'Salsa pesto', '4 cucharaditas'),
#(8, 'Semilla de girasol tostada', '4 cucharaditas')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(9, 'Leche de vaca', '1 taza'),
#(9, 'Leche en polvo', '4 cucharadas'),
#(9, 'Yoghurt natural', '1 taza (220g)'),
#(9, 'Jocoque seco', '½ taza'),
#(9, 'Leche de soya', '1 taza'),
#(9, 'Leche descremada', '1 taza')
#"""

#insert_ingredients = """
#INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
#(10, 'Atel', '13g o 1 cucharada'),
#(10, 'Azúcar', '2 cucharaditas'),
#(10, 'Cajeta', '1 1/2 cucharaditas'),
#(10, 'Gelatina', '1/2 taza'),
#(10, 'Gomitas', '4 piezas'),
#(10, 'Lechera', '2 cucharaditas'),
#(10, 'Miel', '2 cucharaditas'),
#(10, 'Mermelada', '2 1/2 cucharaditas')
#"""
#cursor.execute(insert_ingredients)

""" 3. Meal_Types """
#insert_meal_types = """
#INSERT INTO Meal_Types (meal_Type) VALUES 
#('Al despertar'), 
#('Batido'), 
#('Almuerzo'), 
#('Comida'), 
#('Colacion'),
#('Cena')
#"""
#cursor.execute(insert_meal_types)

""" 4. Meals """
insert_meals = """
INSERT INTO Meals (id_Meal_Type, meal_Name, meal_Description) VALUES 
-- ============ DESAYUNOS ============
(1, 'Pan tostado con guayaba rebanada', 'Equivalencias: 2 rebanadas de pan integral (2 cereales) + 3 rebanadas de guayaba (1 fruta)'),
(1, 'Manzana picada con amaranto', 'Equivalencias: 1 manzana mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Pan tostado con fresas', 'Equivalencias: 2 rebanadas de pan integral (2 cereales) + 6 fresas medianas (1 fruta)'),
(1, 'Pan tostado con manzana rebanada', 'Equivalencias: 2 rebanadas de pan integral (2 cereales) + ½ manzana rebanada (½ fruta)'),
(1, 'Pera picada con amaranto', 'Equivalencias: 1 pera mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Tazon de avena cocida con durazno picado', 'Equivalencias: ½ taza de avena cocida (1 cereal) + ½ durazno picado (½ fruta)'),
(1, 'Un tazon de durazno con nuez en trozos', 'Equivalencias: 1 durazno mediano (1 fruta) + 6 mitades de nuez (1 grasa)'),
(1, 'Avena cocida con manzana en trozos.', 'Equivalencias: ½ taza de avena cocida (1 cereal) + ½ manzana picada (½ fruta)'),
(1, 'Pan tostado con fresas', 'Equivalencias: 2 rebanadas de pan integral (2 cereales) + 6 fresas medianas (1 fruta)'),
(1, 'Un tazón de durazno con nuez en trozos', 'Equivalencias: 1 durazno mediano (1 fruta) + 6 mitades de nuez (1 grasa)'),
(1, 'Manzana picada con amaranto', 'Equivalencias: 1 manzana mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Pera picada con amaranto', 'Equivalencias: 1 pera mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Avena cocida con manzana en trozos.', 'Equivalencias: ½ taza de avena cocida (1 cereal) + ½ manzana picada (½ fruta)'),
(1, 'Un tazon de durazno con nuez en trozos', 'Equivalencias: 1 durazno mediano (1 fruta) + 6 mitades de nuez (1 grasa)'),
(1, 'Manzana picada con amaranto', 'Equivalencias: 1 manzana mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Pera picada con amaranto', 'Equivalencias: 1 pera mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Avena cocida con manzana en trozos.', 'Equivalencias: ½ taza de avena cocida (1 cereal) + ½ manzana picada (½ fruta)'),
(1, 'Manzana picada con amaranto', 'Equivalencias: 1 manzana mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Avena cocida con manzana en trozos.', 'Equivalencias: ½ taza de avena cocida (1 cereal) + ½ manzana picada (½ fruta)'),
(1, 'Pera picada con amaranto', 'Equivalencias: 1 pera mediana (1 fruta) + 1 cucharada de amaranto (1 cereal)'),
(1, 'Pan tostado con fresas', 'Equivalencias: 2 rebanadas de pan integral (2 cereales) + 6 fresas medianas (1 fruta)'),

-- ============ BATIDOS ============
(2, 'Batido de manzana con nuez y 1/4 de taza de avena', 'Equivalencias: 1 manzana (1 fruta) + 6 mitades de nuez (1 grasa) + ¼ taza avena (½ cereal)'),
(2, 'Batido de fresa con amaranto y nueces.', 'Equivalencias: 6 fresas (1 fruta) + 1 cda amaranto (1 cereal) + 6 mitades nuez (1 grasa)'),
(2, 'Batido de fresa con amaranto y nuez.', 'Equivalencias: 6 fresas (1 fruta) + 1 cda amaranto (1 cereal) + 6 mitades nuez (1 grasa)'),
(2, 'Batido de manzana con chía y avena.', 'Equivalencias: 1 manzana (1 fruta) + 1 cda chía (1 cereal) + ¼ taza avena (½ cereal)'),
(2, 'Batido de pera y manzana con almendras y avena.', 'Equivalencias: ½ pera (½ fruta) + ½ manzana (½ fruta) + 10 almendras (1 grasa) + ¼ taza avena (½ cereal)'),
(2, 'Batido de fresa con nueces y linaza.', 'Equivalencias: 6 fresas (1 fruta) + 6 mitades nuez (1 grasa) + 1 cda linaza (1 cereal)'),
(2, 'Batido de fresa con amaranto y nueces.', 'Equivalencias: 6 fresas (1 fruta) + 1 cda amaranto (1 cereal) + 6 mitades nuez (1 grasa)'),
(2, 'Batido de manzana con chía y avena.', 'Equivalencias: 1 manzana (1 fruta) + 1 cda chía (1 cereal) + ¼ taza avena (½ cereal)'),
(2, 'Batido de fresa con nueces y linaza.', 'Equivalencias: 6 fresas (1 fruta) + 6 mitades nuez (1 grasa) + 1 cda linaza (1 cereal)'),
(2, 'Batido de pera y manzana con almendras y avena.', 'Equivalencias: ½ pera (½ fruta) + ½ manzana (½ fruta) + 10 almendras (1 grasa) + ¼ taza avena (½ cereal)'),
(2, 'Batido de fresa con amaranto y nueces.', 'Equivalencias: 6 fresas (1 fruta) + 1 cda amaranto (1 cereal) + 6 mitades nuez (1 grasa)'),
(2, 'Batido de manzana con chía y avena.', 'Equivalencias: 1 manzana (1 fruta) + 1 cda chía (1 cereal) + ¼ taza avena (½ cereal)'),
(2, 'Batido de fresa con nueces y linaza.', 'Equivalencias: 6 fresas (1 fruta) + 6 mitades nuez (1 grasa) + 1 cda linaza (1 cereal)'),
(2, 'Batido de pera y manzana con almendras y avena.', 'Equivalencias: ½ pera (½ fruta) + ½ manzana (½ fruta) + 10 almendras (1 grasa) + ¼ taza avena (½ cereal)'),

-- ============ ALMUERZOS ============
(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Equivalencias: 1 taza pepino (1 verdura) + ½ taza zanahoria (1 verdura) + 90g pollo (3 proteínas) + 6 mitades nuez (1 grasa) + 2 tortillas (2 cereales)'),
(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cúlta de linaza, chia, semillas de calabaza, avena, nuez picada, arándanos', 'Equivalencias: 125g yogur (1 lácteo) + 1 cdta linaza/chía (1 cereal) + 1 cda semillas calabaza (1 grasa) + ¼ taza avena (½ cereal) + 6 mitades nuez (1 grasa) + ¼ taza arándanos (½ fruta)'),
(3, 'Avena cocida, manzana picada y nuez. Acompañados de dos huevos revueltos.', 'Equivalencias: ½ taza avena cocida (1 cereal) + ½ manzana picada (½ fruta) + 6 mitades nuez (1 grasa) + 2 huevos (2 proteínas)'),
(3, '1 sándwich de atún con mostaza y verduras (lechuga, pepino, zanahoria rallada).', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + ½ lata atún (2 proteínas) + 1 taza lechuga (1 verdura) + ½ pepino (1 verdura) + ½ taza zanahoria rallada (1 verdura)'),
(3, 'Ensalada de garbanzo, calabaza y pepino con nueces. Y de postre pan tostado con fresas.', 'Equivalencias: ½ taza garbanzos (1 leguminosa) + ½ taza calabaza (1 verdura) + ½ pepino (1 verdura) + 6 mitades nuez (1 grasa) + 2 rebanadas pan integral (2 cereales) + 6 fresas (1 fruta)'),
(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Equivalencias: 2 huevos (2 proteínas) + 30g jamón (1 proteína) + 30g tocino (1 grasa) + 1 guayaba (½ fruta)'),
(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Equivalencias: 1 taza pepino (1 verdura) + ½ taza zanahoria (1 verdura) + 90g pollo (3 proteínas) + 6 mitades nuez (1 grasa) + 2 tortillas (2 cereales)'),
(3, 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.', 'Equivalencias: Omelette con ½ taza champiñones (1 verdura) + ½ taza espinacas (1 verdura) + 2 tortillas (2 cereales) + 1 cda semillas calabaza (1 grasa) + 1 pera (1 fruta)'),
(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Equivalencias: 2 huevos (2 proteínas) + 30g jamón (1 proteína) + 30g tocino (1 grasa) + 1 guayaba (½ fruta)'),
(3, 'Huevos revueltos con tocino', 'Equivalencias: 2 huevos (2 proteínas) + 30g tocino (1 grasa)'),
(3, 'Huevos revueltos con bistec de res acompañado de tortillas. Como postre manzana en trozos con linaza', 'Equivalencias: 2 huevos revueltos (2 proteínas) + 1 bistec res 90g (3 proteínas) + 2 tortillas (2 cereales) + ½ manzana (½ fruta) + 1 cda linaza (1 cereal)'),
(3, 'Huevo con jamon.', 'Equivalencias: 1 huevo (1 proteína) + 30g jamón (1 proteína)'),
(3, 'Sandwich de jamon y queso, aparte ensalada de lechuga con manzana y trozos de nuez.', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + 30g jamón (1 proteína) + 30g queso (1 proteína) + 1 taza lechuga (1 verdura) + ½ manzana (½ fruta) + 6 mitades nuez (1 grasa)'),
(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos', 'Equivalencias: 125g yogur (1 lácteo) + 1 cdta linaza/chía (1 cereal) + 1 cda semillas calabaza (1 grasa) + ¼ taza avena (½ cereal) + 6 mitades nuez (1 grasa) + ¼ taza arándanos (½ fruta)'),
(3, 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.', 'Equivalencias: Omelette con ½ taza champiñones (1 verdura) + ½ taza espinacas (1 verdura) + 2 tortillas (2 cereales) + 1 cda semillas calabaza (1 grasa) + 1 pera (1 fruta)'),
(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Equivalencias: 1 taza pepino (1 verdura) + ½ taza zanahoria (1 verdura) + 90g pollo (3 proteínas) + 6 mitades nuez (1 grasa) + 2 tortillas (2 cereales)'),
(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos', 'Equivalencias: 125g yogur (1 lácteo) + 1 cdta linaza/chía (1 cereal) + 1 cda semillas calabaza (1 grasa) + ¼ taza avena (½ cereal) + 6 mitades nuez (1 grasa) + ¼ taza arándanos (½ fruta)'),
(3, 'Sandwich de jamón y queso, aparte ensalada de lechuga con manzana y trozos de nuez.', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + 30g jamón (1 proteína) + 30g queso (1 proteína) + 1 taza lechuga (1 verdura) + ½ manzana (½ fruta) + 6 mitades nuez (1 grasa)'),
(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Equivalencias: 2 huevos (2 proteínas) + 30g jamón (1 proteína) + 30g tocino (1 grasa) + 1 guayaba (½ fruta)'),

-- ============ COMIDAS ============
(4, 'Guisado de lentejas con zanahoria, champiñones y apio. Acompañado de una ensalada de lechuga con trozos de queso y nueces. Naranja de postre', 'Equivalencias: ½ taza lentejas cocidas (1 leguminosa) + ½ taza zanahoria (1 verdura) + ½ taza champiñones (1 verdura) + ½ taza apio (1 verdura) + 1 taza lechuga (1 verdura) + 30g queso (1 proteína) + 6 mitades nuez (1 grasa) + 1 naranja (1 fruta)'),
(4, '90 gr de filete de salmon al horno, papas, pimiento verde, nueces y calabazitas. De postre una naranja.', 'Equivalencias: 90g salmón (3 proteínas) + ½ taza papas (1 cereal) + ½ taza pimiento verde (1 verdura) + 6 mitades nuez (1 grasa) + ½ taza calabazitas (1 verdura) + 1 naranja (1 fruta)'),
(4, 'Ensalada de arroz integral con garbanzo, carne, pepino y aderezo de limón con aceite de oliva. Agua de jamaica sin azúcar.', 'Equivalencias: ½ taza arroz integral (1 cereal) + ½ taza garbanzos (1 leguminosa) + 90g carne (3 proteínas) + ½ pepino (1 verdura) + aderezo limón/aceite (1 grasa)'),
(4, 'Caldo de pollo con sus verduras y tortillas. Agua de limón con chía', 'Equivalencias: 2 tazas caldo pollo (1 proteína) + 1 taza verduras (2 verduras) + 2 tortillas (2 cereales) + agua limón con 1 cda chía (1 cereal)'),
(4, '90gr de puntas de res con espinaca y jitomates con avellanas encima y agua de limón', 'Equivalencias: 90g puntas res (3 proteínas) + 1 taza espinaca (2 verduras) + ½ taza jitomates (1 verdura) + 10 avellanas (1 grasa) + agua limón'),
(4, '90gr de arrachera con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', 'Equivalencias: 90g arrachera (3 proteínas) + ½ taza espárragos (1 verdura) + ½ taza brócoli (1 verdura) + ½ taza champiñones (1 verdura) + 2 tortillas (2 cereales) + 1 pera (1 fruta) + 10 avellanas (1 grasa)'),
(4, 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.', 'Equivalencias: ½ taza lentejas cocidas (1 leguminosa) + ½ taza arroz (1 cereal) + ½ taza champiñones (1 verdura) + ½ taza calabazitas (1 verdura) + 1 pera (1 fruta) + 6 mitades nuez (1 grasa)'),
(4, 'Caldo de garbanzo, chicharo, alverjon, champiñón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.', 'Equivalencias: 2 tazas caldo garbanzos (1 leguminosa) + ½ taza chícharos (½ leguminosa) + ½ taza alverjón (½ leguminosa) + ½ taza champiñones (1 verdura) + ½ taza brócoli (1 verdura) + 2 tacos requesón (1 proteína) + 1 pera (1 fruta) + 6 mitades nuez (1 grasa)'),
(4, 'Carne molida con calabaza, arroz y pimientos, y semillas de calabaza. Una naranja.', 'Equivalencias: 90g carne molida (3 proteínas) + ½ taza calabaza (1 verdura) + ½ taza arroz (1 cereal) + ½ taza pimientos (1 verdura) + 1 cda semillas calabaza (1 grasa) + 1 naranja (1 fruta)'),
(4, 'Carne molida con calabaza, arroz y papas, y semillas de calabaza. Una naranja.', 'Equivalencias: 90g carne molida (3 proteínas) + ½ taza calabaza (1 verdura) + ½ taza arroz (1 cereal) + ½ taza papas (1 cereal) + 1 cda semillas calabaza (1 grasa) + 1 naranja (1 fruta)'),
(4, 'Croquetas de garbanzos con zanahorias, perejil y queso. Todo sobre una cama de lechuga y pepinos.', 'Equivalencias: ½ taza garbanzos cocidos (1 leguminosa) + ½ taza zanahorias (1 verdura) + 30g queso (1 proteína) + 1 taza lechuga (1 verdura) + ½ pepino (1 verdura)'),
(4, 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.', 'Equivalencias: ½ taza lentejas cocidas (1 leguminosa) + ½ taza arroz (1 cereal) + ½ taza champiñones (1 verdura) + ½ taza calabazitas (1 verdura) + 1 pera (1 fruta) + 6 mitades nuez (1 grasa)'),
(4, 'Bisteces de res acompañados de tortilla con lechuga, nueces y agua de limon.', 'Equivalencias: 2 bistecs res 90g (3 proteínas) + 2 tortillas (2 cereales) + 1 taza lechuga (1 verdura) + 6 mitades nuez (1 grasa) + agua limón'),
(4, 'Puntas de res con pico de gallo y agua de limon.', 'Equivalencias: 90g puntas res (3 proteínas) + ½ taza pico de gallo (1 verdura) + agua limón'),
(4, '90gr de pechuga de pollo con espinaca y jitomates con avellanas encima y agua de limon', 'Equivalencias: 90g pechuga pollo (3 proteínas) + 1 taza espinaca (2 verduras) + ½ taza jitomates (1 verdura) + 10 avellanas (1 grasa) + agua limón'),
(4, '90 gr de filete de salmon al horno, papas, pimiento verde, nueces y calabazitas. De postre una naranja.', 'Equivalencias: 90g filete salmón (3 proteínas) + ½ taza papas (1 cereal) + ½ taza pimiento verde (1 verdura) + 6 mitades nuez (1 grasa) + ½ taza calabazitas (1 verdura) + 1 naranja (1 fruta)'),
(4, 'Carne molida de chichero, alvejón, champijón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.', 'Equivalencias: 90g carne molida chícharo/alverjón (3 proteínas) + ½ taza champiñones (1 verdura) + ½ taza brócoli (1 verdura) + 2 tacos requesón (1 proteína) + 1 pera (1 fruta) + 6 mitades nuez (1 grasa)'),
(4, 'Carne molida de galbo y zanahoria rallada. De postre una pera picada en trozos con almendras. Agua de Jamaica.', 'Equivalencias: 90g carne molida garbanzo/zanahoria (3 proteínas) + ½ pera picada (½ fruta) + 10 almendras (1 grasa) + agua jamaica'),
(4, '90gr de roastbeef con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', 'Equivalencias: 90g roast beef (3 proteínas) + ½ taza espárragos (1 verdura) + ½ taza brócoli (1 verdura) + ½ taza champiñones (1 verdura) + 2 tortillas (2 cereales) + 1 pera (1 fruta) + 10 avellanas (1 grasa)'),
(4, '90gr de carne de res con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', 'Equivalencias: 90g carne res (3 proteínas) + ½ taza espárragos (1 verdura) + ½ taza brócoli (1 verdura) + ½ taza champiñones (1 verdura) + 2 tortillas (2 cereales) + 1 pera (1 fruta) + 10 avellanas (1 grasa)'),

-- ============ COLACIONES ============
(5, '1 taza de zanahoria y pepino en bastones acompañada de nuez, limón y chilito.', 'Equivalencias: 1 taza zanahoria (2 verduras) + ½ pepino (1 verdura) + 6 mitades nuez (1 grasa) + limón + chile'),
(5, 'Una taza de pepitas con limón y chile.', 'Equivalencias: 1 taza pepitas (1 grasa) + limón + chile'),
(5, 'Zanahoria y apio con limón y sal.', 'Equivalencias: 1 taza zanahoria (2 verduras) + ½ taza apio (1 verdura) + limón + sal'),
(5, 'Manzana y fresas picadas con avellanas.', 'Equivalencias: ½ manzana (½ fruta) + 6 fresas (1 fruta) + 10 avellanas (1 grasa)'),
(5, 'Palomitas naturales hechas a calor con limón y chilito.', 'Equivalencias: 1 taza palomitas naturales (1 cereal) + limón + chile'),
(5, 'Pepinos con limón', 'Equivalencias: 1 pepino mediano (1 verdura) + limón'),
(5, 'Zanahorias con limón', 'Equivalencias: 1 taza zanahoria (2 verduras) + limón'),
(5, 'Jicama con limón y cacahuates', 'Equivalencias: 1 taza jícama (1 verdura) + limón + 10 cacahuates (1 grasa)'),
(5, 'Pepino con limón y semillas de girasol', 'Equivalencias: 1 pepino mediano (1 verdura) + limón + 1 cda semillas girasol (1 grasa)'),
(5, 'Palomitas naturales hechas a calor con limón y chilito.', 'Equivalencias: 1 taza palomitas naturales (1 cereal) + limón + chile'),
(5, 'Pepino con limón y semillas de girasol', 'Equivalencias: 1 pepino mediano (1 verdura) + limón + 1 cda semillas girasol (1 grasa)'),
(5, 'Pepino con limón y semillas de girasol', 'Equivalencias: 1 pepino mediano (1 verdura) + limón + 1 cda semillas girasol (1 grasa)'),
(5, 'Jícama con limón y cacahuates', 'Equivalencias: 1 taza jícama (1 verdura) + limón + 10 cacahuates (1 grasa)'),
(5, 'Pepino con limón y semillas de girasol', 'Equivalencias: 1 pepino mediano (1 verdura) + limón + 1 cda semillas girasol (1 grasa)'),
(5, 'Jicama con limón y cacahuates', 'Equivalencias: 1 taza jícama (1 verdura) + limón + 10 cacahuates (1 grasa)'),
(5, '1 taza de zanahoria y pepino en bastones acompañada de nuez, limón y chilito.', 'Equivalencias: 1 taza zanahoria (2 verduras) + ½ pepino (1 verdura) + 6 mitades nuez (1 grasa) + limón + chile'),
(5, 'Una taza de pepitas con limón y chile.', 'Equivalencias: 1 taza pepitas (1 grasa) + limón + chile'),
(5, 'Zanahoria y apio con limón y sal.', 'Equivalencias: 1 taza zanahoria (2 verduras) + ½ taza apio (1 verdura) + limón + sal'),
(5, 'Manzana y fresas picadas con avellanas.', 'Equivalencias: ½ manzana (½ fruta) + 6 fresas (1 fruta) + 10 avellanas (1 grasa)'),
(5, 'Palomitas naturales hechas a calor con limón y chilito.', 'Equivalencias: 1 taza palomitas naturales (1 cereal) + limón + chile'),

-- ============ CENAS ============
(6, '1 quesadilla y una naranja', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso panela [1 proteína]) + 1 naranja (1 fruta)'),
(6, 'Pan tostado con fresas y rollitos de jamón.', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + 6 fresas (1 fruta) + 2 rollitos jamón (1 proteína)'),
(6, '2 tacos de queso panela con nopales.', 'Equivalencias: 2 tacos queso panela (2 cereales + 60g queso [2 proteínas]) + ½ taza nopales (1 verdura)'),
(6, 'Pan tostado con pera y queso panela.', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + ½ pera (½ fruta) + 40g queso panela (1 proteína)'),
(6, 'Quesadilla y guayaba', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso [1 proteína]) + 1 guayaba (½ fruta)'),
(6, 'Tacos de atun y de postre fresas', 'Equivalencias: 2 tacos atún (2 tortillas [2 cereales] + ½ lata atún [2 proteínas]) + 6 fresas (1 fruta)'),
(6, 'Quesadillas y una manzana.', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso [1 proteína]) + 1 manzana (1 fruta)'),
(6, 'Pan integral con queso panela y manzana', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + 40g queso panela (1 proteína) + ½ manzana (½ fruta)'),
(6, 'Pan tostado con queso fresco y durazno', 'Equivalencias: 2 rebanadas pan integral (2 cereales) + 40g queso fresco (1 proteína) + ½ durazno (½ fruta)'),
(6, '1 quesadilla y una naranja', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso [1 proteína]) + 1 naranja (1 fruta)'),
(6, 'Un taco de carne molida y de postre una naranja.', 'Equivalencias: 1 taco carne molida (1 tortilla [1 cereal] + 60g carne [2 proteínas]) + 1 naranja (1 fruta)'),
(6, 'Quesadilla y guayaba', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso [1 proteína]) + 1 guayaba (½ fruta)'),
(6, 'Tacos de atun y de postre fresas', 'Equivalencias: 2 tacos atún (2 tortillas [2 cereales] + ½ lata atún [2 proteínas]) + 6 fresas (1 fruta)'),
(6, 'Quesadillas y una manzana.', 'Equivalencias: 1 quesadilla (2 tortillas [2 cereales] + 40g queso [1 proteína]) + 1 manzana (1 fruta)');
"""
cursor.execute(insert_meals)

#sql = """UPDATE meals SET meal_Description = "Equivalencias: 2 rebanadas de pan tostado con 4 fresas rebanadas." WHERE id_Meal = 4"""

#cursor.execute(sql)

""" 5. Meals_Ingredients """
#insert_meals_ingredients = """
#INSERT INTO Meals_Ingredients (id_Meal, id_Ingredients) VALUES 
#(1, 1),  
#(1, 5), 
#(2, 2),  
#(2, 5),  
#(3, 3)   
#"""
#cursor.execute(insert_meals_ingredients)

conn.commit()

##################################################################################################################

conn.close()