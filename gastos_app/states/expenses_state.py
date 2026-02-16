import reflex as rx
from sqlmodel import select
from datetime import datetime
from gastos_app.models.expense import Expense
from gastos_app.models.category import Category
from gastos_app.models.staff import Staff


class ExpenseState(rx.State):
    # Datos de la tabla
    expenses: list[dict] = []

    # Opciones para los dropdowns del formulario
    category_options: list[str] = []
    staff_options: list[str] = []

    # Campos del formulario (todos str porque vienen del frontend)
    form_concept: str = ""
    form_amount: str = ""
    form_category: str = ""
    form_staff: str = ""

    @rx.event
    def load_data(self):
        """Carga todo lo necesario: gastos para la tabla + opciones para el form."""
        with rx.session() as session:
            # Gastos con JOIN a categoría
            results = session.exec(
                select(Expense, Category.name).join(Category)
            ).all()

            self.expenses = [
                {
                    "id": expense.id,
                    "concept": expense.concept,
                    "amount": f"{expense.amount:.2f} €",
                    "date": expense.date.strftime("%d/%m/%Y"),
                    "category": category_name,
                }
                for expense, category_name in results
            ]

            # Opciones para los dropdowns
            self.category_options = [
                c.name for c in session.exec(select(Category)).all()
            ]
            self.staff_options = [
                s.name for s in session.exec(select(Staff)).all()
            ]

    @rx.event
    def add_expense(self):
        """Crea un gasto nuevo en la DB y recarga la tabla."""
        # Validación básica: todos los campos obligatorios
        if not all([self.form_concept, self.form_amount, self.form_category, self.form_staff]):
            return

        with rx.session() as session:
            # Buscamos los IDs a partir de los nombres seleccionados
            category = session.exec(
                select(Category).where(Category.name == self.form_category)
            ).first()
            staff = session.exec(
                select(Staff).where(Staff.name == self.form_staff)
            ).first()

            if not category or not staff:
                return

            new_expense = Expense(
                concept=self.form_concept,
                amount=float(self.form_amount),
                date=datetime.now(),
                staff_id=staff.id,
                category_id=category.id,
            )
            session.add(new_expense)
            session.commit()

        # Limpiar el formulario
        self.form_concept = ""
        self.form_amount = ""
        self.form_category = ""
        self.form_staff = ""

        # Recargar la tabla con el nuevo gasto
        self.load_data()
