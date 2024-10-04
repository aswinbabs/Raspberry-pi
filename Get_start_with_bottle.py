#install bottle if not installed

from bottle import route, run, template

'''decorator is used to bind a function to url,here home function
bound to url(/)'''

@route('/')
def home():
    return template('<b>Hello {{name}}</b>!', name = 'world')

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name = 'name')
if __name__ == '__main__':
    run(host = 'localhost', port = 8080)