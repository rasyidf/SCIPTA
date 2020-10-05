# -*- encoding: utf-8 -*-

from app.admin import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/manage/inputs')
@login_required
def inputs():

    return render_template('inputs.html', segment='index')

@blueprint.route('/manage/outputs')
@login_required
def outputs(): 
    return render_template('outputs.html', segment='index')
  
@blueprint.route('/manage/data')
@login_required
def data():
    return render_template('data.html', segment='index')

@blueprint.route('/manage')
@login_required
def manage(): 
    return render_template('manage.html', segment='index')


@blueprint.route('/engine/trainer')
@login_required
def trainer(): 
    return render_template('trainer.html', segment='index')
  
  
@blueprint.route('/engine/logger')
@login_required
def logger(): 
    return render_template('logger.html', segment='index')
  
  
@blueprint.route('/engine/report')
@login_required
def reporter(): 
    return render_template('reporter.html', segment='index')
  