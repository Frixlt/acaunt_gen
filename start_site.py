from flask import Flask, request, session, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'
x_email = "your_email"

def max():
    with open('a_gen.txt', 'r') as file:
        lines = 0
        for line in file.readlines():
            lines += 1
    return lines

@app.route('/', methods=['POST', 'GET'])
def start():
    session['page'] = 0
    session['last_log_and_pas']=['test','test']
    return '<meta http-equiv="refresh" content="0;URL=/list" />'

@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        session['page'] += 1
        if max_leng <= session['page']:
            return '<meta http-equiv="refresh" content="0;URL=/end" />'
        with open('a_gen.txt', 'r') as file:
        	session['last_log_and_pas']=file.readlines()[session['page']][:-1].split(":")
    return render_template('bd.html',email=x_email, l_a_p=session.get('last_log_and_pas'))

@app.route('/end', methods=['POST', 'GET'])
def end():
	if request.method == 'POST':
		return '<meta http-equiv="refresh" content="0;URL=/" />'
	return render_template('end.html')

if __name__ == "__main__":
    max_leng = max()
    app.run(host='0.0.0.0',port=5000)