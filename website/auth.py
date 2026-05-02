from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

# ---------------- SIGNUP ----------------
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        # Duplicate email check
        if User.query.filter_by(email=email).first():
            flash("This email is already registered")
            return render_template("base.html", name=name, email=email, phone=phone)

        # Password match check
        if password != confirm_password:
            flash("Passwords do not match")
            return render_template("base.html", name=name, email=email, phone=phone)

        # Create user
        new_user = User(
            name=name,
            email=email,
            phone=phone,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        # Log the user in
        session['user_id'] = new_user.id
        return redirect(url_for('views.dashboard'))
    
    # print(request.form)

    return render_template("base.html")


# ---------------- LOGIN ----------------
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Email not found")
            return render_template("login.html", email=email)

        if not check_password_hash(user.password, password):
            flash("Incorrect password!")
            return render_template("login.html", email=email)

        session['user_id'] = user.id
        return redirect(url_for('views.dashboard'))

    return render_template("login.html")


# ---------------- LOGOUT ----------------
@auth.route("/logout")
def logout():
    session.pop('user_id', None)
    flash("Logged out successfully")
    return redirect(url_for('auth.login'))









