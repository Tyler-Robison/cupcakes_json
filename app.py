from flask import Flask, json, request, jsonify, render_template, flash
from flask.wrappers import Response
from werkzeug.utils import redirect

from models import db, connect_db, Cupcake, default_img

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def show_list():
    """Lists cupcakes"""

    return render_template('cupcakes.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """returns JSON for all cupcakes in response to GET"""

    cupcakes = Cupcake.query.all()

    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    """returns JSON for specified cupcake in response to GET"""

    cupcake = Cupcake.query.get_or_404(id)

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes', methods=["POST"])
def add_upcake():
    """Adds a cupcake and returns appropriate JSON"""

    try:
        flavor = request.json['flavor']
        size = request.json['size']
        rating = request.json['rating']
        image = request.json.get('image', default_img)

        cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

        db.session.add(cupcake)
        db.session.commit()
    except:
        db.session.rollback()
        return("Failed Request")

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def edit_cupcake(id):
    """Edits a cupcake and returns appropriate JSON"""

    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Deletes a cupcake and returns appropriate JSON"""

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")
