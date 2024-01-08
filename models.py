from ext import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class User(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)

    def __init__(self, username, password, role="guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Museum(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    country = db.Column(db.String)
    info = db.Column(db.String)
    img = db.Column(db.String)


class Artefact(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artefact_museum = db.Column(db.String)
    info = db.Column(db.String)
    img = db.Column(db.String)


class Commentaries(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    comment = db.Column(db.String)


class Opinion(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    new_user = User(username="admin_user", password="password", role="Admin")
    new_user.create()
    normal_user = User(username="normal_user", password="password", role="guest")
    new_user.create()
