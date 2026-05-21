
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    # 일반 변수: 문자열, 정수, 불리언
    page_title = 'Flask jinja 문법 학습'
    classMonth = 2 # 3개월차
    is_active = True
    # 파이썬: 딕셔너리, 데이터/웹: json
    user_info = {"username":"iot_class", "level":"bootcamp"} 
    # 파이썬: 리스트, C/java: 배열
    items = ["Flask 배우기", "jinja 이해", "예쁜 웹앱 만들기"]
    return render_template('index.html', user=user_info, tasks=items, title = page_title, chasu=classMonth, on_class = is_active)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
