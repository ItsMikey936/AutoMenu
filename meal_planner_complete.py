"""
SCRIPT PRINCIPAL COMPLETO
Este es el archivo final que integra todo el sistema
"""

import mysql.connector
from collections import defaultdict
import random
from datetime import datetime
import os

class CompleteMealPlanner:
    """
    Clase completa del planificador de comidas
    Integra todas las funcionalidades en una sola clase
    """
    
    
    def __init__(self, host='localhost', user='root', password='', database='test'):
        """Inicializa el planificador"""
        self.db_config = {
            'host': host,
            'user': user, 
            'password': password,
            'database': database
        }
        
        self.meal_types = {
            1: "Al despertar",
            2: "Batido",
            3: "Almuerzo", 
            4: "Comida",
            5: "Colación",
            6: "Cena"
        }
        
        self.days_of_week = [
            "Lunes", "Martes", "Miércoles", "Jueves",
            "Viernes", "Sábado", "Domingo"
        ]
        
        self.connection = None
        self.cursor = None
        self.meals_data = {}
        self.current_weekly_plan = {}
        self.used_meals_this_week = set()
    
    def connect_to_database(self):
        """Conecta a la base de datos"""
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            return True
        except mysql.connector.Error as e:
            print(f"❌ Error de conexión: {e}")
            return False
    
    def load_meals_from_database(self):
        """Carga todas las comidas de la base de datos"""
        if not self.connection:
            if not self.connect_to_database():
                return False
        
        try:
            query = """
            SELECT id_Meal, meal_Name, meal_Description, id_Meal_Type
            FROM meals
            ORDER BY id_Meal_Type, meal_Name
            """
            
            self.cursor.execute(query)
            meals = self.cursor.fetchall()
            
            self.meals_data = defaultdict(list)
            
            for meal in meals:
                id_meal, name, description, meal_type = meal
                meal_info = {
                    'id': id_meal,
                    'name': name,
                    'description': description,
                    'type_id': meal_type
                }
                self.meals_data[meal_type].append(meal_info)
            
            return True
            
        except mysql.connector.Error as e:
            print(f"❌ Error al cargar comidas: {e}")
            return False
    
    def generate_weekly_plan(self):
        """Genera un plan semanal completo sin repeticiones"""
        print("\n🗓️ GENERANDO PLAN SEMANAL SIN REPETICIONES")
        print("=" * 60)
        
        # Reiniciar variables
        self.current_weekly_plan = {}
        self.used_meals_this_week = set()
        
        # Verificar que hay suficientes comidas
        for type_id, type_name in self.meal_types.items():
            available_count = len(self.meals_data[type_id])
            if available_count < 7:
                print(f"⚠️ {type_name}: solo {available_count} opciones (se necesitan 7)")
        
        # Generar plan día por día
        for day in self.days_of_week:
            daily_plan = {}
            print(f"\n📅 Planificando {day}...")
            
            for meal_type_id, meal_type_name in self.meal_types.items():
                # Obtener comidas disponibles de este tipo
                available_meals = self.meals_data[meal_type_id]
                
                # Filtrar comidas no usadas esta semana
                unused_meals = [
                    meal for meal in available_meals 
                    if meal['id'] not in self.used_meals_this_week
                ]
                
                if unused_meals:
                    # Seleccionar aleatoriamente
                    selected_meal = random.choice(unused_meals)
                    self.used_meals_this_week.add(selected_meal['id'])
                    daily_plan[meal_type_name] = selected_meal
                else:
                    # No hay más opciones sin usar
                    if available_meals:
                        selected_meal = random.choice(available_meals)
                        daily_plan[meal_type_name] = selected_meal
                    else:
                        daily_plan[meal_type_name] = None
            
            self.current_weekly_plan[day] = daily_plan
        
        return self.current_weekly_plan
    
    def display_weekly_plan(self):
        """Muestra el plan semanal completo"""
        if not self.current_weekly_plan:
            print("⚠️ No hay plan generado")
            return
        
        print("\n📋 PLAN SEMANAL DE COMIDAS")
        print("=" * 80)
        
        for day, daily_plan in self.current_weekly_plan.items():
            print(f"\n🗓️ {day.upper()}")
            print("-" * 50)
            
            for meal_type, meal in daily_plan.items():
                if meal:
                    print(f"  {meal_type:15}:  | {meal['name']} | {meal['description']}")
                else:
                    print(f"  {meal_type:15} | ❌ No disponible")
    
    def save_plan_to_file(self, filename=None):
        """Guarda el plan en un archivo"""
        if not self.current_weekly_plan:
            print("⚠️ No hay plan para guardar")
            return
        
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"plan_semanal_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("PLAN DE COMIDAS SEMANAL\n")
                f.write("=" * 50 + "\n")
                f.write(f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
                
                for day, daily_plan in self.current_weekly_plan.items():
                    f.write(f"\n🗓️ {day.upper()}")
                    f.write("-" * 50)

                    for meal_type, meal in daily_plan.items():
                        if meal:
                            f.write(f"  {meal_type:15}:  | {meal['name']} | {meal['description']}")
                        else:
                            f.write(f"  {meal_type:15} | ❌ No disponible")
                        
                    
                    
                    f.write("\n")
            
            print(f"✅ Plan guardado en: {filename}")
            return filename
            
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
            return None
    
    def close_connection(self):
        """Cierra la conexión a la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

def main():
    """Función principal del programa"""
    print("🍽️ PLANIFICADOR DE COMIDAS SEMANAL")
    print("=" * 50)
    
    # Crear planificador
    planner = CompleteMealPlanner()
    
    try:
        # Conectar y cargar datos
        print("🔌 Conectando a base de datos...")
        if not planner.connect_to_database():
            print("❌ No se pudo conectar. Verifica tu configuración.")
            return
        
        print("📥 Cargando comidas...")
        if not planner.load_meals_from_database():
            print("❌ No se pudieron cargar las comidas.")
            return
        
        print("✅ Datos cargados correctamente")
        
        # Menú interactivo
        while True:
            print("\n" + "="*50)
            print("📋 OPCIONES DISPONIBLES:")
            print("1. 📋 Generar y ver plan actual")
            print("2. 💾 Guardar plan en archivo")
            print("3. ❌ Salir")
            print("="*50)
            
            opcion = input("\nSelecciona una opción (1-3): ").strip()
            
            if opcion == "1":
                planner.generate_weekly_plan()
                planner.display_weekly_plan()
                
            elif opcion == "2":
                filename = input("Nombre del archivo (Enter para automático): ").strip()
                if not filename:
                    filename = None
                planner.save_plan_to_file(filename)
                
            elif opcion == "3":
                print("\n👋 ¡Hasta luego!")
                break
                
            else:
                print("❌ Opción no válida")
            
            input("\nPresiona Enter para continuar...")
    
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido")
    
    finally:
        planner.close_connection()
        print("🔌 Conexión cerrada")

if __name__ == "__main__":
    main()
