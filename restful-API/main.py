from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictinoary = {}

        for column in self.__table__.columns:
            dictinoary[column.name] = getattr(self, column.name)

        return dictinoary

with app.app_context():
    db.create_all()

@app.route('/doc')
def doc():
    return render_template('index.html')

@app.route("/", methods=["GET"])
def home():
    random_cafe = db.session.query(Cafe).get(random.randint(1,Cafe.query.count()))
    return jsonify(
        # cafe={
        #     # "id": random_cafe.id,
        #     "name": random_cafe.name,
        #     "map_url": random_cafe.map_url,
        #     "img_url": random_cafe.img_url,
        #     "location": random_cafe.location,
        #     "amenities": {
        #   "seats": random_cafe.seats,
        #   "has_toilet": random_cafe.has_toilet,
        #   "has_wifi": random_cafe.has_wifi,
        #   "has_sockets": random_cafe.has_sockets,
        #   "can_take_calls": random_cafe.can_take_calls,
        #   "coffee_price": random_cafe.coffee_price,
        # }
        # }

        cafe = random_cafe.to_dict()
    )

def str_to_bool(v):
    if v in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False

@app.route('/all', methods=['GET'])
def get_All():
    cafe = db.session.query(Cafe).all()
    all_cafe = []
    for i in cafe:
        all_cafe.append(i.to_dict())
    
    return jsonify(all_cafe)

## HTTP GET - Read Record
@app.route('/search/<string:location>', methods=['GET'])
def get(location):
    data = Cafe.query.filter_by(location=location).first()
    if data is None:
        return jsonify(cafe={
            "error": "Data Not found"
        })
    return jsonify(data.to_dict())

## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add_element():
        cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=str_to_bool(request.form.get("sockets")),
        has_toilet=str_to_bool(request.form.get("toilet")),
        has_wifi=str_to_bool(request.form.get("wifi")),
        can_take_calls=str_to_bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
        )

        db.session.add(cafe)
        db.session.commit()
        return jsonify({
            "response": "Successfullt added to database"
        })


## HTTP PUT/PATCH - Update Record
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    cafe = db.session.query(Cafe).get(id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify({
            "Sucess": "Your Data is updated successfully"
        }),200
    return jsonify({
        "error": "Id is not found into the database"
    }),404

## HTTP DELETE - Delete Record
@app.route('/close/<int:id>', methods=['DELETE'])
def delete(id):
    api_key = request.args.get("api")
    if api_key == "Secret":
        cafe = db.session.query(Cafe).get(id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"Deleted": "Your cafe is deletd suceessfully"}),200
        return jsonify({ "error": "Cafe is not found with this id."}),404
    return jsonify({"error": "Api Key is wrong."}),404

if __name__ == "__main__":
    app.run(debug=False)
