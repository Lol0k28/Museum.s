from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, file_size
from wtforms.fields import StringField, SubmitField, PasswordField, RadioField, DateField, SelectField, EmailField, \
    TextAreaField
from wtforms.validators import DataRequired, Length, equal_to


# IntegerField,

class AddMuseumForm(FlaskForm):
    title = StringField("მუზეუმის სახელი", validators=[DataRequired()])
    info = StringField("მუზეუმის ინფორმაცია", validators=[DataRequired()])
    img = FileField("მუზეუმის სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpeg", "jpg", "png", "webp", "avif"], message="მხოლოდ სურათები"), file_size(1024 * 1024 * 5, message="ფაილი მაქსიმუმ უნდა იყოს 5 მეგაბაიტი")])
    country = StringField("მუზეუმის მდებარეობა(ქვეყანა)", validators=[DataRequired()])

    submit = SubmitField("დამატება")


class AddArtefactForm(FlaskForm):
    title = StringField("არტეფაქტის სახელი", validators=[DataRequired()])
    info = StringField("არტეფაქტის ინფორმაცია", validators=[DataRequired()])
    artefact_museum = StringField("არტეფაქტის მდებარეობა(მუზეუმი)", validators=[DataRequired()])
    img = FileField("არტეფაქტის სურათის სახელი", validators=[FileRequired(), FileAllowed(["jpeg", "jpg", "png", "webp", "avif"], message="მხოლოდ სურათები"), file_size(1024 * 1024 * 1024 * 5, message="ფაილი მაქსიმუმ უნდა იყოს 64 მეგაბაიტი")])
    submit = SubmitField("დამატება")


class AddCommentForm(FlaskForm):
    username = StringField("Nickname", validators=[DataRequired(), Length(min=1, max=10, message="სახელი არ უნდა იყოს 10 ასოზე მეტი")])
    comment = TextAreaField("ჩაწერეთ კომენტარი", validators=[DataRequired()])
    submit = SubmitField("დამატება")


class UserOpinion(FlaskForm):
    opinion = TextAreaField("თქვენი აზრი",  validators=[DataRequired()])
    submit = SubmitField("გაგზავნა")


class RegisterForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired(message="შეიყვანეთ სახელი !")])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[Length(min=8, max=22, message="პაროლი უნდა იყოს მინიმუმ 8 ასო")])
    repeat_password = PasswordField("გაიმეორეთ პაროლი", validators=[Length(min=8, max=22, message="პაროლი უნდა იყოს მინიმუმ 8 ასო"), equal_to("password", message="პაროლები უნდა ემთხვევოდეს ერთმანეთს")])
    email = EmailField("შეიყვანეთ იმეილი", validators=[DataRequired(message="შეიყვანეთ იმეილი !")])
    birthday = DateField("დაბადების თარიღი", validators=[DataRequired(message="შექრჩიეთ დაბადების თარიღი")])
    gender = RadioField("ამოირჩიეთ სქესი", choices=["კაცი", "ქალი"], validators=[DataRequired(message="შექრჩიეთ სქესი")])
    country = SelectField("მონიშნეთ ქვეყანა", choices=["საქართველო", "საფრანგეთი", "ეგვიპტე"])
    about = TextAreaField("დაწერეთ თქვენს შესახებ")
    favourite_photos = FileField("საყვარელი მუზეუმის სურათი",validators=[FileAllowed(["jpeg", "jpg", "png"], message="მხოლოდ სურათები"), file_size(1024 * 1024 * 5, message="ფაილი მაქსიმუმ უნდა იყოს 5 მეგაბაიტი")])

    submit = SubmitField("რეგისტრაცია")


class AuthorizationForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired(message="შეიყვანეთ სახელი !")])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(message="შეიყვანეთ პაროლი !")])

    submit = SubmitField("ავტორიზაცია")



















