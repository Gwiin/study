# MySQL 학습 정리

## 저장소 구성

- `MySQL.txt`: 수업 중 작성한 원본 SQL 기록
- `01_iot_intro.sql`: database/table 생성 기초
- `02_madang_schema.sql`: `Book`, `Customer`, `Orders` schema
- `03_madang_seed.sql`: madang 예제 data
- `04_madang_queries.sql`: SELECT, 조건, 집계, JOIN, subquery
- `05_scott_schema_seed.sql`: DEPT/EMP 예제
- `06_dml_ddl_view.sql`: INSERT, UPDATE, DELETE, ALTER, VIEW

## SQL을 읽는 기본 순서

SQL은 작성 순서와 실제로 이해하는 순서가 조금 다름. `SELECT`가 맨 앞에 있지만, 먼저 봐야 할 것은 어떤 table에서 가져오는지임.

```text
FROM -> JOIN/ON -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
```

이 순서로 읽으면 복잡한 query도 “어디서 가져오고, 어떻게 거르고, 어떻게 묶고, 무엇을 보여주는가”로 나눌 수 있음.

## database와 table

database는 table을 담는 공간이고, table은 같은 형태의 row들을 담음. `CREATE DATABASE`, `USE`, `CREATE TABLE`, `SHOW TABLES`는 MySQL을 시작할 때 가장 먼저 보는 명령임.

```sql
CREATE TABLE IF NOT EXISTS student (
    id INT,
    name VARCHAR(10)
);
```

`IF NOT EXISTS`는 이미 table이 있을 때 오류를 줄이기 위한 조건임. column에는 이름과 type이 함께 필요함.

## primary key

primary key는 table 안에서 row를 구분하는 대표 값임. 같은 table 안에서 중복되면 안 되고, 보통 NULL도 허용하지 않음.

`Book(bookid)`, `Customer(custid)`, `Orders(orderid)`처럼 각 table의 row를 구분하는 값이 primary key가 됨.

## foreign key와 관계

관계형 database는 모든 정보를 한 table에 몰아넣지 않고 의미별 table로 나눔.

```text
Book: 책 정보
Customer: 고객 정보
Orders: 누가 어떤 책을 샀는지
```

`Orders`는 `custid`, `bookid`로 `Customer`, `Book`을 참조함.

```sql
FOREIGN KEY (custid) REFERENCES Customer(custid),
FOREIGN KEY (bookid) REFERENCES Book(bookid)
```

foreign key는 존재하지 않는 고객이나 책에 대한 주문이 생기지 않게 data 관계를 지켜줌.

## INSERT와 seed data

schema가 table의 구조라면 seed data는 실습 query를 실행하기 위한 기본 data임. `03_madang_seed.sql`은 `Book`, `Customer`, `Orders`에 예제 row를 넣음.

```sql
INSERT INTO Book VALUES (1, '축구의 역사', '굿스포츠', 7000);
INSERT INTO Customer VALUES (1, '박지성', '영국 맨체스타', '000-5000-0001');
```

column 순서에 맞춰 값을 넣는 방식임. 실무에서는 column 이름을 명시하는 방식이 더 안전함.

## WHERE

`WHERE`는 row를 조건으로 거름. 가격, 이름, 날짜, publisher 같은 column 값을 기준으로 필요한 row만 남김.

```sql
SELECT *
FROM Book
WHERE price BETWEEN 10000 AND 20000;
```

`BETWEEN`, `IN`, `LIKE`는 조건 검색에서 자주 나옴. 문자열 pattern 검색은 `LIKE`, 여러 후보 중 하나는 `IN`, 범위는 `BETWEEN`으로 읽으면 됨.

## 집계와 GROUP BY

집계 함수는 여러 row를 하나의 값으로 계산함.

- `COUNT`: 개수
- `SUM`: 합계
- `AVG`: 평균
- `MIN`, `MAX`: 최소/최대

`GROUP BY`는 row를 기준별로 묶은 뒤 각 그룹마다 집계를 계산함.

```sql
SELECT custid, COUNT(*) AS order_count, SUM(saleprice) AS total_price
FROM Orders
GROUP BY custid;
```

`WHERE`는 그룹으로 묶기 전에 row를 거르고, `HAVING`은 그룹으로 묶은 뒤 결과를 거름.

## JOIN

JOIN은 여러 table을 관계 조건으로 연결함. 주문 table만 보면 고객 이름과 책 제목을 알 수 없기 때문에 `Customer`, `Book`을 함께 연결함.

```sql
SELECT C.name, B.bookname, O.saleprice
FROM Customer C
JOIN Orders O ON C.custid = O.custid
JOIN Book B ON O.bookid = B.bookid;
```

JOIN에서 가장 중요한 것은 연결 조건임. 조건을 빠뜨리면 모든 row 조합이 만들어지는 cross join이 되어 결과가 폭발적으로 늘어남.

## subquery

subquery는 query 안에 들어가는 query임. 먼저 어떤 값을 구하고, 그 값을 바깥 query의 조건으로 사용할 때 유용함.

```sql
SELECT bookname
FROM Book
WHERE price = (SELECT MAX(price) FROM Book);
```

이 예제는 가장 비싼 가격을 먼저 구한 뒤, 그 가격을 가진 책을 찾음. JOIN이 table 관계를 펼쳐서 보는 방식이라면, subquery는 조건을 단계적으로 계산하는 방식에 가깝음.

## DML과 DDL

DML은 data를 바꾸는 명령임.

- `INSERT`: row 추가
- `UPDATE`: row 수정
- `DELETE`: row 삭제

DDL은 구조를 바꾸는 명령임.

- `CREATE`: database/table/view 생성
- `ALTER`: table 구조 변경
- `DROP`: 구조 삭제

`ALTER TABLE`은 기존 data와 충돌할 수 있음. 예를 들어 NULL이 들어 있는 column에 `NOT NULL`을 추가하면 실패할 수 있음.

## VIEW

VIEW는 query에 이름을 붙인 가상 table임. 복잡한 JOIN을 매번 쓰지 않고 재사용할 수 있음.

```sql
CREATE OR REPLACE VIEW V_orders AS
SELECT orderid, O.custid, name, B.bookid, bookname
FROM Customer C, Orders O, Book B
WHERE C.custid = O.custid
  AND B.bookid = O.bookid;
```

VIEW는 원본 data를 복사해 저장하는 것이 아니라, 조회할 때 정의된 query를 실행해 결과를 보여주는 방식으로 이해하면 됨.

## `ON DELETE CASCADE`

foreign key에 `ON DELETE CASCADE`를 붙이면 부모 row가 삭제될 때 연결된 자식 row도 함께 삭제됨. 편리하지만 위험함. 고객을 삭제했을 때 주문 기록까지 같이 사라지는 것이 맞는지 먼저 판단해야 함.
