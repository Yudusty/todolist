from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {'name': 'Astolfo', 'finished': True},
    {'name': 'Felix', 'finished': True},
    {'name': 'Hideri', 'finished': True}
]

@app.route('/')
def home():
    # template/home.html
    return render_template("home.html", tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    task = {'name': name, 'finished': True}
    tasks.append(task)
    return render_template("home.html", tasks=tasks)

app.run(debug=True)