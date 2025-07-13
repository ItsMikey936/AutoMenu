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
#        ('Verdura'), 
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
#(1, 'Desayuno continental', 'Café con leche y tostadas'),
#(2, 'Pollo al curry', 'Pollo con salsa curry y arroz'),
#(3, 'Ensalada César', 'Ensalada con pollo y aderezo especial'),
#(4, 'Yogur con frutas', 'Yogur griego con frutas frescas'),
#(5, 'Flan casero', 'Postre de flan de huevo tradicional')
#"""
#cursor.execute(insert_meals)

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