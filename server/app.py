#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    return make_response(bakeries, 200)


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    found_bakery = Bakery.query.filter_by(id = id).first()
    bakery_serialize = found_bakery.to_dict()
    return make_response(bakery_serialize, 200)


@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    baked_goods_serialized = [
        bg.to_dict() for bg in baked_goods
    ]
    return make_response(baked_goods_serialized, 200)


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
