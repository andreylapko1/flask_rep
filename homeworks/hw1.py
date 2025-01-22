from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'


@app.route('/hello/<name>')
def hello_by_name(name):
    return f'Hello, {name}!'

if  __name__ == '__main__':
    app.run(debag=True)