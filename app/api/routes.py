# -*- encoding: utf-8 -*-

from app.api import blueprint
from flask import current_app as apps
from flask import render_template, redirect, url_for, request, make_response, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound


from .models import Data, Input, Output, DataEncoder, InputEncoder, OutputEncoder

error = {
    "itemNotFound": {
        "id": -1,
        "errorCode": "itemNotFound",
        "errorMessage": "Item not found"
    },
    "itemAlreadyExists": {
        "id": -1,
        "errorCode": "itemAlreadyExists",
        "errorMessage": "Could not create item. Item already exists"
    }
}

# region Output


class OutputApi(MethodView):
    """
    /api/output
    """

    def get(self):
        """ Return the entire inventory collection """
        inventory = Output.query.all()
        apps.json_encoder = OutputEncoder
        return make_response(jsonify(inventory), 200)

    def post(self):
        """ Create an item """
        body = request.get_json()  
        apps.json_encoder = OutputEncoder
        test = Output.query.filter(
            Output.text == body.get('text', 'Untitled')).first()

        if test is None:
            data = Output(text=body.get('text', 'Untitled'), 
                          desc=body.get('desc', ''), data=body.get('data', ''))
            db.session.add(data)
        else:
            make_response(jsonify(error["itemAlreadyExists"]), 200)

        db.session.commit()
        return make_response(jsonify(data))

    def delete(self):
        """ Delete the entire inventory collection """
        Output.query.clear()
        return make_response(jsonify({}), 200)


class OutputItemApi(MethodView):
    """ /api/inventory/<item_name> """

    def get(self, ids: int):
        """ Get an item """

        apps.json_encoder = OutputEncoder
        data = Output.query.filter(Output.id == ids).first()
        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        return make_response(jsonify(data), 200)

    def put(self, ids: int):
        """ Update/replace an item """
        body = request.get_json()

        q = Output.query.filter(Output.id == ids).first()

        q.text = body.get("text", '')
        q.desc = body.get("desc", '')
        q.data = body.get("data", '')

        db.session.commit()

        return make_response(jsonify(q))

    def delete(self, ids):
        """ Delete an item """

        data = Output.query.filter(Output.id == ids).first()

        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        db.session.delete(data)
        db.session.commit()

        return make_response(jsonify({}), 200)

# region Input


class InputApi(MethodView):
    """
    /api/input
    """

    def get(self):
        """ Return the entire inventory collection """
        inventory = Input.query.all()
        apps.json_encoder = InputEncoder
        return make_response(jsonify(inventory), 200)

    def post(self):
        """ Create an item """
        body = request.get_json() 

        apps.json_encoder = InputEncoder
        test = Input.query.filter(
            Input.text == body.get('text', 'Untitled')).first()

        if test is None:
            data = Input(text=body.get('text', 'Untitled'), desc=body.get(
                'desc', ''), data=body.get('data', ''))
            db.session.add(data)
        else:
            make_response(jsonify(error["itemAlreadyExists"]), 200)

        db.session.commit()
        return make_response(jsonify(data))

    def delete(self):
        """ Delete the entire inventory collection """
        Input.query.clear()
        return make_response(jsonify({}), 200)


class InputItemApi(MethodView):
    """ /api/inputs/<item_name> """

    def get(self, ids: int):
        """ Get an item """

        apps.json_encoder = InputEncoder
        data = Input.query.filter(Input.id == ids).first()
        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        return make_response(jsonify(data), 200)

    def put(self, ids: int):
        """ Update/replace an item """
        body = request.get_json()

        q = Input.query.filter(Input.id == ids).first()

        q.text = body.get("text", '')
        q.desc = body.get("desc", '')
        q.data = body.get("data", '')

        db.session.commit()

        return make_response(jsonify(q))

    def delete(self, ids):
        """ Delete an item """

        data = Input.query.filter(Input.id == ids).first()

        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        db.session.delete(data)
        db.session.commit()

        return make_response(jsonify({}), 200)

# region Data


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
        body = request.get_json()

        apps.json_encoder = DataEncoder
        test = Data.query.filter(
            Data.text == body.get('text', 'Untitled')).first()

        if test is None:
            data = Data(text=body.get('text', 'Untitled'), desc=body.get(
                'desc', ''), data=body.get('data', ''))
            db.session.add(data)
        else:
            make_response(jsonify(error["itemAlreadyExists"]), 200)

        db.session.commit()
        return make_response(jsonify(data))

    def delete(self):
        """ Delete the entire inventory collection """
        Data.query.clear()
        return make_response(jsonify({}), 200)


class DataItemApi(MethodView):
    """ /api/data/<item_name> """

    def get(self, ids: int):
        """ Get an item """

        apps.json_encoder = DataEncoder
        data = Data.query.filter(Data.id == ids).first()
        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        return make_response(jsonify(data), 200)

    def put(self, ids: int):
        """ Update/replace an item """
        body = request.get_json()

        q = Data.query.filter(Data.id == ids).first()

        q.text = body.get("text", '')
        q.desc = body.get("desc", '')
        q.data = body.get("data", '')

        db.session.commit()

        return make_response(jsonify(q))

    def delete(self, ids):
        """ Delete an item """

        data = Data.query.filter(Data.id == ids).first()

        if data is None:
            return make_response(jsonify(error["itemNotFound"]), 200)

        db.session.delete(data)
        db.session.commit()

        return make_response(jsonify({}), 200)


blueprint.add_url_rule("/inputs", view_func=InputApi.as_view("input_api"))
blueprint.add_url_rule(
    "/inputs/<ids>", view_func=InputItemApi.as_view("input_item_api"))

blueprint.add_url_rule("/outputs", view_func=OutputApi.as_view("output_api"))
blueprint.add_url_rule(
    "/outputs/<ids>", view_func=OutputItemApi.as_view("output_item_api"))

blueprint.add_url_rule("/data", view_func=DataApi.as_view("data_api"))
blueprint.add_url_rule(
    "/data/<ids>", view_func=DataItemApi.as_view("data_item_api"))
