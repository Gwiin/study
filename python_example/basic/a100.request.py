# pip freeze >> requirments.txt

import requests

url = "https://www.naver.com"
response = requests.get(url)

print("stats", response.status_code)
print(("text", response.text))
