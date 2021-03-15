from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from forms import LoginForm, RegisterForm, DayForm

app = Flask(__name__)
Bootstrap(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timeline.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'VERYSECRETKEY'
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    am1 = db.Column(db.String(200), nullable=True)
    am2 = db.Column(db.String(200), nullable=True)
    am3 = db.Column(db.String(200), nullable=True)
    am4 = db.Column(db.String(200), nullable=True)
    am5 = db.Column(db.String(200), nullable=True)
    am6 = db.Column(db.String(200), nullable=True)
    am7 = db.Column(db.String(200), nullable=True)
    am8 = db.Column(db.String(200), nullable=True)
    am9 = db.Column(db.String(200), nullable=True)
    am10 = db.Column(db.String(200), nullable=True)
    am11 = db.Column(db.String(200), nullable=True)
    am12 = db.Column(db.String(200), nullable=True)
    pm1 = db.Column(db.String(200), nullable=True)
    pm2 = db.Column(db.String(200), nullable=True)
    pm3 = db.Column(db.String(200), nullable=True)
    pm4 = db.Column(db.String(200), nullable=True)
    pm5 = db.Column(db.String(200), nullable=True)
    pm6 = db.Column(db.String(200), nullable=True)
    pm7 = db.Column(db.String(200), nullable=True)
    pm8 = db.Column(db.String(200), nullable=True)
    pm9 = db.Column(db.String(200), nullable=True)
    pm10 = db.Column(db.String(200), nullable=True)
    pm11 = db.Column(db.String(200), nullable=True)
    pm12 = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=("POST", "GET"))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.psw, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('timeline', name=current_user.name))
        return "<h1> Неправильное имся пользователя или пароль"
    return render_template('login.html', form=form)


@app.route('/register', methods=("POST", "GET"))
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            hash = generate_password_hash(form.password.data)
            u = User(name=form.username.data, email=form.email.data, psw=hash)
            db.session.add(u)
            db.session.flush()
            db.session.commit()
            return "<h1> всё заебись ёпта </h1>"
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            db.session.rollback()
    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/timeline/<name>')
@login_required
def timeline(name):
    day = Day.query.filter(Day.user_id == current_user.id).order_by(Day.id.desc()).first()
    return render_template('timeline.html', day=day)


@app.route('/timeline/<name>/change', methods=('POST', 'GET'))
@login_required
def change(name):
    form = DayForm()

    if form.validate_on_submit():
        try:
            d = Day(
                am1=form.am1.data,
                am2=form.am2.data,
                am3=form.am3.data,
                am4=form.am4.data,
                am5=form.am5.data,
                am6=form.am6.data,
                am7=form.am7.data,
                am8=form.am8.data,
                am9=form.am9.data,
                am10=form.am10.data,
                am11=form.am11.data,
                am12=form.am12.data,
                pm1=form.pm1.data,
                pm2=form.pm2.data,
                pm3=form.pm3.data,
                pm4=form.pm4.data,
                pm5=form.pm5.data,
                pm6=form.pm6.data,
                pm7=form.pm7.data,
                pm8=form.pm8.data,
                pm9=form.pm9.data,
                pm10=form.pm10.data,
                pm11=form.pm11.data,
                pm12=form.pm12.data,
                user_id=current_user.id

            )
            db.session.add(d)
            db.session.flush()
            db.session.commit()
            return redirect(url_for('timeline', name=current_user.name))

        except:
            db.session.rollback()
            print('Ошибка добавления в БД')
    return render_template('change.html', title='Главная', name=current_user.name, form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
