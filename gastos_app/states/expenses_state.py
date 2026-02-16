import reflex as rx
from sqlmodel import select
from gastos_app.models.expense import Expense
from gastos_app.models.category import Category


class ExpenseState(rx.State):
    expenses: list[dict] = []

    @rx.event
    def get_all_expenses(self):
        with rx.session() as session:
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
