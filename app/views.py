"""
Code for rendering the views
"""
from flask import render_template

from app import app

@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    """
    Render the user dashboard
    """
    return render_template("dashboard.html")

@app.route('/create-list')
def create_list():
    """
    View used to create new shopping lists
    """
    return render_template("create_shopping_list.html")

@app.route('/edit-list')
def edit_list():
    """
    View used to edit shopping lists
    """
    return render_template("edit_shopping_list.html")

@app.route('/view-list')
def view_list():
    """
    View for displaying a particular shopping list and all its items
    """
    return render_template("shopping_list.html")

@app.route('/edit-item')
def edit_item():
    """
    View for editing shopping list items
    """
    return render_template("shopping_list_items.html")
