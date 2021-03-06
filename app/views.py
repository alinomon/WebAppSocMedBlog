from flask import Flask, render_template, flash, redirect, url_for, request, session
from app import app, models, db
from .forms import LogInForm, RegisterForm, BlogPostForm
import pdb
import logging


@app.route('/')
def Landing():
    return render_template('landing.html')

@app.route('/home', methods=['POST', 'GET'])
def Home():
    form = BlogPostForm()
    user = session['username']
    posts = UserPosts(user)
    if request.method=="POST" and form.validate_on_submit():
        blog = models.BlogPosts(owner=user, title=form.title.data, blogBody=form.blogBody.data, complete=False)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('Home'))
    return render_template('home.html', form=form, posts=posts)

@app.route('/login', methods=['POST', 'GET'])
def LogIn():
    #pdb.set_trace()
    form = LogInForm()
    if form.validate_on_submit():
        result = models.Users.query.filter_by(username=form.username.data, password=form.password.data).first()
        if result:
            session['username'] = form.username.data
            return redirect(url_for('Home'))
        return redirect(url_for('LogIn'))
        logging.debug(result)
    return render_template('login.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        reg = models.Users(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(reg)
        db.session.commit()
        logging.debug("Register")
        return redirect(url_for('Landing'))
    return render_template('register.html', form=form)

@app.route('/friends', methods=['POST', 'GET'])
def Friends():
    users = models.Users.query.all()
    friends = CurrentFriends()
    usersFinal = []
    for user in users:
        foundUser = False
        if user.username != session['username']:
            for friend in friends:
                if user.username == friend.username2:
                    foundUser = True
            if foundUser == False:
                usersFinal.append(user)
    logging.debug("Friends")
    return render_template('friends.html', users=usersFinal, friends = friends)

@app.route('/addfriend/<username>', methods=['POST', 'GET'])
def AddFriend(username):
    result = models.Friends(username1 = session['username'], username2 = username)
    users = models.Users.query.all()
    db.session.add(result)
    db.session.commit()
    friends = CurrentFriends()
    usersFinal = []
    for user in users:
        foundUser = False
        if user.username != session['username']:
            for friend in friends:
                if user.username == friend.username2:
                    foundUser = True
            if foundUser == False:
                usersFinal.append(user)
    logging.debug("Friends")
    return render_template('friends.html', users=usersFinal, friends = friends)

def CurrentFriends():
    friends = models.Friends.query.all()
    friendList = []
    for friend in friends:
        if friend.username2 != session['username'] and friend not in friendList:
            friendList.append(friend)
    logging.debug("Friends")
    return friendList

@app.route('/delete/<username>', methods=['POST', 'GET'])
def delete(username):
    friend = models.Friends.query.filter_by(username2 = username).first()
    db.session.delete(friend)
    friendList = CurrentFriends()
    db.session.commit()
    users = models.Users.query.all()
    usersFinal = []
    for user in users:
        foundUser = False
        if user.username != session['username']:
            for friend in friendList:
                if user.username == friend.username2:
                    foundUser = True
            if foundUser == False:
                usersFinal.append(user)
    return render_template('friends.html', users=usersFinal, friends=friendList)

@app.route('/deletepost/<id>', methods=['POST', 'GET'])
def deletepost(id):
    post = models.BlogPosts.query.filter_by(id=int(id)).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('Home'))

def UserPosts(username):
    posts = models.BlogPosts.query.filter_by(owner = username)
    print(posts)

    return posts

@app.route('/profile/<username>', methods=['GET'])
def Profile(username):
    posts = UserPosts(username)
    return render_template('profile.html', posts=posts, username=username)
