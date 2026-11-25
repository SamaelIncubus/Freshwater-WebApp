from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard/dashboard_uk.html")

@app.route("/dashboard/location")
def dashboard_location():
    return render_template("dashboard/dashboard_location.html")

@app.route("/dashboard/specie")
def dashboard_specie():
    return render_template("dashboard/dashboard_specie.html")


@app.route("/catalogue/")
def catalogue():
    return render_template("catalogue/catalogue.html")

@app.route("/catalogue/specie")
def catalogue_specie():
    return render_template("catalogue/catalogue_specie.html")


@app.route("/crud")
def crud():
    return render_template("crud/crud.html")

@app.route("/crud/location")
def crud_location():
    return render_template("crud/crud_location.html")

@app.route("/crud/catalogue")
def crud_catalogue():
    return render_template("crud/crud_catalogue.html")

@app.route("/crud/specie")
def crud_specie():
    return render_template("crud/crud_specie.html")

@app.route("/crud/user")
def crud_user():
    return render_template("crud/crud_user.html")