-- madang SELECT, aggregate, join, and subquery practice
-- Run after 02_madang_schema.sql and 03_madang_seed.sql.

USE madang;

-- Q3-1: 모든 도서의 이름과 가격 조회
SELECT bookname, price FROM Book;

-- Q3-3: 출판사 중복 제거
SELECT DISTINCT publisher FROM Book;

-- Q3-4: 가격이 20000 미만인 도서
SELECT * FROM Book WHERE price < 20000;

-- Q3-5: 가격이 10000 이상 20000 이하인 도서
SELECT * FROM Book WHERE price BETWEEN 10000 AND 20000;
SELECT * FROM Book WHERE price >= 10000 AND price <= 20000;

-- Q3-6: 출판사가 굿스포츠 또는 대한미디어인 도서
SELECT * FROM Book WHERE publisher = '굿스포츠' OR publisher = '대한미디어';
SELECT * FROM Book WHERE publisher IN ('굿스포츠', '대한미디어');

-- LIKE wildcard search
SELECT * FROM Book WHERE bookname LIKE '%축구%';

-- Q3-13: 도서를 가격순으로 검색, 가격이 같으면 이름순
SELECT * FROM Book ORDER BY price, bookname;

-- Q3-14: 가격 내림차순, 가격이 같으면 출판사 오름차순
SELECT * FROM Book ORDER BY price DESC, publisher ASC;

-- Q3-15: 총매출
SELECT SUM(saleprice) AS total_sales FROM Orders;

-- Q3-16: 2번 고객이 주문한 총 판매액
SELECT SUM(saleprice) AS total_sales FROM Orders WHERE custid = 2;

-- Q3-19: 고객별 주문 도서 수량과 총 판매액
SELECT custid, COUNT(*) AS book_count, SUM(saleprice) AS total_sales
FROM Orders
GROUP BY custid;

-- Q3-20: 판매가격 8000 이상 주문 중 2권 이상 구매한 고객
SELECT custid, COUNT(*) AS book_count
FROM Orders
WHERE saleprice >= 8000
GROUP BY custid
HAVING COUNT(*) >= 2;

-- Cross join 형태. 실무에서는 join condition 없이 사용하지 않도록 주의.
SELECT * FROM Customer, Orders;

-- Customer와 Orders join
SELECT *
FROM Customer, Orders
WHERE Customer.custid = Orders.custid;

-- 박지성이 구매한 도서 목록
SELECT *
FROM Customer
INNER JOIN Orders ON Customer.custid = Orders.custid
WHERE name = '박지성';

SELECT name, bookname
FROM Customer, Orders, Book
WHERE Customer.custid = Orders.custid
  AND Orders.bookid = Book.bookid
  AND name = '박지성';

SELECT name, bookname
FROM Customer
INNER JOIN Orders ON Customer.custid = Orders.custid
INNER JOIN Book ON Orders.bookid = Book.bookid
WHERE name = '박지성';

-- 고객별 판매액
SELECT name, saleprice
FROM Customer
INNER JOIN Orders ON Customer.custid = Orders.custid;

SELECT name, SUM(saleprice) AS total_sales
FROM Customer
LEFT JOIN Orders ON Customer.custid = Orders.custid
GROUP BY name;

SELECT name, SUM(saleprice) AS total_sales
FROM Customer
RIGHT JOIN Orders ON Customer.custid = Orders.custid
GROUP BY name;

-- 가장 비싼 도서
SELECT bookname
FROM Book
WHERE price = (SELECT MAX(price) FROM Book);

-- 도서를 구매한 이력이 있는 고객의 이름
SELECT name
FROM Customer
JOIN Orders ON Customer.custid = Orders.custid
GROUP BY Customer.name;

SELECT DISTINCT name
FROM Customer
JOIN Orders ON Customer.custid = Orders.custid;

SELECT name
FROM Customer
WHERE custid IN (SELECT custid FROM Orders);

-- 대한미디어에서 출판한 도서를 구매한 고객의 이름
SELECT name
FROM Customer
WHERE custid IN (
    SELECT custid
    FROM Orders
    WHERE bookid IN (
        SELECT bookid
        FROM Book
        WHERE publisher = '대한미디어'
    )
);

-- 출판사별 평균 도서 가격보다 비싼 도서
SELECT b1.bookname
FROM Book b1
WHERE b1.price > (
    SELECT AVG(b2.price)
    FROM Book b2
    WHERE b2.publisher = b1.publisher
);

SELECT b1.bookname
FROM Book b1
JOIN (
    SELECT publisher, AVG(price) AS avg_price
    FROM Book
    GROUP BY publisher
) b2 ON b1.publisher = b2.publisher
WHERE b1.price > b2.avg_price;

-- 김연아 고객이 주문한 도서의 총판매액
SELECT SUM(saleprice) AS total_sales
FROM Orders
WHERE custid = (
    SELECT custid
    FROM Customer
    WHERE name = '김연아'
);

SELECT SUM(saleprice) AS total_sales
FROM Customer
JOIN Orders ON Customer.custid = Orders.custid
WHERE Customer.name = '김연아';

-- 정가가 20000원인 도서를 주문한 고객의 이름과 주소
SELECT name, address
FROM Customer
WHERE custid IN (
    SELECT custid
    FROM Orders
    WHERE bookid IN (
        SELECT bookid
        FROM Book
        WHERE price = 20000
    )
);

SELECT name, address
FROM Customer
JOIN Orders ON Customer.custid = Orders.custid
JOIN Book ON Orders.bookid = Book.bookid
WHERE Book.price = 20000;

-- 도서 가격과 판매가격의 차이가 가장 큰 주문
SELECT Orders.orderid AS order_id, (price - saleprice) AS price_gap
FROM Orders
JOIN Book ON Orders.bookid = Book.bookid
WHERE (price - saleprice) = (
    SELECT MAX(price - saleprice)
    FROM Orders
    JOIN Book ON Orders.bookid = Book.bookid
);
