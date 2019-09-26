from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/welcome', methods = ['POST'])
def user_signup():
    username = request.form['username']
    username_error = False

    password = request.form['password']
    password_error = False

    verify_password = request.form['verify-password']
    verify_password_error = False

    email = request.form['email']
    email_error = False

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = True

    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = True

    if verify_password != password:
        verify_password_error = True

    if email:
        if len(password) < 3 or len(password) > 20 or '@' not in email or '.' not in email:
            email_error = True


    if username_error == True or password_error == True or verify_password_error == True or email_error == True:
        return render_template('signup.html', username = username, username_error = username_error, password = password, password_error = password_error, verify_password = verify_password, verify_password_error = verify_password_error, email = email, email_error = email_error)

    return render_template('welcome.html', username = username)

app.run()