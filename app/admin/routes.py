# -*- encoding: utf-8 -*-

from app.admin import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

#region  inputs

@blueprint.route('/manage/inputs')
@login_required
def inputs():
    return render_template('input/index.html', segment='index')

@blueprint.route('/manage/inputs/create')
@login_required
def inputs_create():
    return render_template('input/create.html', segment='index')

@blueprint.route('/manage/inputs/edit/<id>')
@login_required
def inputs_edit(id):
    return render_template('input/edit.html', segment='index', ids = id)

#region Outputs

@blueprint.route('/manage/outputs')
@login_required
def outputs(): 
    return render_template('output/index.html', segment='index')

@blueprint.route('/manage/outputs/create')
@login_required
def outputs_create(): 
    return render_template('output/create.html', segment='index')

@blueprint.route('/manage/outputs/edit/<id>')
@login_required
def outputs_edit(id):
    return render_template('output/edit.html', segment='index', ids = id)
  
#region  Data

@blueprint.route('/manage/data')
@login_required
def data():
    return render_template('data/index.html', segment='index')

@blueprint.route('/manage/data/create')
@login_required
def data_create():
    return render_template('data/create.html', segment='index')

@blueprint.route('/manage/data/edit/<id>')
@login_required
def data_edit(id):
    return render_template('data/edit.html', segment='index', ids = id)

#region manage

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
  