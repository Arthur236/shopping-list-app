"""
Code for rendering the views
"""
from functools import wraps
from flask import request, session, redirect, url_for, render_template, flash

from app import app, user_object, list_object, item_object

def login_required(f):
    """
    Checks if a user is logged in
    """
    @wraps(f)
    def verified(*args, **kwargs):
        """
        Decorated function to check log in status
        """
        if "username" in session:
            return f(*args, **kwargs)
        else:
            msg = "You need to be logged in"
            return render_template("index.html", error=msg)
    return verified

@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    """
    Register a user
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['conf_password']

        status = user_object.register(username, password, cpassword)
        if status == "Registered successfully":
            session['username'] = username
            return render_template('index.html', error=status)
        else:
            return render_template('index.html', resp=status)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Logs in user and renders the user dashboard
    """
    if request.method == 'POST':
        username = request.form['username2']
        password = request.form['password2']

        status = user_object.login(username, password)
        if status == "Login successful":
            session['username'] = username
            user_lists = list_object.show_lists(username)

            return render_template('dashboard.html', shopping_lists=user_lists)
        else:
            return render_template('index.html', resp=status)

@app.route('/create_list', methods=['GET', 'POST'])
@login_required
def create_list():
    """
    View used to create new shopping lists
    """
    user = session['username']

    if request.method == 'POST':
        list_name = request.form['name']
        description = request.form['description']
        status = list_object.create_list(user, list_name, description)

        if isinstance(status, list):
            user_lists = list_object.show_lists(user)
            return render_template('dashboard.html', shopping_lists=user_lists)
        else:
            return render_template("create_shopping_list.html", error=status)

    return render_template("create_shopping_list.html")

@app.route('/edit_list/<name>', methods=['GET', 'POST'])
@login_required
def edit_list(name):
    """
    View used to edit shopping lists
    """
    user = session['username']
    user_lists = list_object.show_lists(user)

    if request.method == 'POST':
        old_name = name
        new_name = request.form['name']
        description = request.form['description']
        status = list_object.update_list(old_name, new_name, description, user)

        if status == list_object.shopping_list:
            response = "" + name + " shopping list successfully updated"
            return render_template('dashboard.html', error=response, shoppinglist=status)
        else:
            return render_template('dashboard.html', error=status, shoppinglist=user_lists)
    
    return render_template("edit_shopping_list.html")

@app.route('/delete_list/<name>', methods=['POST'])
@login_required
def delete_list(name):
    """
    Used to delete shopping list
    """
    user = session['username']
    if request.method == 'POST':
        status = list_object.delete_list(name, user)
        # Delete list items
        item_object.delete_list_items(name)
        response = "Successfuly deleted " + name + " shopping list"
    
    return render_template("dashboard.html", error=response, shopping_lists=status)

@app.route('/view_list/<name>')
@login_required
def view_list(name):
    """
    View for displaying a particular shopping list and all its items
    """
    return render_template("shopping_list.html")

@app.route('/edit_item/<list_name>/<item_name>')
@login_required
def edit_item(list_name, item_name):
    """
    View for editing shopping list items
    """
    return render_template("shopping_list_items.html")

@app.route('/delete_item/<list_name>/<item_name>')
@login_required
def delete_item(list_name, item_name):
    """
    Used for deleting shopping list items
    """
    return render_template("shopping_list_items.html")

@app.route('/logout')
@login_required
def logout():
    """
    Log out a user
    """
    session.pop('logged_in', None)
    msg = "You were logged out"
    return render_template("login.html", error=msg)
