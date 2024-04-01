from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return 'Welcome to the Flask App!'

# Route to display a form
@app.route('/form', methods=['GET'])
def show_form():
    return render_template('form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you could process the form data further (e.g., store it in a database, send an email, etc.)
        
        return f"Form submitted successfully! Name: {name}, Email: {email}, Message: {message}"
    else:
        return redirect(url_for('show_form'))

if __name__ == '__main__':
    app.run(debug=True)
