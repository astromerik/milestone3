import os
from functools import wraps
from flask import Flask, render_template, session, request, redirect, url_for
from flask_pymongo import PyMongo
from passlib.hash import pbkdf2_sha256
import env
from bson.objectid import ObjectId


# Start application
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "components"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = "+h`%FHZpbRi|del2!87OJ)Rh_!k|zbOAf>EpJ~)L_Sn>p((]^r|%J,aP,me.18|"
mongo = PyMongo(app)

coll = mongo.db


def checked_logged_in(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        if 'logged-in' in session:
            return(func(*args, **kwargs))
        else:
            return render_template('notloggedin.html')
    return wrapped_function

# Display home page
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", projects=coll.projects.find_one())


# Display and filter projects

@app.route('/projects', methods=['POST', 'GET'])
def projects():
    casemat = request.form.get('casemat')
    size = request.form.get('size')
    layout = request.form.get('layout')

    # Handle POST request
    if request.method == 'POST':
        query = {}

        if casemat != 'none':
            query['caseMaterial'] = casemat

        if layout != 'none':
            query['layout'] = layout

        if size != 'none':
            query['layoutSize'] = size

        all_projects = coll.projects.find(query)

    # Handle GET request
    else:
        all_projects = coll.projects.find()

    return render_template("projects.html",
                           casematerial=coll.caseMaterial.find(),
                           size=coll.layoutSize.find(),
                           layout=coll.layout.find(),
                           casemat=casemat,
                           projects=all_projects)


# Build a keyboard
@app.route('/build')
@checked_logged_in
def build():
    return render_template("build.html",
                           casematerial=coll.caseMaterial.find(),
                           size=coll.layoutSize.find(),
                           layout=coll.layout.find(),
                           projects=coll.projects.find(),
                           casebrand=coll.caseBrand.find(),
                           switchbrand=coll.keyswitchBrand.find(),
                           switchtype=coll.cherry.find())

# Takes the user input and passes it to the database to build keyboard
@app.route('/insert_build', methods=['POST'])
def insert_build():
    coll.projects.insert_one(request.form.to_dict())
    return redirect(url_for('projects'))

# View the projects indepth
@app.route('/view_project/<project_id>')
def view_project(project_id):
    if ObjectId.is_valid(project_id):
        the_project = coll.projects.find_one({'_id': ObjectId(project_id)})
        return render_template('viewproject.html', projects=the_project)

# Edit existing keyboard
@app.route('/edit_project/<project_id>')
@checked_logged_in
def edit_project(project_id):
    if ObjectId.is_valid(project_id):
        the_projects = coll.projects.find_one({'_id': ObjectId(project_id)})
        return render_template('editdelete.html', projects=the_projects,
                               casematerial=coll.caseMaterial.find(),
                               size=coll.layoutSize.find(),
                               layout=coll.layout.find(),
                               casebrand=coll.caseBrand.find(),
                               switchbrand=coll.keyswitchBrand.find(),
                               switchtype=coll.cherry.find())

# Update project
@app.route('/update_project/<project_id>', methods=['POST'])
def update_project(project_id):
    coll.projects.update({'_id': ObjectId(project_id)},
                         {'projectName': request.form.get('projectName'),
                          'caseBrand': request.form.get('caseBrand'),
                          'caseMaterial': request.form.get('caseMaterial'),
                          'keyboardSize': request.form.get('keyboardSize'),
                          'keyboardLayout': request.form.get('keyboardLayout'),
                          'keyswitchBrand': request.form.get('keyswitchBrand'),
                          'keyswitch': request.form.get('keyswitch'),
                          'description': request.form.get('description'),
                          'imgURL': request.form.get('imgURL')})
    return redirect(url_for('projects'))

# Delete project
@app.route('/delete_project/<project_id>')
def delete_project(project_id):
    coll.projects.remove({'_id': ObjectId(project_id)})
    return redirect(url_for('projects'))


@app.route('/about')
def about():
    return render_template('about.html')


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.form['userid']
        password = request.form['password']
        _hash = pbkdf2_sha256.hash("password")
        coll.users.insert_one({
            'username': username,
            'password': _hash
        })
        return render_template('login.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['userid']
        user = coll.users.find_one({'username': username})
        user_password = user['password']
        form_password = request.form['password']
        if pbkdf2_sha256.verify(form_password, user_password):
            session['logged-in'] = True
            session['user-name'] = username
        else:
            return "Login error"
        return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


# flask, pymongo, dnspython and flask-pymongo are installed
