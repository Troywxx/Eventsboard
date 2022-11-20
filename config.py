#!/usr/bin/env python
# coding=utf-8

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    CSRF_ENABLED = True
    SECRET_KEY = '123456' #KeyError: 'A secret key is required to use CSRF.'

alltype = [ u'气象设备', u'气象预报', u'气象观测', u'转报机', '自动化', '跑道关停']
typelist = [(1, alltype[0]), (2, alltype[1]), (3, alltype[2]), (4, alltype[3]), (5, alltype[4]), (6, alltype[5])]
tag = [(1, u'气象'), (2, u'非气象')]