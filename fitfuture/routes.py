import os
import secrets
import requests
from fitfuture import app, db, bcrypt
from flask import render_template, url_for, redirect, flash, request, abort
from fitfuture.db_models import Article, User, Workout
from fitfuture.forms import Registration, Login, UpdateAccount, ArticleForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home():
    """
    Home Page
    """
    workouts = []
    if current_user.is_authenticated:
        workouts = db.session.query(Workout).filter_by(user_id=current_user.id).all()
    articles = db.session.query(Article).all()
    return render_template("home.html", articles=articles, workouts=workouts)

@app.route('/articles')
def articles():
    """
    Article Page
    """
    articles = db.session.query(Article).all()
    return render_template("article.html", articles=articles)

@app.route('/articles/new', methods=['GET', 'POST'])
@login_required
def new_article():
    """
    Article Page
    """
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(article)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('articles'))
    return render_template("create_article.html", form=form, legend='Create Article')

@app.route('/articles/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('show_article.html', article=article)

@app.route('/articles/<int:article_id>/update', methods=['GET', 'POST'])
@login_required
def update_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author != current_user:
        abort(403)
    form = ArticleForm()
    if form.validate_on_submit():
        article.title = form.title.data
        article.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('article', article_id=article.id))
    if request.method == 'GET':
        form.title.data = article.title
        form.content.data = article.content
    return render_template("create_article.html", form=form, legend='Update Article')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Account sign up and Login page
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registration()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, username=form.username.data, email=form.email.data, height=form.height.data, weight=form.weight.data, password=hashed_password, gender=form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password.', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename)
    form_picture.save(picture_path)
    return picture_filename
    

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
           picture_file = save_picture(form.picture.data)
           current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", image_file=image_file, form=form)


@app.route('/workout', methods=['GET', 'POST'])
@login_required
def workout():
    if request.method == 'POST':
        day = request.form.get('day')
        muscle_groups = request.form.getlist('muscle-group')
        workout_type = request.form.getlist('workout-type')  # Assuming there's an input for workout type
        # Assuming 'user_id' comes from the current user
        workout = Workout(workout_day=day, muscle_groups=', '.join(muscle_groups), workout_type=', '.join(workout_type), user_id=current_user.id)
        db.session.add(workout)
        db.session.commit()
        flash('Workout data submitted Successfully')
    return render_template("workout.html")

@app.route('/workout/my_workouts')
def my_workouts():
    workouts = []
    if current_user.is_authenticated:
        workouts = db.session.query(Workout).filter_by(user_id=current_user.id).all()
    return render_template("my_workouts.html", workouts=workouts)
@app.route('/success')
def success():
    return 'Workout data submitted successfully!'

@app.route('/about')
def about():
    return render_template("about.html")