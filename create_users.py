from app import app
from models import User

with app.app_context():
    User.create_user('admin', 'admin123', 'admin')
    User.create_user('user1', 'user123', 'user')
    print("✅ Semua user demo dibuat!")

