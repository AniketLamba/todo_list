from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['description']
    tasks.append(description)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect(url_for('index'))

# @app.route('/update/<int:index>', methods=['GET', 'POST'])
# def update_task(index):
#     if request.method == 'POST':
#         new_description = request.form['description']
#         tasks[index] = new_description
#         return redirect(url_for('index'))
#     else:
#         return render_template('update.html', task=tasks[index])

if __name__ == '__main__':
    app.run(debug=True, port=1000)
