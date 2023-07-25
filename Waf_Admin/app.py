from flask import Flask, request, render_template, redirect,url_for,session
# import flask という行は、 flask という名前のモジュールを読み込んで、 flask という名前の変数に代入しています。 Python は数値や文字列だけでなく、モジュールやクラスなども全てオブジェクトで、 変数に代入して利用しています
from config import auth_test
# configフォルダのauth_test.pyを指定
# 緑になってなくて心配だと思うけど、フォルダを指定してるからだよ


app = Flask(__name__)
# app = flask.Flask(__name__) という行は、 Flask クラスのインスタンスを作って、 app という変数に代入しています。 オブジェクトの属性にアクセスする場合は、 . という記号を使って、 オブジェクト名.要素名 のようにします

#configフォルダーのauth_test.pyファイルのsecretkeyを指定
app.secret_key = auth_test.SECRET_KEY


# URLを/だけにされたら実行される
@app.route('/', methods=['GET'])
# index関数を宣言
def index():
    # ログインページへのリダイレクトを行うなど、ルートパスの処理を記述する
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
# login関数を宣言
# 基本的にlogin.htmlに飛ばすだけ
def login():
    if request.method == 'POST':
        # POSTリクエストの処理

        return render_template('login.html')
    

    else:
        # GETリクエストの処理
        return render_template('login.html')
    

@app.route('/home', methods=['GET','POST'])
# URLが/homeとなった際のgetとpostの際の処理
def home():
        if request.method == 'POST':
            #ポストの処理
            username = request.form.get("username")
            # username変数にlogin.htmlからログイン処理の際に入力したusernameを代入
            password = request.form.get("password")
            # password変数にlogin.htmlからログイン処理の際に入力したpasswordを代入

            

            if username == auth_test.USERNAME and password == auth_test.PASSWORD:
                # もしusernameがauth_test.pyのUSERNAMEと同じでpasswordがauth_test.pyのPASSWORDと同じなら
                # ログイン成功の場合は適切な処理を行う
                return render_template('rule_settings.html')  # ログイン後のページに飛ばす
            else:
                # ログイン失敗の場合はlogin関数にリダイレクト処理をしてlogin.htmlにリダイレクトで飛ばす    
                return redirect(url_for('login'))
        else:
                    # GETリクエストの処理
            if 'username' in session and session['username'] == auth_test.USERNAME:
                # 'username' in sessionという条件で、セッションに'username'というキーが存在するかどうかを確認
                # さらにそのsessionのusernameの値がauth_test.pyのUSERNAME の値と同じか確認する

                # ログイン済みの場合は適切な処理を行う
                return render_template('rule_settings.html')  # ログイン後のページを表示
            else:
                # ログインしていない場合はログインページにリダイレクトする
                return redirect(url_for('login'))
                

if __name__ == '__main__':
    # もしもこのプログラムが実行されたら
    app.debug = True
    # debug=Trueとするとデバッグモードで立ち上がる。
    # エラーが出た時のエラー画面最下部に見えるエラーメッセージの右端のターミナルのようなものをクリックする。
    # すると、PINの入力が求められるので、ターミナルに表示されていたPINを入力する。
    # (app.pyを実行した時にターミナルで出るPINcode)
    # すると、コンソールが表示されて、様々な値を入力して何が正しいのか確かめる事ができる。
    app.run()
    # 実行する時のおまじない

    