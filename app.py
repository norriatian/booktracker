from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

# class Book(db.Model):
#     # be able to be sorted by author & genre 
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     author_name = db.String()
#     begin_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)
#     publication_year = db.Column(db.Integer)
#     # enum
#     genre = 
#     series = 
#     # description grabbed from wiki summary
#     description = db.Column(db.String)

# class Author(db.Model):
#     # sort by: name
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     # description grabbed from wiki summary
#     description = db.Column(db.String)
#     # link to the book table
#     books = 

# class Genre(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     # description grabbed from wiki summary
#     description = db.Column(db.String)
    
# class BookList(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String)
#     note = db.Column(db.String)
#     books = 
# # also have reading lists 

if __name__ == '__main__':
    app.run(debug=True)


