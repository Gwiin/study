-- DML, DDL, cascade, and view practice
-- Some destructive commands from the original note are kept as comments.

USE madang;

-- INSERT with selected columns
INSERT INTO Book(bookid, bookname, publisher)
VALUES (11, '스포츠 의학', '고려대학교');

-- Multiple row insert
INSERT INTO Book(bookid, bookname, publisher)
VALUES
    (12, '스포츠 의학2', '고려대학교'),
    (13, '스포츠 의학3', '고려대학교');

-- Q3-47: customer address update
UPDATE Customer
SET address = '대한민국 부산'
WHERE custid = 5;

-- MySQL에서는 같은 table을 update하면서 바로 같은 table을 subquery로 참조할 때 제약이 생길 수 있다.
-- 이런 경우 먼저 대상 key를 조회하고, 그 결과로 update하는 2-pass 방식을 사용할 수 있다.
SELECT custid FROM Customer WHERE name = '박세리';

-- Q3-49: inserted practice rows cleanup
DELETE FROM Book
WHERE bookid > 10;

-- Destructive cleanup examples from the original note:
-- DELETE FROM Orders;
-- DELETE FROM Book;
-- DROP TABLE Orders;
-- DROP TABLE Book;

CREATE TABLE IF NOT EXISTS NewOrders (
    orderid INTEGER PRIMARY KEY,
    custid INTEGER,
    bookid INTEGER,
    saleprice INTEGER,
    orderdate DATE,
    FOREIGN KEY (custid) REFERENCES Customer(custid) ON DELETE CASCADE,
    FOREIGN KEY (bookid) REFERENCES Book(bookid) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS NewBook (
    bookid INTEGER,
    bookname VARCHAR(40),
    publisher VARCHAR(40),
    price INTEGER
);

ALTER TABLE NewBook ADD isbn VARCHAR(13);
ALTER TABLE NewBook MODIFY isbn INTEGER;
ALTER TABLE NewBook DROP COLUMN isbn;
ALTER TABLE NewBook MODIFY bookname VARCHAR(40) NOT NULL;
ALTER TABLE NewBook ADD PRIMARY KEY(bookid);

CREATE OR REPLACE VIEW V_orders AS
SELECT orderid, O.custid, name, B.bookid, bookname
FROM Customer C, Orders O, Book B
WHERE C.custid = O.custid
  AND B.bookid = O.bookid;

SELECT * FROM V_orders;
