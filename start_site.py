from flask import Flask, request, session, render_template
from my_function import max
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'

email = "your_email" # Ваша почта, будет отображаться на сайте к каждому акаунту
online = True #открыть сервер для сети? (True/False)

@app.route('/', methods=['POST', 'GET'])
def start():
    session['page'] = 0 #установление значения страницы для нового пользователя
    session['log_and_pas']=['test_login','test_password'] #установление значения последнего логина и пароля с последующим выводом пользователю
    return render_template('redirect.html',link = "/list")

@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        session['page'] += 1
        if max_leng <= session['page']:
            return render_template('redirect.html',link = "/end")
        with open('a_gen.txt', 'r') as file:
        	session['log_and_pas']=file.readlines()[session['page']][:-1].split(":")
    return render_template('bd.html',email=email, log=(session.get('log_and_pas'))[0], pas=(session.get('log_and_pas'))[1])

@app.route('/end', methods=['POST', 'GET'])
def end():
	if request.method == 'POST':
		return render_template('redirect.html',link = "/")
	return render_template('end.html')

if __name__ == "__main__":
    max_leng = max('a_gen.txt')
    app.run(host='0.0.0.0',port=5000) if online else app.run()