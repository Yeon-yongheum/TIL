CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);
-- DATA 추가(C)
INSERT INTO classmates (name, age)
VALUES ('홍길동', 23);

-- 모든 열의 데이터를 넣을 때는 컬럼을 명시할 필요가 없다!
INSERT INTO classmates 
VALUES ('홍길동', 30, '서울');


SELECT rowid, * FROM classmates;

DROP TABLE classmates;

CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates 
VALUES (1, '홍길동', 30, '서울');

DROP TABLE classmates;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates 
VALUES ('연용흠', 30, '군대'), ('박태수', 100, '대전');
-- 특정 column 조회
SELECT age, name FROM classmates;
-- LIMIT
SELECT rowid, name FROM classmates LIMIT 1;
-- OFFSET
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- WHERE
SELECT rowid, name FROM classmates
WHERE address='서울';
-- 특정 column 중복 제거
SELECT DISTINCT age FROM classmates;
-- DELETE
DELETE FROM classmates WHERE rowid=3;
-- 마지막 데이터를 삭제하고 새롭게 추가해보면, 
-- id가 다시 활용되는 것을 볼 수 있다.
-- 이를 방지하려면, AUTOINCREMENT (django에서 id값)
CREATE TABLE tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
-- U
UPDATE classmates SET age=10 WHERE rowid=3;
SELECT rowid, * FROM classmates;