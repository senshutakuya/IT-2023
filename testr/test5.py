import webbrowser
import string
import requests
from requests.auth import HTTPBasicAuth


url = "https://welp.melonkun.jp/login/"
url2 = "https://welp.melonkun.jp/home/"


auth = HTTPBasicAuth('melon', 'melon')

headers = {
    'Cookie': 'sord9lgel5cfn1pc2gdtf6pijm'
}

response = requests.post(url, headers=headers)

print(response.cookies)
print(response.text)

webbrowser.open(url2)