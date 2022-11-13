from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

class ZBJdevice(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    devicename = db.Column(db.String(255))
    info = db.Column(db.String(255))

    def __init__(self, devicename):
        self.devicename = devicename

    def __repr__(self):
        return "<User '{}'>".format(self.devicename)
    
if __name__ == "__main__":
    manager.run()