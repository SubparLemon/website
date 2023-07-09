from flask import Flask, render_template, url_for, redirect, send_file

app = Flask(__name__)

@app.route('/')
def redirectohome():
    return redirect(url_for('home'))

@app.route('/home')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/bylaws')
def bylaws():
    return send_file('AHEAD_BYLAWS_26JUN2023_lshi.docx.pdf')


if __name__ == '__main__':
    app.run()
