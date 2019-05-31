from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return str(fahrenheit)


if __name__ == '__main__':
    app.run()
