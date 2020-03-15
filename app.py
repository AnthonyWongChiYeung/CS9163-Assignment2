from flask import Flask, render_template, request
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    user_name = request.form.get('uname')
    password = request.form.get('psw')
    login_success = False
    if user_name:
        results = db.get_info(user_name, password);
        login_success = bool(results)
    if login_success:
        return render_template('result.html', results=results)
    else:
        return render_template('index.html', user_name=user_name)


@app.after_request
def add_security_headers(resp):
    resp.headers['X-XSS-Protection'] = 0
    return resp