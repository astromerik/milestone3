import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "components"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", projects=mongo.db.caseBrand.find_one())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



#flask, pymongo, dnspython and flask-pymongo are installed
