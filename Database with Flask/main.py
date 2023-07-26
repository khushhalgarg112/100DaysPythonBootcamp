from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///book-databse.db'
db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.String(5), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
        # books = Data.query.all()  This fucntion is used by us but it is from the older version   
    books = db.session.query(Data).all()
    return render_template('index.html',books=books)
   


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        obj1 = Data(book=request.form['Book_name'],author=request.form['Book_author'],rating=request.form['Book_rating'])
        db.session.add(obj1)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
    if request.method=='POST':
        new_Data = db.session.query(Data).get(id)
        new_Data.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    book = db.session.query(Data).get(id)
    return render_template('edit.html', book= book)

@app.route('/delete/<int:id>')
def delete(id):
    book = db.session.query(Data).get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False)


'''SQLite DataBase Code'''
# db = sqlite3.connect("data-base.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


'''SQlAlchemy Database Codes'''

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///alchemy_databse.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), unique=True, nullable=False)
#     author = db.Column(db.String(120), nullable=False)
#     rating = db.Column(db.String(5), nullable=False)

#     def __repr__(self):
#         return f'<Book {self.title}>'

# with app.app_context():
    # db.create_all()

'''Create Data'''
    # obj1 = User(id=2,title="Potter",author="J.K Rowling", rating="9.2")
    # db.session.add(obj1)
    # db.session.commit()

'''Read all data '''
    # book  = User.query.all()
    # for i in book:
    #     print(i.title)

'''Read a specific data '''
    # book = User.query.filter_by(title="Harry Potter").first()
    # print(book.author)

'''Update throw a specific data'''
    # book = User.query.filter_by(title="Harry Potter").first()
    # book.title = "Harry Potter and the chamber  of Secrets"
    # db.session.commit()

'''Update throw Id'''
    # book_id = 2
    # book = User.query.get(book_id)
    # book.title = "Think and Grow Rich"
    # book.author = "Napollian Hill"
    # db.session.commit()

'''Delete Data '''
    # book_id = 1
    # book = User.query.get(book_id)
    # db.session.delete(book)
    # db.session.commit()
