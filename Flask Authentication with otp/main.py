from flask import Flask, render_template, request, session, url_for, redirect, flash, send_from_directory, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import smtplib
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


login = LoginManager()
login.init_app(app)

MY_MAIL = "khusgarg1@gmail.com"
MY_PASS = "vphnppivvlsntbgt"

# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user  = db.session.query(User).filter_by(email = request.form.get('email')).first()
        if user:
           flash('Email already exist, try to login')
           return redirect(url_for('login')) 
        
        session['number'] = random.randrange(1111, 9999)
        session['name'] = request.form.get('name')
        session['password']=generate_password_hash(request.form.get('password'), method='pbkdf2:sha1', salt_length=8)
        session['email'] =  request.form.get('email')
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MY_PASS)
            connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=session['email'],
            msg=f"Subject: Cheet Sheet\n\n Your Otp is : { session['number'] }",
        )
        return redirect(url_for('otp'))
    return render_template("register.html")


@app.route('/otp', methods=['POST','GET'])
def otp():
    email = session.get('email', None)
    password = session.get('password', None)
    name = session.get('name', None)
    otp1 = session.get('number', None)
    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        print(otp1)
        print(email)
        print(entered_otp)
        if int(entered_otp) == otp1:
            obj = User(email=email,password=password,name=name)
            db.session.add(obj)
            db.session.commit()
            login_user(obj)
            return redirect(url_for('secrets', name = name))
        else:
            flash(f"You entered wrong otp")
            return redirect(url_for('register'))
        
    return render_template('otp.html')

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user  = db.session.query(User).filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                 flash('Invalid Password , Please try again')
                 return redirect(url_for('login'))
        else:
            flash('Email does not exist.')
            return redirect(url_for('login'))
    
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    username = request.args.get('name')
    return render_template("secrets.html", name=username, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # return send_from_directory(directory='static/files', path='cheat_sheet.pdf', as_attachment=True)
    return send_file("static/files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=False)
