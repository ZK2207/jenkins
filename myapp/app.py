from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

# Danh sách môn học
subjects = [
    {'id': 1, 'name': 'Toán học'},
    {'id': 2, 'name': 'Vật lý'},
    {'id': 3, 'name': 'Hóa học'},
    {'id': 4, 'name': 'Ngôn ngữ'},
]

@app.route('/')
def index():
    return render_template('index.html', subjects=subjects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
