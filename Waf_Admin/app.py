from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # ログインページへのリダイレクトを行うなど、ルートパスの処理を記述する
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # POSTリクエストの処理
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('login.html')
    
        if username == 'admin' and password == 'password':
            # ログイン成功の場合は適切な処理を行う
            return redirect('rule_settings.html')  # ログイン後のページにリダイレクトするなど

            # ログイン失敗の場合はエラーメッセージを表示するなどの処理を行う
        else:
            return render_template('login.html', error_message='ログインに失敗しました')
    else:
        # GETリクエストの処理
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

    