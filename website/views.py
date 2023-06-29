from flask import Blueprint, render_template, request, flash, jsonify
from .models import User, Tasks
from . import db
from flask_login import login_required, current_user
import json
import datetime
from datetime import date


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/task_page', methods=['GET', 'POST'])
@login_required
def task_page():

    user = User.query.get(current_user.id)
    #sorted_user_tasks = user.tasks.order_by(Tasks.due_date, Tasks.completed).all()
    sorted_user_tasks = sorted(user.tasks, key=lambda task: (not task.completed, task.due_date))
    if request.method == 'POST':

        task = request.form.get('task')
        title = request.form.get('title')
        date = request.form.get('date')
        todays_date = datetime.datetime.now()

        if len(task) < 1:
            flash('You must enter a task!', category='error')
        elif (int(date[:4]) < todays_date.year) or (int(date[5:7]) < todays_date.month and int(date[:4]) < todays_date.year) or (int(date[8:]) < todays_date.day and int(date[:4]) < todays_date.year) or (int(date[8:]) < todays_date.day and int(date[5:7]) == todays_date.month and int(date[:4]) == todays_date.year) or (int(date[5:7]) < todays_date.month and int(date[:4]) == todays_date.year):
            flash('Enter a valid date during or after today!', category='error')
        else:
            new_task = Tasks(data=task, data_title=title, due_date=date, user_id=current_user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added!', category='success')

        sorted_user_tasks = sorted(user.tasks, key=lambda task: (not task.completed, task.due_date))
    
    return render_template('task_page.html', user=current_user, sorted_tasks=sorted_user_tasks)

@views.route('/delete-task', methods=['POST'])
def delete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Tasks.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return jsonify({})

@views.route('/complete-task', methods=['POST'])
def complete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Tasks.query.get(taskId)
    if task:
       if task.user_id == current_user.id:
           task.completed = True 
           db.session.commit()

    return jsonify({})

@views.route('/uncomplete-task', methods=['POST'])
def uncomplete_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Tasks.query.get(taskId)
    if task:
       if task.user_id == current_user.id:
           task.completed = False 
           db.session.commit()
    return jsonify({})




