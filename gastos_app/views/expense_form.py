import reflex as rx
from gastos_app.states.expenses_state import ExpenseState


def expense_form() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.heading("Nuevo Gasto", size="4"),
            rx.input(
                placeholder="Concepto (ej: Vuelo a Madrid)",
                value=ExpenseState.form_concept,
                on_change=ExpenseState.set_form_concept,
            ),
            rx.input(
                placeholder="Importe",
                type="number",
                value=ExpenseState.form_amount,
                on_change=ExpenseState.set_form_amount,
            ),
            rx.select(
                ExpenseState.category_options,
                placeholder="Categoría",
                value=ExpenseState.form_category,
                on_change=ExpenseState.set_form_category,
            ),
            rx.select(
                ExpenseState.staff_options,
                placeholder="Staff",
                value=ExpenseState.form_staff,
                on_change=ExpenseState.set_form_staff,
            ),
            rx.button(
                "Añadir Gasto",
                on_click=ExpenseState.add_expense,
                width="100%",
            ),
            spacing="3",
            width="100%",
        ),
    )
