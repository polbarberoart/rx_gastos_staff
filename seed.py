import reflex as rx
from gastos_app.models.staff import Staff
from gastos_app.models.category import Category
from gastos_app.models.expense import Expense

def seed_data():
    # 1. Abrimos la conexión con la base de datos
    with rx.session() as session:
        # 2. Creamos una Categoría
        cat_viajes = Category(name="Viajes", description="Gastos de transporte y hotel")
        session.add(cat_viajes)
        
        # 3. Creamos un Staff (Usuario)
        # Nota: En el futuro usaremos una librería para el password_hash
        admin = Staff(
            name="Pol Barbero", 
            email="pol@ejemplo.com", 
            password_hash="hash_super_secreto", 
            role="admin"
        )
        session.add(admin)
        
        # Guardamos primero para que la DB les asigne un ID
        session.commit()
        
        # 4. Creamos un Gasto relacionado con los dos anteriores
        nuevo_gasto = Expense(
            concept="Vuelo a Madrid",
            amount=120.50,
            staff_id=admin.id,      # Usamos el ID generado
            category_id=cat_viajes.id # Usamos el ID generado
        )
        session.add(nuevo_gasto)
        
        # Sello final
        session.commit()
        print("¡Base de datos poblada con éxito!")

if __name__ == "__main__":
    seed_data()