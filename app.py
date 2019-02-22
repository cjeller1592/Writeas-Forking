from flask import Flask, flash, request, render_template, redirect, url_for

from auth import loginUser

from utils import forkCPost
from forms import login, Fork
import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def start():
    global token # Setting token the stupid way! Use this app locally...

    form = login()
    error = None

    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        token = loginUser(user, password)

        if token == None: # catches a bs password or username
            flash('Woops! Try again!')
            return redirect(request.url)

        flash('You successfully logged in! You can start using the app!')
        return redirect(url_for('fork'))

    return render_template('login.html', form=form)


@app.route('/fork', methods=['GET', 'POST'])
def fork():
    form = Fork()
    if request.method == 'POST':
        try:
            alias = request.form['alias']
            slug = request.form['slug']

            url = forkCPost(alias, slug, token)

            if url == None: # catches if alias/slug are off in request
                flash('Hmm something went wrong. Check the alias and or slug!')
                return redirect(url_for('fork'))

            return redirect(url)

        except NameError: # catches if someone tries to use app before logging in
                flash('Easy tiger! Login first . . .')
                return redirect(url_for('start'))


    return render_template('fork.html', form=form)
