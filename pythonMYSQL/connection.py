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
#tableCreation = """CREATE TABLE Meals_Ingredients (id_Meal_Ingredient INT AUTO_INCREMENT PRIMARY KEY, id_Ingredient INT, id_Meal INT, FOREIGN KEY (id_Meal) REFERENCES meals(id_Meal), FOREIGN KEY (id_Ingredient) REFERENCES ingredients(id_Ingredient))"""
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
#insert_meals = """
#INSERT INTO Meals (id_Meal_Type, meal_Name, meal_Description) VALUES 
#(1, 'Pan tostado con guayaba rebanada', 'Pan tostado con guayaba rebanada'),
#(1, 'Manzana picada con amaranto', 'Manzana picada con amaranto'),
#(1, 'Pan tostado con fresas', 'Pan tostado con fresas'),
#(1, 'Pan tostado con manzana rebanada', 'Pan tostado con manzana rebanada'),
#(1, 'Pera picada con amaranto', 'Pera picada con amaranto'),
#(1, 'Tazon de avena cocida con durazno picado', 'Tazon de avena cocida con durazno picado'),
#(1, 'Un tazon de durazno con nuez en trozos', 'Un tazon de durazno con nuez en trozos'),
#(1, 'Avena cocida con manzana en trozos.', 'Avena cocida con manzana en trozos.'),
#(1, 'Pan tostado con fresas', 'Pan tostado con fresas'),
#(1, 'Un tazón de durazno con nuez en trozos', 'Un tazón de durazno con nuez en trozos'),
#(1, 'Manzana picada con amaranto', 'Manzana picada con amaranto'),
#(1, 'Pera picada con amaranto', 'Pera picada con amaranto'),
#(1, 'Avena cocida con manzana en trozos.', 'Avena cocida con manzana en trozos.'),
#(1, 'Un tazon de durazno con nuez en trozos', 'Un tazon de durazno con nuez en trozos'),
#(1, 'Manzana picada con amaranto', 'Manzana picada con amaranto'),
#(1, 'Pera picada con amaranto', 'Pera picada con amaranto'),
#(1, 'Avena cocida con manzana en trozos.', 'Avena cocida con manzana en trozos.'),
#(1, 'Manzana picada con amaranto', 'Manzana picada con amaranto'),
#(1, 'Avena cocida con manzana en trozos.', 'Avena cocida con manzana en trozos.'),
#(1, 'Pera picada con amaranto', 'Pera picada con amaranto'),
#(1, 'Pan tostado con fresas', 'Pan tostado con fresas'),
#(2, 'Batido de manzana con nuez y 1/4 de taza de avena', 'Batido de manzana con nuez y 1/4 de taza de avena'),
#(2, 'Batido de fresa con amaranto y nueces.', 'Batido de fresa con amaranto y nueces.'),
#(2, 'Batido de fresa con amaranto y nuez.', 'Batido de fresa con amaranto y nuez.'),
#(2, 'Batido de manzana con chía y avena.', 'Batido de manzana con chía y avena.'),
#(2, 'Batido de pera y manzana con almendras y avena.', 'Batido de pera y manzana con almendras y avena.'),
#(2, 'Batido de fresa con nueces y linaza.', 'Batido de fresa con nueces y linaza.'),
#(2, 'Batido de fresa con amaranto y nueces.', 'Batido de fresa con amaranto y nueces.'),
#(2, 'Batido de manzana con chía y avena.', 'Batido de manzana con chía y avena.'),
#(2, 'Batido de fresa con nueces y linaza.', 'Batido de fresa con nueces y linaza.'),
#(2, 'Batido de pera y manzana con almendras y avena.', 'Batido de pera y manzana con almendras y avena.'),
#(2, 'Batido de fresa con amaranto y nueces.', 'Batido de fresa con amaranto y nueces.'),
#(2, 'Batido de manzana con chía y avena.', 'Batido de manzana con chía y avena.'),
#(2, 'Batido de fresa con nueces y linaza.', 'Batido de fresa con nueces y linaza.'),
#(2, 'Batido de pera y manzana con almendras y avena.', 'Batido de pera y manzana con almendras y avena.'),
#(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.'),
#(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cúlta de linaza, chia, semillas de calabaza, avena, nuez picada, arándanos', 'Bowl: 125g de yogurt (1 tarrito) + 1 cúlta de linaza, chia, semillas de calabaza, avena, nuez picada, arándanos'),
#(3, 'Avena cocida, manzana picada y nuez. Acompañados de dos huevos revueltos.', 'Avena cocida, manzana picada y nuez. Acompañados de dos huevos revueltos.'),
#(3, '1 sándwich de atún con mostaza y verduras (lechuga, pepino, zanahoria rallada).', '1 sándwich de atún con mostaza y verduras (lechuga, pepino, zanahoria rallada).'),
#(3, 'Ensalada de garbanzo, calabaza y pepino con nueces. Y de postre pan tostado con fresas.', 'Ensalada de garbanzo, calabaza y pepino con nueces. Y de postre pan tostado con fresas.'),
#(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Huevo con jamón y tocino acompañado de guayaba.'),
#(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.'),
#(3, 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.', 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.'),
#(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Huevo con jamón y tocino acompañado de guayaba.'),
#(3, 'Huevos revueltos con tocino', 'Huevos revueltos con tocino'),
#(3, 'Huevos revueltos con bistec de res acompañado de tortillas. Como postre manzana en trozos con linaza', 'Huevos revueltos con bistec de res acompañado de tortillas. Como postre manzana en trozos con linaza'),
#(3, 'Huevo con jamon.', 'Huevo con jamon.'),
#(3, 'Sandwich de jamon y queso, aparte ensalada de lechuga con manzana y trozos de nuez.', 'Sandwich de jamon y queso, aparte ensalada de lechuga con manzana y trozos de nuez.'),
#(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos', 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos'),
#(3, 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.', 'Omellete de champiñones y espinacas con 2 tortillas, semillas de calabaza y una pera.'),
#(3, 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.', 'Ensalada de pepino y zanahoria con fajitas de pollo y nuez con tortillas.'),
#(3, 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos', 'Bowl: 125g de yogurt (1 tarrito) + 1 cdita de linaza, chía, semillas de calabaza, avena, nuez picada, arándanos'),
#(3, 'Sandwich de jamón y queso, aparte ensalada de lechuga con manzana y trozos de nuez.', 'Sandwich de jamón y queso, aparte ensalada de lechuga con manzana y trozos de nuez.'),
#(3, 'Huevo con jamón y tocino acompañado de guayaba.', 'Huevo con jamón y tocino acompañado de guayaba.'),
#(4, 'Guisado de lentejas con zanahoria, champiñones y apio. Acompañado de una ensalada de lechuga con trozos de queso y nueces. Naranja de postre', 'Guisado de lentejas con zanahoria, champiñones y apio. Acompañado de una ensalada de lechuga con trozos de queso y nueces. Naranja de postre'),
#(4, '90 gr de filete de salmon al horno, papas, pimiento verde, nueces y calabazitas. De postre una naranja.', '90 gr de filete de salmon al horno, papas, pimiento verde, nueces y calabazitas. De postre una naranja.'),
#(4, 'Ensalada de arroz integral con garbanzo, carne, pepino y aderezo de limón con aceite de oliva. Agua de jamaica sin azúcar.', 'Ensalada de arroz integral con garbanzo, carne, pepino y aderezo de limón con aceite de oliva. Agua de jamaica sin azúcar.'),
#(4, 'Caldo de pollo con sus verduras y tortillas. Agua de limón con chía', 'Caldo de pollo con sus verduras y tortillas. Agua de limón con chía'),
#(4, '90gr de puntas de res con espinaca y jitomates con avellanas encima y agua de limón', '90gr de puntas de res con espinaca y jitomates con avellanas encima y agua de limón'),
#(4, '90gr de arrachera con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', '90gr de arrachera con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.'),
#(4, 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.', 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.'),
#(4, 'Caldo de garbanzo, chicharo, alverjon, champiñón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.', 'Caldo de garbanzo, chicharo, alverjon, champiñón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.'),
#(4, 'Carne molida con calabaza, arroz y pimientos, y semillas de calabaza. Una naranja.', 'Carne molida con calabaza, arroz y pimientos, y semillas de calabaza. Una naranja.'),
#(4, 'Carne molida con calabaza, arroz y papas, y semillas de calabaza. Una naranja.', 'Carne molida con calabaza, arroz y papas, y semillas de calabaza. Una naranja.'),
#(4, 'Croquetas de garbanzos con zanahorias, perejil y queso. Todo sobre una cama de lechuga y pepinos.', 'Croquetas de garbanzos con zanahorias, perejil y queso. Todo sobre una cama de lechuga y pepinos.'),
#(4, 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.', 'Lentejas guisadas con arroz y champiñones con calabazitas. De postre una pera con nueces.'),
#(4, 'Bisteces de res acompañados de tortilla con lechuga, nueces y agua de limon.', 'Bisteces de res acompañados de tortilla con lechuga, nueces y agua de limon.'),
#(4, 'Puntas de res con pico de gallo y agua de limon.', 'Puntas de res con pico de gallo y agua de limon.'),
#(4, '90gr de pechuga de pollo con espinaca y jitomates con avellanas encima y agua de limon', '90gr de pechuga de pollo con espinaca y jitomates con avellanas encima y agua de limon'),
#(4, 'Carne molida de chichero, alvejón, champijón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.', 'Carne molida de chichero, alvejón, champijón y brocoli, acompañado de tacos de requesón. De postre una pera picada con nuez.'),
#(4, 'Carne molida de galbo y zanahoria rallada. De postre una pera picada en trozos con almendras. Agua de Jamaica.', 'Carne molida de galbo y zanahoria rallada. De postre una pera picada en trozos con almendras. Agua de Jamaica.'),
#(4, '90gr de roastbeef con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', '90gr de roastbeef con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.'),
#(4, '90gr de carne de res con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.', '90gr de carne de res con esparragos, brocoli y champiñones con tortillas. De postre una pera con avellanas.'),
#(5, '1 taza de zanahoria y pepino en bastones acompañada de nuez, limón y chilito.', '1 taza de zanahoria y pepino en bastones acompañada de nuez, limón y chilito.'),
#(5, 'Una taza de pepitas con limón y chile.', 'Una taza de pepitas con limón y chile.'),
#(5, 'Zanahoria y apio con limón y sal.', 'Zanahoria y apio con limón y sal.'),
#(5, 'Manzana y fresas picadas con avellanas.', 'Manzana y fresas picadas con avellanas.'),
#(5, 'Palomitas naturales hechas a calor con limón y chilito.', 'Palomitas naturales hechas a calor con limón y chilito.'),
#(5, 'Pepinos con limón', 'Pepinos con limón'),
#(5, 'Zanahorias con limón', 'Zanahorias con limón'),
#(5, 'Jicama con limón y cacahuates', 'Jicama con limón y cacahuates'),
#(5, 'Pepino con limón y semillas de girasol', 'Pepino con limón y semillas de girasol'),
#(5, 'Palomitas naturales hechas a calor con limón y chilito.', 'Palomitas naturales hechas a calor con limón y chilito.'),
#(5, 'Pepino con limón y semillas de girasol', 'Pepino con limón y semillas de girasol'),
#(5, 'Pepino con limón y semillas de girasol', 'Pepino con limón y semillas de girasol'),
#(5, 'Jícama con limón y cacahuates', 'Jícama con limón y cacahuates'),
#(5, 'Pepino con limón y semillas de girasol', 'Pepino con limón y semillas de girasol'),
#(5, 'Jicama con limón y cacahuates', 'Jicama con limón y cacahuates'),
#(6, '1 quesadilla y una naranja', '1 quesadilla y una naranja'),
#(6, 'Pan tostado con fresas y rollitos de jamón.', 'Pan tostado con fresas y rollitos de jamón.'),
#(6, '2 tacos de queso panela con nopales.', '2 tacos de queso panela con nopales.'),
#(6, 'Pan tostado con pera y queso panela.', 'Pan tostado con pera y queso panela.'),
#(6, 'Quesadilla y guayaba', 'Quesadilla y guayaba'),
#(6, 'Tacos de atun y de postre fresas', 'Tacos de atun y de postre fresas'),
#(6, 'Quesadillas y una manzana.', 'Quesadillas y una manzana.'),
#(6, 'Pan integral con queso panela y manzana', 'Pan integral con queso panela y manzana'),
#(6, 'Pan tostado con queso fresco y durazno', 'Pan tostado con queso fresco y durazno'),
#(6, 'Un taco de carne molida y de postre una naranja.', 'Un taco de carne molida y de postre una naranja.'),
#(6, 'Quesadilla y guayaba', 'Quesadilla y guayaba'),
#(6, 'Tacos de atun y de postre fresas', 'Tacos de atun y de postre fresas'),
#(6, 'Quesadillas y una manzana.', 'Quesadillas y una manzana.');
#"""
#cursor.execute(insert_meals)

sql = """UPDATE meals SET meal_Description = "Eo" WHERE id_Meal = 1"""

cursor.execute(sql)

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