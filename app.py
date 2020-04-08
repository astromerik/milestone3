import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "components"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", projects=mongo.db.projects.find_one())


@app.route('/projects')
def projects():
    return render_template("projects.html",
                           casematerial=mongo.db.caseMaterial.find(),
                           size=mongo.db.layoutSize.find(),
                           layout=mongo.db.layout.find(),
                           projects=mongo.db.projects.find())


@app.route('/build')
def build():
    return render_template("build.html",
                           casematerial=mongo.db.caseMaterial.find(),
                           size=mongo.db.layoutSize.find(),
                           layout=mongo.db.layout.find(),
                           projects=mongo.db.projects.find(),
                           casebrand=mongo.db.caseBrand.find(),
                           switchbrand=mongo.db.keyswitchBrand.find(),
                           switchtype=mongo.db.cherry.find())


@app.route('/insert_build', methods=['POST'])
def insert_build():
    mongo.db.projects.insert_one(request.form.to_dict())
    return redirect(url_for('build'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



#flask, pymongo, dnspython and flask-pymongo are installed
