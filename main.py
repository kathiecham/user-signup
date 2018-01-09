from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

# process and validate form
@app.route('/validate_inputs', methods=['POST'])
def validate_inputs():  
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) <3 or len(username) >20 or ' ' in username:
        username_error = 'Username must be 3-20 characters with no spaces'
        username = ''
    if len(password) <3 or len(password) >20 or ' ' in password:
        password_error = 'Password must be 3-20 characters with no spaces'
        password = ''
    if password != verify_password:
        verify_error = 'Does not match password above'
        verify_password = ''
    if email != "" and (len(email) < 3 or len(email) > 20):
        email_error = 'Not a valid email'
        email = ''
    if email != "" and (email.count("@") !=1 or email.count(".") !=1):
        email_error = 'Not a valid email'
        email = '' 
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)

app.run()
