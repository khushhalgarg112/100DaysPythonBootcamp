from flask import Flask,request,render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    data = request.form['username']
    password = request.form['password']
    return render_template('login.html', user=data, passw=password)

if __name__ == "__main__":
    app.run(debug=True)