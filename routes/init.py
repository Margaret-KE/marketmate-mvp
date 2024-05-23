from .products import products_bp
from .users import users_bp

# Define blueprints for products and users
def init_app(app):
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
