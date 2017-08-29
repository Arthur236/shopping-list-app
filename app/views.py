from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/create-list')
def create_list():
    return render_template("create_shopping_list.html")

@app.route('/edit-list')
def edit_list():
    return render_template("edit_shopping_list.html")

@app.route('/view-list')
def view_list():
    return render_template("shopping_list.html")

@app.route('/edit-item')
def edit_item():
    return render_template("shopping_list_items.html")
