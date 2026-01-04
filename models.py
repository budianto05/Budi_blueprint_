from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# ===========================
# User Model
# ===========================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_user(cls, username, password, role):
        user = cls(username=username, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print(f"User '{username}' dengan role '{role}' berhasil dibuat.")
        return user

# ===========================
# Inventory Model
# ===========================
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Inventory {self.name}>"

