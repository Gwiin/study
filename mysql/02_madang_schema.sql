-- madang bookstore schema
-- Source: MySQL.txt madang schema section

CREATE DATABASE IF NOT EXISTS madang;
USE madang;

CREATE TABLE IF NOT EXISTS Book (
    bookid INTEGER PRIMARY KEY,
    bookname VARCHAR(40),
    publisher VARCHAR(40),
    price INTEGER
);

CREATE TABLE IF NOT EXISTS Customer (
    custid INTEGER PRIMARY KEY,
    name VARCHAR(40),
    address VARCHAR(40),
    phone VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS Orders (
    orderid INTEGER PRIMARY KEY,
    custid INTEGER,
    bookid INTEGER,
    saleprice INTEGER,
    orderdate DATE,
    FOREIGN KEY (custid) REFERENCES Customer(custid),
    FOREIGN KEY (bookid) REFERENCES Book(bookid)
);

DESC Book;
DESC Customer;
DESC Orders;
