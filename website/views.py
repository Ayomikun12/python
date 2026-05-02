from flask import Blueprint, render_template, session, redirect, url_for, flash
from .models import User


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return redirect(url_for('auth.login'))  # redirect to login page

@views.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        flash("Please log in first")
        return redirect(url_for('auth.login'))

    user = User.query.get(user_id)
    return render_template("dashboard.html", user=user)

@views.route('/index')
def index():
    return render_template("index.html")




