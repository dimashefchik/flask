from flask import Flask
application = Flask(__name__)
app = application


@application.route('/')
def inxed_1():
    return 'Hello! The first flask page!!'

@application.route('/help')
def inxed_2():
    return '<b>This is  help page!!<b>'

@application.route('/name/<user>')
def inxed_3(user):
    return 'Name ' + user.upper()

@application.route('/kvadrat/<x>')
def inxed_4(x):
    return str(x) + ' v kvadrate = ' + str(int(x)*int(x))
