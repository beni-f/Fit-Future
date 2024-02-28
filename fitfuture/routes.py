from fitfuture import app, db, bcrypt
from flask import render_template, url_for, redirect, flash
from fitfuture.db_models import Article, User
from fitfuture.forms import Registration, Login

@app.route('/')
@app.route('/home')
def home():
    """
    Home Page
    """
    articles = db.session.query(Article).all()
    return render_template("home.html", articles=articles)

@app.route('/articles')
def articles():
    """
    Article Page
    """
    articles = db.session.query(Article).all()
    return render_template("article.html", articles=articles)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Account sign up and Login page
    """
    form = Registration()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data, height=form.height.data, weight=form.weight.data, password=hashed_password, gender=form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("account.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    return render_template("login.html", form=form)