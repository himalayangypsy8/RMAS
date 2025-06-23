from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # use a long random one for production

# Home Page: Show login form
@app.route('/')
def home():
    return render_template('login.html')

# Handle Login Submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # ✅ For now, accept any username/password
    session['username'] = username

    # Randomly pick one auth method
    method = random.choice(['sms', 'email', 'biometric'])
    session['auth_method'] = method

    if method in ['sms', 'email']:
        return redirect('/otp')
    else:
        return redirect('/biometric')

# OTP Input Page
@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        # ✅ Accept '123456' for testing
        if entered_otp == '123456':
            return render_template('success.html')
        else:
            return "Wrong OTP. Try again."
    return render_template('otp.html')

# Simulate Biometric
@app.route('/biometric', methods=['GET', 'POST'])
def biometric():
    if request.method == 'POST':
        # Simulate successful scan
        return render_template('success.html')
    return '''
    <h2>Biometric Scan</h2>
    <form method="POST">
        <button type="submit">Simulate Fingerprint Scan</button>
    </form>
    '''

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
