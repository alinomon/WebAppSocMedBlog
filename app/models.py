from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))

class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(200))
    title = db.Column(db.String(100))
    blogBody = db.Column(db.String(500))
    complete = db.Column(db.Boolean)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username1 = db.Column(db.String(200))
    username2 = db.Column(db.String(200))
