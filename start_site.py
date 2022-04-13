from flask import Flask, request, session, render_template
from my_function import max
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'
email = "your_email"

@app.route('/', methods=['POST', 'GET'])
def start():
    session['page'] = 0
    session['log_and_pas']=['test_login','test_password']
    return '<meta http-equiv="refresh" content="0;URL=/list" />'

@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        session['page'] += 1
        if max_leng <= session['page']:
            return '<meta http-equiv="refresh" content="0;URL=/end" />'
        with open('a_gen.txt', 'r') as file:
        	session['log_and_pas']=file.readlines()[session['page']][:-1].split(":")
    return render_template('bd.html',email=email, log=(session.get('log_and_pas'))[0], pas=(session.get('log_and_pas'))[1])

@app.route('/end', methods=['POST', 'GET'])
def end():
	if request.method == 'POST':
		return '<meta http-equiv="refresh" content="0;URL=/" />'
	return render_template('end.html')

if __name__ == "__main__":
    max_leng = max('a_gen.txt')
    app.run(host='0.0.0.0',port=5000)