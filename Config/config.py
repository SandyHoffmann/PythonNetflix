from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.engine import Engine
from sqlalchemy import event
app = Flask(__name__)
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'netflix2.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/netflix2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()