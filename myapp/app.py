from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

subjects = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'Ruby'},
    {'id': 3, 'name': 'Java'},
    {'id': 4, 'name': 'PHP'},
]

@app.route('/')
def index():
    return render_template('index.html', subjects=subjects)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
