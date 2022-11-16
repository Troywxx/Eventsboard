#!/usr/bin/env python
# coding=utf-8

import sys
import json

from flask import Flask, render_template, redirect, url_for
from config import DevConfig, typelist, tag, alltype
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import datetime 

reload(sys)
sys.setdefaultencoding('utf-8')

bootstrap = Bootstrap()
app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
bootstrap.init_app(app)
db.init_app(app)

class Mention(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    workname = db.Column(db.String(255))     #事件名：RWY10/28停航施工
    workcontent = db.Column(db.String(255))  #事件内容：每周一三五日 0001-0500
    workinfo = db.Column(db.String(255))     #事件备注：可能引起的问题
    workstatus = db.Column(db.String(255))   #事件状态：主用/正在执行
    worktype = db.Column(db.String(255))     #事件类别：转报机/自动化/跑道关停
    worktag = db.Column(db.String(255))     #事件类型：气象/非气象
    recorddate = db.Column(db.String(255))

    
class CommentForm(FlaskForm):
    name = StringField(
        '事件名称',
        validators=[DataRequired(), Length(max=255)]
    )
    type = SelectField(u'类别', choices=typelist, coerce=int)
    tag = SelectField(u'类型', choices=tag, coerce=int)
    text = TextAreaField(u'内容', validators=[DataRequired()])
    info = TextAreaField(u'备注', validators=[DataRequired()])
    status = TextAreaField(u'状态', validators=[DataRequired()])
    submit = SubmitField(u'提交')



@app.route('/')
def home():
    return render_template(
        'base.html'
    )

@app.route('/work')
def work():
    posts = Mention.query.all()
    postsdic = {}
    types = []

    for i in alltype:
        print(str(i).decode("unicode-escape"))
        types.append(str(i).decode("unicode-escape"))
        print(types)

    for i,j in zip(types, posts) :
        print(j.worktype)
        if i == j.worktype:
            new_dic = {}
            new_dic[i] = j
            postsdic.update(new_dic)
    print( postsdic)
    return render_template(
        'qixiangyewu.html',
        postsdic=postsdic,
        posts=posts
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
        new_post.worktype = form.type.data
        new_post.workcontent = form.text.data
        new_post.workinfo = form.info.data
        new_post.workstatus = form.status.data
        new_post.recorddate = datetime.datetime.now()
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template(
            'u_work.html',
            form=form
        )



if __name__ == "__main__":
    app.run()