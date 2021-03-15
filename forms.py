from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField('Электронная почта',
                        validators=[InputRequired(), Email(message='Некорректный адрес электронной почты'),
                                    Length(min=2, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Запомнить меня')


class RegisterForm(FlaskForm):
    email = StringField('Электронная почта',
                        validators=[InputRequired(), Email(message='Некорректный адрес электронной почты'),
                                    Length(max=50)])
    username = StringField('Имя пользователя', validators=[InputRequired(), Length(min=2, max=15)])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=8, max=80)])


class DayForm(FlaskForm):
    am1 = StringField('1:00', validators=[Length(max=300)])
    am2 = StringField('2:00', validators=[Length(max=300)])
    am3 = StringField('3:00', validators=[Length(max=300)])
    am4 = StringField('4:00', validators=[Length(max=300)])
    am5 = StringField('5:00', validators=[Length(max=300)])
    am6 = StringField('6:00', validators=[Length(max=300)])
    am7 = StringField('7:00', validators=[Length(max=300)])
    am8 = StringField('8:00', validators=[Length(max=300)])
    am9 = StringField('9:00', validators=[Length(max=300)])
    am10 = StringField('10:00', validators=[Length(max=300)])
    am11 = StringField('11:00', validators=[Length(max=300)])
    am12 = StringField('12:00', validators=[Length(max=300)])
    pm1 = StringField('13:00', validators=[Length(max=300)])
    pm2 = StringField('14:00', validators=[Length(max=300)])
    pm3 = StringField('15:00', validators=[Length(max=300)])
    pm4 = StringField('16:00', validators=[Length(max=300)])
    pm5 = StringField('17:00', validators=[Length(max=300)])
    pm6 = StringField('18:00', validators=[Length(max=300)])
    pm7 = StringField('19:00', validators=[Length(max=300)])
    pm8 = StringField('20:00', validators=[Length(max=300)])
    pm9 = StringField('21:00', validators=[Length(max=300)])
    pm10 = StringField('22:00', validators=[Length(max=300)])
    pm11 = StringField('23:00', validators=[Length(max=300)])
    pm12 = StringField('00:00',validators=[Length(max=300)])