# -*- encoding: utf-8 -*-

from app.api import blueprint
from flask import current_app as apps
from flask import render_template, redirect, url_for, request, make_response, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from app import login_manager, db
from jinja2 import TemplateNotFound


from .models import Data, DataEncoder

inventory = {
    "1": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "2": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "3": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "4": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "5": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "6": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "7": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "8": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "9": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "10": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "11": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "12": {
        "desc": "Red and juicy",
        "qty": 500
    },
    "13": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "14": {
        "desc": "Red and juicy",
        "qty": 500
    }, "15": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "16": {
        "desc": "Red and juicy",
        "qty": 500
    }, "17": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "18": {
        "desc": "Red and juicy",
        "qty": 500
    }, "19": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "20": {
        "desc": "Red and juicy",
        "qty": 500
    }, "21": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "22": {
        "desc": "Red and juicy",
        "qty": 500
    }, "23": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "24": {
        "desc": "Red and juicy",
        "qty": 500
    }, "25": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "26": {
        "desc": "Red and juicy",
        "qty": 500
    }, "27": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "28": {
        "desc": "Red and juicy",
        "qty": 500
    }, "29": {
        "desc": "Crunchy and delicious",
        "qty": 30
    },
    "30": {
        "desc": "Red and juicy",
        "qty": 500
    }
}


class DataApi(MethodView):
    """
    /api/inventory
    """

    def get(self):
        """ Return the entire inventory collection """
        inventory = Data.query.all()
        apps.json_encoder = DataEncoder 
        return make_response(jsonify(inventory), 200)

    def delete(self):
        """ Delete the entire inventory collection """
        Data.query.clear()
        return make_response(jsonify({}), 200)


class DataItemApi(MethodView):
    """ /api/inventory/<item_name> """

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

    def get(self, item_name):
        """ Get an item """
        
        apps.json_encoder = DataEncoder 
        data = Data.query.filter(Data.id == int(item_name)).first()
        if data is None:
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        
        return make_response(jsonify(data), 200)

    def post(self, item_name):
        """ Create an item """
        if data.get(item_name, None):
            return make_response(jsonify(self.error["itemAlreadyExists"]), 400)
        body = request.get_json()
        
        data = Data.query.filter(Data.id == int(item_name)).first()
        if data is None:
            Data.query.create()
        data[item_name] = {"description": body.get( "description", None), "qty": body.get("qty", None)}
        
        return make_response(jsonify(data[item_name]))

    def put(self, item_name):
        """ Update/replace an item """
        body = request.get_json()
        inventory[item_name] = {"description": body.get(
            "description", None), "qty": body.get("qty", None)}
        
        return make_response(jsonify(inventory[item_name]))

    def patch(self, item_name):
        """ Update/modify an item """
        if not inventory.get(item_name, None):
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        body = request.get_json()
        inventory[item_name].update({"description": body.get(
            "description", None), "qty": body.get("qty", None)})
        
        return make_response(jsonify(inventory[item_name]), 2)

    def delete(self, item_name):
        """ Delete an item """
        
        inventory = Data.query.filter(Data.id == int(item_name)).first()
        if inventory is None:
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        db.session.delete(inventory)
        db.session.commit()
        return make_response(jsonify({}), 200)


blueprint.add_url_rule("/data", view_func=DataApi.as_view("data_api"))
blueprint.add_url_rule("/data/<item_name>",
                       view_func=DataItemApi.as_view("data_item_api"))
