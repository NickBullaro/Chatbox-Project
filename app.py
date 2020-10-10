# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio


MESSAGES_RECEIVED_CHANNEL = 'messages received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['USER']
#database_uri = 'postgresql://{}:{}@localhost/postgres'.format(sql_user, sql_pwd)
database_uri = os.environ['DATABASE_URL']


app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

import models

db.create_all()
db.session.commit()

def emit_all_messages(channel):#--------------------------------------
    # TODO   - content.jsx is looking for key 'allAddresses' we want to emit to allAddresses
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
        'test': 'Connected'
    })
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    
    db.session.add(models.Messages(data["message"]));
    db.session.commit();
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

@app.route('/')
def index():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
