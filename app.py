from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        voter_id = request.form['voterId']
        email = request.form['email']
        captcha_input = int(request.form['captchaInput'])
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        # Validate CAPTCHA
        if captcha_input != num1 + num2:
            flash('Wrong CAPTCHA, please try again.')
            return render_template('login.html')

        # Check Voter ID and Email in the database
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE voter_id = ? AND email = ?',
                            (voter_id, email)).fetchone()
        conn.close()

        if user is None:
            flash('Invalid Voter ID or Email.')
            return render_template('login.html')

        # If CAPTCHA and credentials are correct, redirect to OTP verification page
        return redirect(url_for('otp_verification'))

    return render_template('login.html')

@app.route('/otp_verification', methods=['GET', 'POST'])
def otp_verification():
    if request.method == 'POST':
        otp_entered = request.form['otp']
        # You can add your OTP validation logic here

        # For now, let's assume the OTP is always correct for demonstration
        flash('OTP verified successfully!')
        return redirect(url_for('success_page'))  # Redirect to a success page or dashboard

    return render_template('otp.html')


if __name__ == '__main__':
    app.run(debug=True)
