# pip install flask flask-mysqldb werkzeug python-dotenv

# CREATE database bookstore_flask;
# USE bookstore_flask;


# CREATE TABLE book(
#     bookid int primary key auto_increment,
#     bookname varchar(40) not null,
#     publisher varchar(40),
#     price int
# );

# CREATE TABLE customer(
#     custid int primary key auto_increment,
#     name varchar(40) not null,
#     address varchar(40),
#     phone varchar(40),
#     password varchar(255) not null
# );

# CREATE TABLE orders(
#     orderid int primary key auto_increment,
#     custid int,
#     bookid int,
#     saleprice int,
#     orderdate date,
#     foreign key (custid) references customer(custid) on delete cascade,
#     foreign key (bookid) references book(bookid) on delete cascade
# );

# on delete cascade: 책/고객이 삭제되면 관련주문도 삭제

# CRUD      /   SQL     /   WEB(Restful API)
# Create    /   insert  /   POST
# Read      /   select  /   GET (Ex 브라우저 주소 창 입력)
# Update    /   update  /   PUT(한줄 전체 교체) or patch(특정 값만 교체)
# Delete    /   delete  /   delete


from flask import Flask, render_template, request, jsonify, session, url_for, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from dotenv import load_dotenv
import os

#env file을 관리하는 이유: github 올릴 때 gitignore 파일에 .env를 등록
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
#MYSQL_HOST=localhost
#MYSQL_USER=root
#MYSQL_PASSWORD=1234
#MYSQL_DB=bookstore_flask
#위 주석내용은 코드에 두지않도록 할것

app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

def is_logged_in(): #로그인 상태 확인
    return 'logged_in' in session

@app.route('/')
def index():
    if is_logged_in(): return redirect(url_for('books_page'))
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/books')
def books_page():
    if not is_logged_in(): return redirect(url_for('index'))
    return render_template('books.html')

@app.route('/add_book')
def add_books_page():
    if not is_logged_in(): return redirect(url_for('index'))
    return render_template('add_book.html')


# /api/books GET --------------------------------
@app.route('/api/books',methods=['GET'])
def api_get_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM book")
    books = cur.fetchall()
    cur.close()
    return jsonify(books)


@app.route('/api/add_book', methods=['POST'])
def api_add_book():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO book(bookname, publisher, price) values(%s, %s, %s)", (data['bookname'],data['publisher'], data['price']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"success":True})


# /api/order POST
@app.route('/api/order', methods=['POST'])
def api_order():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO orders(custid, bookid, saleprice, orderdate) values(%s, %s, %s, %s)", (session['custid'],data['bookid'], data['price'],datetime.now().date()))
    mysql.connection.commit()
    cur.close()
    return jsonify({"success":True})

# /my_orders
@app.route('/my_orders')
def my_order_page():
    if not is_logged_in(): return redirect(url_for('index'))
    return render_template('my_orders.html')


@app.route('/api/my_orders',methods=['GET'])
def api_get_orders():
    cur = mysql.connection.cursor()
    cur.execute("""
                SELECT o.orderid, o.orderdate, o.saleprice, b.bookname
                FROM orders o
                JOIN book b
                ON o.bookid = b.bookid
                WHERE o.custid =%s
                """, [session['custid']])
    orders = cur.fetchall()
    cur.close()
    return jsonify(orders)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO customer(name, address, phone, password) VALUES(%s, %s, %s, %s)",\
                 (data['name'],data['address'],data['phone'],hashed_pw))
    mysql.connection.commit()
    cur.close()
    return jsonify({"success":True,"message":"회원 가입 잘 되었음"})
    pass # 수신, DB에 insert

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer WHERE name=%s", (data['name'],))
    user = cur.fetchone()
    cur.close()
    if user and check_password_hash(user['password'], data['password']):
        session.update({'logged_in':True, 'custid':user['custid'], 'name':user['name']})
        return jsonify({'success':True})
    return jsonify({"success":False, "message":"ID or PW 통과 못함"})







if __name__ == "__main__":
    app.run(debug=True, port=5000, host = '127.0.0.1')
