from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    for user in users:
        month=user.created_at.strftime('%B')
        date=user.created_at.strftime('%d')
        year=user.created_at.strftime('%Y')
        if date[0] == "0":
            date = date[1:]
        user.created_at=month+' '+date+', '+year
    return render_template('index.html', users=users)

@app.route('/new_user_form/')
def new_user_form():
    return render_template('new_user.html')

@app.route('/save_user/',methods=['POST'])
def save_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    id=User.save_user(data)
    return redirect('/show_one_user/'+str(id))

@app.route('/show_one_user/<int:id>/')
def show_one_user(id):
    data = {
        'id':id
    }
    user=User.get(data)
    month=user.created_at.strftime('%B')
    date=user.created_at.strftime('%d')
    year=user.created_at.strftime('%Y')
    if date[0] == "0":
        date = date[1:]
    created_at=month+' '+date+', '+year
    month=user.updated_at.strftime('%B')
    date=user.updated_at.strftime('%d')
    year=user.updated_at.strftime('%Y')
    time=user.updated_at.strftime('%I:%M')
    am_pm=user.updated_at.strftime('%p').lower()
    if time[0] == "0":
        time = time[1:]
    if date[0] == "0":
        date = date[1:]
    updated_at=month+' '+date+', '+year+' at '+time+' '+am_pm
    return render_template('show_one_user.html',user=user,created_at=created_at,updated_at=updated_at)

@app.route('/edit_user_page/<int:id>/')
def edit_user_page(id):
    data = {
        'id':id
    }
    user=User.get(data)
    return render_template('edit_user.html',user=user)

@app.route('/delete_user/<int:id>/')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect('/')

@app.route('/update_user/<int:id>/',methods=['POST'])
def update_user(id):
    data = {
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
    }
    User.update(data)
    return redirect('/show_one_user/'+str(id))

    session.modified = True # By default, it's set to False


