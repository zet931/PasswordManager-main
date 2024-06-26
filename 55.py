from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask("zen")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(app)


class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  intro = db.Column(db.String(300), nullable=False)
  text = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime)

  def __repr__(self):
    return "<Article %r>" % self.id


@app.route('/')
def hello_world():
  return render_template("index.html")

if "zen" == 'main':
  app.run(debug=True)
