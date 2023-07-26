from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests


MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
API_KEY = "57733101f3feb3c3c084c165c2c9a31d"
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NzczMzEwMWYzZmViM2MzYzA4NGMxNjVjMmM5YTMxZCIsInN1YiI6IjY0YzBjNDY1ZWRlMWIwMDBjOGJjYjVjMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fEPySGZLpKfpkJfy_hlg-oHDasbqFySBESpJcrGOShk"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
SELECTED_MOVIE = "https://api.themoviedb.org/3/movie"

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-database.db"
Bootstrap5(app)
db = SQLAlchemy(app)


class Add_form(FlaskForm):
    title_name = StringField(label="Movie Name", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class Edit_Form(FlaskForm):
    rating = FloatField(label="Update Rating (Out of 10)", validators=[DataRequired()])
    review = StringField(label="Update Review", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(100))
    description = db.Column(db.String(1000), nullable=False)
    img_url = db.Column(db.String(500), unique=True, nullable=False)


with app.app_context():
    db.create_all()

    # add_movie = Movie(
    #     title="Avatar: The Way of Water",
    #     year=2022,
    #     rating=8.1,
    #     ranking=1,
    #     review="Best Graphics and Visuals",
    #     description="Jake Sully lives with his newfound family formed on the extrasolar moon Pandora. Once a familiar threat returns to finish what was previously started, Jake must work with Neytiri and the army of the Na'vi race to protect their home.",
    #     img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQsu7fAOboJJfzRhYZq2fyPdWGk_HvuPtSIA&usqp=CAU",
    # )
    # db.session.add(add_movie)
    # db.session.commit()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = movies.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    form = Edit_Form()
    movie_data = db.session.query(Movie).get(id)
    if form.validate_on_submit():
        movie = db.session.query(Movie).get(id)
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_data)


@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.query(Movie).get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = Add_form()
    if form.validate_on_submit():
        movie_name = form.title_name.data
        movie_data = requests.get(
            MOVIE_URL, params={"api_key": API_KEY, "query": movie_name}
        )
        data = movie_data.json()["results"]
        return render_template("select.html", data=data)

    return render_template("add.html", form=form)


@app.route("/select")
def select():
    movie_id = request.args.get("id")
    movie_url = f"{SELECTED_MOVIE}/{movie_id}"
    movie_details = requests.get(
        movie_url, params={"api_key": API_KEY, "language": "en-US"}
    )
    data = movie_details.json()
    new_movie = Movie(
        title=data["original_title"],
        description=data["overview"],
        img_url=f"{IMAGE_URL}{data['poster_path']}",
        year=data["release_date"].split("-")[0],
    )
    db.session.add(new_movie)
    db.session.commit()
    user = Movie.query.filter_by(title=data["original_title"])

    return redirect(url_for("edit", id=new_movie.id))


if __name__ == "__main__":
    app.run(debug=False)
