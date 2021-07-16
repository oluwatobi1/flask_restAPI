from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask World'


@app.route('/<name>')
def print_name(name):
    return 'hello, {}'.format(name)

if __name__ == "__main__":
    app.run()

