from flask import Blueprint, render_template, session, redirect, url_for, flash
from .models import User

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

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




