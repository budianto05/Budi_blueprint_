from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/', methods=['GET'])
@login_required
def home():
    """
    Dashboard utama.
    - Protected: hanya user yang login bisa mengakses (login_required).
    - current_user disediakan oleh Flask-Login (UserMixin).
    - Render template dashboard.html yang sudah dibuat.
    """
    return render_template('dashboard.html')

