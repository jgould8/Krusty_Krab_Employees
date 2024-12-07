from . import orders, resources, ratings, promotions, payment, menu_items, customers


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(resources.router)
    app.include_router(ratings.router)
    app.include_router(promotions.router)
    app.include_router(payment.router)
    app.include_router(menu_items.router)
    app.include_router(customers.router)
