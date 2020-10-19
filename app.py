# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
from flask import request
import flask_sqlalchemy
import flask_socketio
import models
import bot


MESSAGES_RECEIVED_CHANNEL = 'messages received'
USERS_RECEIVED_CHANNEL = 'users received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)


database_uri = os.environ['DATABASE_URL']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri


db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app


db.create_all()
db.session.commit()


def parseM(data):
    words = data['message'].split()
    print("_", words)
    if(words[0] == "!!"):
        out = bot.switch(words)
        return out

    


connected = {}



def emit_all_users(channel):
    all_users = []
    for k in connected:
        all_users.append(connected[k])
    #     db_user.user for db_user in \
    #     db.session.query(models.user_info).all()]
    print("-", all_users)
    socketio.emit(channel, {
        'all_users': all_users
    })


def emit_all_messages(channel):
    all_messages = [ 
        db_message.message for db_message in \
        db.session.query(models.Messages).all()]
    
    socketio.emit(channel, {
        'allMessages': all_messages
    })


@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'connected'
    })
    print("..", connected)
    
    emit_all_users(USERS_RECEIVED_CHANNEL)
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')
    del (connected[request.sid])
    print("...", connected)
    emit_all_users(USERS_RECEIVED_CHANNEL)
    
@socketio.on('new google user')
def on_login(data):
    print('New login from user:', data['user'])
    connected[request.sid] = data['user']
    
    try:
        db.session.add(models.user_info(data['email'], data['user'], data['pic']));
        db.session.commit();
    except Exception as error:
        db.session.rollback();
        print("User already in db")
    
    emit_all_users(USERS_RECEIVED_CHANNEL)
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    output = parseM(data)
    print(output)
    try:
        db.session.add(models.Messages(connected[request.sid] + ": " + data["message"], db.session.query(models.user_info.id).filter(models.user_info.user==connected[request.sid]).first().id));
        db.session.commit();
        if output:
            db.session.add(models.Messages('Awesome Bot: ' + output, db.session.query(models.user_info.id).filter(models.user_info.user=='Awesome Bot').first().id));
            db.session.commit();
    except Exception as error:
        db.session.rollback();
        db.session.add(models.Messages("ERROR: User " + connected[request.sid] + "'s message has failed to send! Please try again!", db.session.query(models.user_info.id).filter(models.user_info.user==connected[request.sid]).first().id));
        db.session.commit();
    
    emit_all_users(USERS_RECEIVED_CHANNEL)
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@app.route('/')
def index():
    try:
        db.session.add(models.user_info('awesomebot@gmail.com', 'Awesome Bot', 'https://www.internetandtechnologylaw.com/files/2019/06/iStock-872962368-chat-bots-265x300.jpg'));
        db.session.commit();
    except Exception as error:
        db.session.rollback();
        print("User already in db")
    emit_all_users(USERS_RECEIVED_CHANNEL)
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")


if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )