from flask import Flask, render_template
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
import datetime 

bootstrap = Bootstrap()
app = Flask(__name__)
app.config.from_object(DevConfig)
app.secret_key = '123456'  #KeyError: 'A secret key is required to use CSRF.'
db = SQLAlchemy(app)
bootstrap.init_app(app)
db.init_app(app)

class Mention(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    workname = db.Column(db.String(255))
    workcontent = db.Column(db.String(255))
    workinfo = db.Column(db.String(255))
    workstatus = db.Column(db.String(255))
    recorddate = db.Column(db.String(255))

    def __init__(self, workname):
        self.workname = workname

    def __repr__(self):
        return "<User '{}'>".format(self.workname)
    
class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])
    info = TextAreaField(u'Comment', validators=[DataRequired()])
    status = TextAreaField(u'Comment', validators=[DataRequired()])



@app.route('/')
def home():
    return render_template(
        'base.html'
    )

@app.route('/work')
def work():
    return render_template(
        'qixiangyewu.html'
    )

@app.route('/relatedwork')
def relatedwork():
    return render_template(
        'guanlianyewu.html'
    )

@app.route('/post/', methods=('GET','POST'))
def post():
    form = CommentForm()
    if form.validate_on_submit():
        new_post = Mention()
        new_post.workname = form.name.data
        new_post.workcontent = form.text.data
        new_post.workinfo = form.info.data
        new_post.workstatus = form.status.data
        new_post.recorddate = datetime.datetime.now()
        db.session.add(new_post)
        db.session.commit()
    
    return render_template(
        'edit_work.html',
        form=form
    )



if __name__ == "__main__":
    app.run()