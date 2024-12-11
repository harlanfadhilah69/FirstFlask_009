from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    address = request.form['address']

    return render_template('hasil.html', name=name, age=age, email=email, address=address)

if __name__ == '__main__':
    app.run(debug=True)