import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import env
from bson.objectid import ObjectId


# Start application
app = Flask(__name__)
app.config["MONGO_DBNAME"] = "components"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

coll = mongo.db


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", projects=coll.projects.find_one())


# Display and filter projects

@app.route('/projects', methods=['POST', 'GET'])
def projects():
    casemat = request.form.get('casemat')
    print(casemat)
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
        print(query)
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
    return redirect(url_for('build'))


# @app.route('/view_project')
# def view_project():
#     render_template('viewproject.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# flask, pymongo, dnspython and flask-pymongo are installed
