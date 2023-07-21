from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf import FlaskForm  
from wtforms.validators import DataRequired,Email, length

class My_forms(FlaskForm):
    Email = StringField(label='Email', validators=[DataRequired(),Email()])
    Password = PasswordField(label='Password',validators=[length(min=8)])
    submit  = SubmitField(label='Log_in')


app = Flask(__name__)

app.secret_key = "MyNameIsRaj"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = My_forms()
    if login_form.validate_on_submit()== True:
        if login_form.Email.data == "U@gmail.com" and login_form.Password.data == "123456789":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    
    return render_template('login.html', log_in=login_form)

if __name__ == '__main__':
    app.run(debug=True)
