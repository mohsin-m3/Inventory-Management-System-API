from flask import Flask
from config import Config
from src.models import db
from src.routes_auth import auth_bp
from src.routes_products import product_bp
from src.routes_orders import order_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(product_bp, url_prefix='/api/products')
app.register_blueprint(order_bp, url_prefix='/api/orders')

@app.route('/')
def home():
    return {'message': 'Inventory API Running'}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)