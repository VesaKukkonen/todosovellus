# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään task.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True
# Korjaa virheen
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Luetaan kansiosta application/tasks tiedoston models sisältö
from application.tasks import models
from application.tasks import views

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()

