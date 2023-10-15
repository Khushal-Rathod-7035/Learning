from flask import Flask

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello Hi %s!' % name


if __name__ == '__main__':
    app.run()
