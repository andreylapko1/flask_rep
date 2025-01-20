from flask import Flask

app = Flask(__name__)

@app.route('/hello/<user>')
def main(user):
    return f'<br><br><h2>Hello, {user}!</h2>'

@app.route('/sum/<int:a>_<int:b>')
def suma(a, b):
    return f'{a + b}'
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/mult/<int:a>')
def multiply(a):
    return f'{a * 2}'


@app.route('/multdot/<float:a>')
def multiplydot(a):
    return f'{a * 2}'

@app.route('/div/<path:a>')
def to_path(a):
    return f'{a[::-1]}'


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',)