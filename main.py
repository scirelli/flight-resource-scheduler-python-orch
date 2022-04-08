from flask import Flask, render_template, request, url_for
from routes.routeConverters.RegexConverter import RegexConverter

app = Flask(__name__)

app.url_map.converters['regex'] = RegexConverter

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/login', methods=['POST'])
@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	return render_template('signin.html')

@app.route('/signup', methods=['POST'])
@app.route('/createuser', methods=['POST'])
def createUser():
	firstName = request.form['fistname']
	lastName = request.form['lastname']
	email = request.form['email']
	recaptchaToken = request.form['recaptcha']

	return render_template('signup.html')

@app.route('/<regex("[abcABC0-9]{4,6}"):uid>-<slug>/')
def example(uid, slug):
    return "uid: %s, slug: %s" % (uid, slug)

@app.route("/")
def index():
	return 'hello world'

@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    return 'You want path: %s' % path

if __name__ == "__main__":
	app.run()
