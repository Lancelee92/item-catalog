from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, CategoryItem

import httplib2
import json
from flask import make_response
import requests

engine = create_engine('sqlite:///itemcatalog.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def home():
    categories = session.query(Categories)
    return render_template('home.html', categories=categories)
    #return "homepage with list of Categories"

@app.route('/login')
def showLogin():
    return render_template('login.html')
    #return "Login page"

@app.route('/topNewItem')
def topNewItem():
    items = session.query(CategoryItem).order_by(CategoryItem.time_created.desc()).limit(10)
    return render_template('topNewItem.html', items=items)

@app.route('/category/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Categories(name = request.form['name'], img = request.form['img'])
        session.add(newCategory)
        session.commit()
        flash('New Category Created', 'positive')
        return redirect(url_for('home'))
    else:
        return render_template('newCategory.html')

@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    category = session.query(Categories).filter_by(id = category_id).one()

    if request.method == 'POST':
        category.name = request.form['name']
        category.img = request.form['img']
        session.add(category)
        session.commit()
        flash('Category Edited', 'positive')
        return redirect(url_for('home'))
    else:
        return render_template('editCategory.html', category = category)

@app.route('/categories/<int:category_id>/delete', methods=['GET', 'POST'])
def deleteCategory(category_id):
    category = session.query(Categories).filter_by(id = category_id).one()

    if request.method == 'POST':
        session.delete(category)
        session.commit()
        flash('Item Deleted', 'positive')
        return redirect(url_for('home'))
    else:
        return render_template('deleteCategory.html', category = category)

@app.route('/categories/<int:category_id>/itemlist')
def itemlist(category_id):
    itemlist = session.query(CategoryItem).filter_by(category_id = category_id)
    return render_template('itemlist.html', itemlist = itemlist, category_id = category_id)
    # return "itemlist"

@app.route('/categories/<int:category_id>/itemlist/new', methods=['GET', 'POST'])
def newItemList(category_id):
    if request.method == 'POST':
        newItem = CategoryItem(name = request.form['name'], description = request.form['description'], category_id = category_id)
        session.add(newItem)
        session.commit()
        flash('New Item Created', 'positive')
        return redirect(url_for('itemlist', category_id = category_id))
    else:
        return render_template('newItem.html', category_id = category_id)

@app.route('/categories/<int:category_id>/itemlist/<int:item_id>/edit', methods=['GET', 'POST'])
def editItemList(category_id, item_id):
    category = session.query(Categories).filter_by(id = category_id).one()
    item = session.query(CategoryItem).filter_by(category_id = category_id).filter_by(id=item_id).one()

    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        session.add(item)
        session.commit()
        flash('Item Edited', 'positive')
        return redirect(url_for('itemlist', category_id = category_id))
    else:
        return render_template('editItem.html', item = item,category_name = category.name)

@app.route('/categories/<int:category_id>/itemlist/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItemList(category_id, item_id):
    category = session.query(Categories).filter_by(id = category_id).one()
    item = session.query(CategoryItem).filter_by(category_id = category_id).filter_by(id=item_id).one()

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash('Item Deleted', 'positive')
        return redirect(url_for('itemlist', category_id = category_id))
    else:
        return render_template('deleteItem.html', item = item, category_name = category.name)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)