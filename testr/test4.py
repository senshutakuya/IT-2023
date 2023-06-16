import requests
from requests.auth import HTTPBasicAuth

url = "https://welp.melonkun.jp/login/"
url2 = "https://welp.melonkun.jp/home/"

auth = HTTPBasicAuth('aaaa@gmail.com', 'aaaa')

session = requests.Session()

response = session.post(url, auth=auth)

if response.status_code == 200 and response.url == url2:
    print("ログインに成功しました。")
    print("メールアドレス: aaaa@gmail.com")
    print("パスワード: aaaa")
else:
    print("ログインに失敗しました。")
