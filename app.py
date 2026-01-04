from flask import Flask
from extensions import db, login_manager
from models import User
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.inventory import inventory_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db & login_manager
db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/')
app.register_blueprint(inventory_bp, url_prefix='/inventory')

# create database if not exists
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
