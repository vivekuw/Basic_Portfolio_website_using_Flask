from flask import Flask, render_template,request,jsonify
import json

with open('data.json', 'r') as file:
    data = json.load(file)
new_d = data
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfoilo')
def portfoilo():
    return render_template('portfoilo.html',project=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/fill-form' ,methods=['POST'])
def form():
    no = request.form['number']
    title = request.form['name']
    body = request.form['body']
    github = request.form['github']
    ndata = {
        'id':no,
        'title': title,
        'body': body,
        'github': github
    }
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):

        data = []
    data.append(ndata)

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    return render_template('index.html')


@app.route('/delete-no', methods=['POST'])
def delete_entry():
    entry_id = request.form['number']
    with open('data.json', 'r') as file:
        data = json.load(file)
    updated_data = [entry for entry in data if entry.get('id') != entry_id]
    if len(data) == len(updated_data):
        return jsonify({'error': 'Entry not found'}), 404

    with open('data.json', 'w') as file:
        json.dump(updated_data, file, indent=4)
    return render_template('index.html')

@app.route('/skill')
def skill():
    return render_template('skill.html')
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
