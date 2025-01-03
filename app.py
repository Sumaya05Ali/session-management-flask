from flask import Flask, session, redirect, url_for, request, render_template, flash
from datetime import timedelta

app = Flask(__name__)


app.secret_key = 'secret key'


app.permanent_session_lifetime = timedelta(minutes=1)


users = {
    "admin": "123"
    }

@app.route('/')
def home():
    if 'user' in session:
        username = session['user']
        return f'Logged in as {username}. <a href="/logout">Logout</a>'
    return 'You are not logged in! <a href="/login">Login here</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True  
        username = request.form['username']
        password = request.form['password']
        
        
        if username in users and users[username] == password:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

