from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/second')
def second():
    return 'Burası ikinci sayfa'

@app.route('/third/subthird')
def third():
    return 'Burası üçüncü sayfanın alt sayfası'

@app.route('/fourth/<string:id>')
def fourth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True)