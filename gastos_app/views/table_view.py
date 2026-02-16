import reflex as rx
from gastos_app.states.expenses_state import ExpenseState


def expense_table() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Concepto"),
                rx.table.column_header_cell("Importe"),
                rx.table.column_header_cell("Fecha"),
                rx.table.column_header_cell("Categoría"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                ExpenseState.expenses,
                lambda item: rx.table.row(
                    rx.table.cell(item["concept"]),
                    rx.table.cell(item["amount"]),
                    rx.table.cell(item["date"]),
                    rx.table.cell(item["category"]),
                ),
            )
        ),
    )
