from flask import Flask, render_template

app = Flask(__name__)

CLUBS = [{
    'id': 1,
    'name': 'Avyaan',
    'arts': 'Music',
    'type': 'Cultural'
}, {
    'id': 2,
    'name': 'Enigma',
    'arts': 'Dance',
    'type': 'Cultural'
}, {
    'id': 3,
    'name': 'Khalas',
    'arts': 'Dance',
    'type': 'Cultural'
}, {
    'id': 4,
    'name': 'Atrangi',
    'arts': 'Art and Poetry',
    'type': 'Cultural'
}, {
    'id': 5,
    'name': 'Adaa',
    'arts': 'Fashion',
    'type': 'Cultural'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', clubs=CLUBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
