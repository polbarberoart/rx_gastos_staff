"""Gastos Staff - Sistema de registro de gastos."""

import reflex as rx

# Importamos los modelos para que Reflex registre las tablas en la DB
from .models import Staff, Category, Expense

# Importamos estado y vistas
from .states import ExpenseState
from .views import expense_table, expense_form


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Gastos Staff", size="9"),
            expense_form(),
            expense_table(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index, on_load=ExpenseState.load_data)
