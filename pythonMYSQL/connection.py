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

""" AUN NO INSERTO LOS DATOS """
# INSERCIÓN DE 5 REGISTROS POR TABLA

# 1. Ingredient_Types
insert_ingredient_types = """
INSERT INTO Ingredients_Types (Ingredient_Type) VALUES 
('Lácteo'), 
('Carne'), 
('Verdura'), 
('Fruta'), 
('Cereal')
"""
cursor.execute(insert_ingredient_types)

# 2. Ingredients (con el nuevo campo ingredient_Porcion)
insert_ingredients = """
INSERT INTO Ingredients (id_Ingredient_Type, Ingredient_Name, ingredient_Porcion) VALUES 
(1, 'Leche entera', '250 ml'),
(2, 'Pechuga de pollo', '200 g'),
(3, 'Zanahoria', '1 unidad mediana'),
(4, 'Manzana roja', '1 unidad'),
(5, 'Arroz blanco', '1 taza')
"""
cursor.execute(insert_ingredients)

# 3. Meal_Types
insert_meal_types = """
INSERT INTO Meal_Types (meal_Type) VALUES 
('Desayuno'), 
('Almuerzo'), 
('Cena'), 
('Merienda'), 
('Postre')
"""
cursor.execute(insert_meal_types)

# 4. Meals
insert_meals = """
INSERT INTO Meals (id_Meal_Type, meal_Name, meal_Description) VALUES 
(1, 'Desayuno continental', 'Café con leche y tostadas'),
(2, 'Pollo al curry', 'Pollo con salsa curry y arroz'),
(3, 'Ensalada César', 'Ensalada con pollo y aderezo especial'),
(4, 'Yogur con frutas', 'Yogur griego con frutas frescas'),
(5, 'Flan casero', 'Postre de flan de huevo tradicional')
"""
cursor.execute(insert_meals)

# 5. Meals_Ingredients (relaciones)
insert_meals_ingredients = """
INSERT INTO Meals_Ingredients (id_Meal, id_Ingredients) VALUES 
(1, 1),  
(1, 5), 
(2, 2),  
(2, 5),  
(3, 3)   
"""
cursor.execute(insert_meals_ingredients)

conn.commit()

##################################################################################################################

conn.close()