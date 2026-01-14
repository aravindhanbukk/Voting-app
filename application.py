from flask import Flask, render_template_string, request, redirect, session
import os

application = Flask(__name__)
application.secret_key = os.environ.get('SECRET_KEY', 'voting_secret_key')

# Sample credentials
USERS = {'admin': 'password'}

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Voting System - Login</title>
<style>
body { font-family: Arial; background: #f4f4f4; padding: 50px; }
.container { max-width: 400px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
button { width: 100%; padding: 12px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
</style>
</head>
<body>
<div class="container">
<h2>Login to Vote</h2>
<form method="POST">
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button>
</form>
</div>
</body>
</html>
'''

VOTING_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Voting System</title>
<style>
body { font-family: Arial; background: #f4f4f4; padding: 50px; }
.container { max-width: 500px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
.party { margin: 15px 0; padding: 10px; border: 2px solid #ddd; border-radius: 5px; }
.party input { margin-right: 10px; }
button { width: 100%; padding: 15px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
</style>
</head>
<body>
<div class="container">
<h2>Select Your Party</h2>
<form method="POST" action="/vote">
<div class="party"><input type="radio" name="party" value="Party A" required> Party A</div>
<div class="party"><input type="radio" name="party" value="Party B" required> Party B</div>
<div class="party"><input type="radio" name="party" value="Party C" required> Party C</div>
<button type="submit">Cast Vote</button>
</form>
<a href="/logout">Logout</a>
</div>
</body>
</html>
'''

@application.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            return redirect('/voting')
        else:
            return "Invalid credentials!"
    
    return render_template_string(LOGIN_TEMPLATE)

@application.route('/voting')
def voting():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template_string(VOTING_TEMPLATE)

@application.route('/vote', methods=['POST'])
def vote():
    if not session.get('logged_in'):
        return redirect('/')
    
    party = request.form['party']
    return f"<h2 style='text-align:center; color:green; font-family:Arial;'>Vote is registered for {party}, Thank you!</h2><br><a href='/voting'>Vote Again</a> | <a href='/logout'>Logout</a>"

@application.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')

@application.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    application.run(debug=False, host='0.0.0.0', port=8000)
