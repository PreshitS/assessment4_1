from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock user database
users = {
    "user1": "password1",
    "user2": "password2"
}

# Homepage route
@app.route('/')
def home():
    return 'Welcome to the Flask Login App!'

# Route to display login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            return redirect(url_for('welcome', username=username))
        else:
            return render_template('login.html', message='Invalid username or password.')
    else:
        return render_template('login.html')

# Route to display welcome page after successful login
@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
