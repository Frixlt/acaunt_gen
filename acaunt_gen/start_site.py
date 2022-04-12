from flask import Flask, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERY_SECRET_KEY'
x = ['test', 'test']
head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>топовый текст</title>
<script>
function copylogin() {
  var copyText = document.getElementById("login");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
}
function copypassword() {
  var copyText = document.getElementById("password");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
}
function copyemail() {
  var copyText = document.getElementById("email");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
}
</script> '''
body = f'''
</head>
    <body>
        <input type="text" value="maksproo22@gmail.com" id="email">
        <button onclick="copyemail()">Скопировать текст</button>
        <br>
        <input type="text" value="{x[0]}" id="login">
        <button onclick="copylogin()">Скопировать текст</button>
        <br>
        <input type="text" value="{x[1]}" id="password">
        <button onclick="copypassword()">Скопировать текст</button>
        <form method="post">
            <button type="submit" class="registerbtn">следующая страница</button>
        </form>
    </body>
</html>
'''

def max():
    with open('a_gen.txt', 'r') as file:
        lines = 0
        for line in file.readlines():
            lines += 1
    return lines
print(max())

@app.route('/', methods=['POST', 'GET'])
def start():
    session['page'] = 0
    return '<meta http-equiv="refresh" content="0;URL=/list" />'

@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        session['page'] += 1
        print(session['page'])
        if max_leng <= session['page']:
            return "END!"
        with open('a_gen.txt', 'r') as file:
	        x = file.readlines()[session['page']][:-1].split(":")
        return head + f'''
</head>
    <body>
        <input type="text" value="maksproo22@gmail.com" id="email">
        <button onclick="copyemail()">Скопировать текст</button>
        <br>
        <input type="text" value="{x[0]}" id="login">
        <button onclick="copylogin()">Скопировать текст</button>
        <br>
        <input type="text" value="{x[1]}" id="password">
        <button onclick="copypassword()">Скопировать текст</button>
        <form method="post">
            <button type="submit" class="registerbtn">следующая страница</button>
        </form>
    </body>
</html>
'''
    return head + body
if __name__ == "__main__":
    max_leng = max()
    app.run(host='0.0.0.0',port=5000)
# host='0.0.0.0',port=5000