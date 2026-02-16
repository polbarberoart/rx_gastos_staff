import reflex as rx

config = rx.Config(
    app_name="gastos_app",
    #api_url="https://rxgastosstaff-production.up.railway.app", 
    cors_allowed_origins=[
        "https://rx-gastos-staff.vercel.app",
        "http://localhost:3000"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)