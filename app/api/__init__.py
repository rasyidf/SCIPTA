# -*- encoding: utf-8 -*-


from flask import Blueprint

blueprint = Blueprint(
    'api_blueprint',
    __name__,
    url_prefix='/api',
    template_folder='templates',
    static_folder='static'
)
