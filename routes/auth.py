from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import User
from extensions import db
from flask_login import login_user, logout_user, login_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            flash('Username atau password salah!', 'danger')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('dashboard.home'))

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form.get('role', 'user')

        if User.query.filter_by(username=username).first():
            flash('Username sudah ada!', 'danger')
            return redirect(url_for('auth.register'))

        User.create_user(username, password, role)
        flash('User berhasil dibuat!', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

