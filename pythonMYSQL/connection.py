import mysql.connector

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

ingredientes = """CREATE TABLE Ingredientes (id_Ingrediente INT AUTO_INCREMENT PRIMARY KEY, nombre_Ingrediente VARCHAR (255), unidad_Ingrediente VARCHAR (20), porcion_Ingrediente DECIMAL(6,2), 
id_Tipo_Ingrediente INT, FOREIGN KEY (id_Tipo_Ingrediente) REFERENCES Tipos_Ingredientes(id_Tipo_Ingrediente))"""
cursor.execute(ingredientes)

#################################################################################################################################################################################




#################################################################################################################################################################################

conn.commit()

conn.close()