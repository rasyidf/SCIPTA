# -*- encoding: utf-8 -*-

from app.api import blueprint
from flask import current_app as apps
from flask import render_template, redirect, url_for, request, make_response, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound


from .models import Data, DataEncoder

error = {
    "itemNotFound": {
        "errorCode": "itemNotFound",
        "errorMessage": "Item not found"
    },
    "itemAlreadyExists": {
        "errorCode": "itemAlreadyExists",
        "errorMessage": "Could not create item. Item already exists"
    }
}


class DataApi(MethodView):
    """
    /api/data
    """

    def get(self):
        """ Return the entire inventory collection """
        inventory = Data.query.all()
        apps.json_encoder = DataEncoder
        return make_response(jsonify(inventory), 200)

    def post(self):
        """ Create an item """

        apps.json_encoder = DataEncoder
        body = request.get_json()

        test = Data.query.filter(
            Data.text == body.get('text', 'Untitled')).first()

        if test is None:
            data = Data(text=body.get('text', 'Untitled'), description=body.get(
                'description', ''), data=body.get('data', ''))
            db.session.add(data)
        else:
            make_response(jsonify(error["itemAlreadyExists"]), 400)

        db.session.commit()
        return make_response(jsonify(data))

    def delete(self):
        """ Delete the entire inventory collection """
        Data.query.clear()
        return make_response(jsonify({}), 200)


class DataItemApi(MethodView):
    """ /api/inventory/<item_name> """

    def get(self, item_name):
        """ Get an item """

        apps.json_encoder = DataEncoder
        data = Data.query.filter(Data.id == int(item_name)).first()
        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 400)

        return make_response(jsonify(data), 200)

    def put(self, item_name):
        """ Update/replace an item """
        body = request.get_json()

        q = Data.query.filter(Data.id == int(item_name)).first()

        q.text = body.get("text", '')
        q.desc = body.get("desc", '')
        q.data = body.get("data", '')

        db.session.commit()

        return make_response(jsonify(q))

    def delete(self, item_name):
        """ Delete an item """

        data = Data.query.filter(Data.id == int(item_name)).first()
        
        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 400)
        
        db.session.delete(data)
        db.session.commit()
        
        return make_response(jsonify({}), 200)


blueprint.add_url_rule("/data", view_func=DataApi.as_view("data_api"))
blueprint.add_url_rule("/data/<item_name>",
                       view_func=DataItemApi.as_view("data_item_api"))
