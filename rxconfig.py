import reflex as rx

config = rx.Config(
    app_name="gastos_app",
    api_url="https://rxgastosstaff-production.up.railway.app", 
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)