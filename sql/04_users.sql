.mode csv
.import users.csv users

-- 1. 나이가 30 이상인 사람
SELECT * FROM users WHERE age >= 30;
-- 2. 나이가 30 이상인 사람의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 3. 30이상, 김씨
SELECT first_name, age FROM users 
WHERE age >= 30 and last_name = '김';
-- 4. 30이상, 김씨 인원수
SELECT COUNT(*) FROM users
WHERE age >= 30 and last_name = '김';
-- 5. 전체 데이터 갯수
SELECT COUNT(*) FROM users;
-- 6. 전체 평균 나이
SELECT AVG(age) FROM users;
-- 7. 30 이상 평균 나이
SELECT AVG(age) FROM users
WHERE age >= 30;
-- 8. 계좌 잔액이 가장 높은 사람 이름과 액수
SELECT first_name, MAX(balance) FROM users;
-- 9. 30살 이상 평균 잔액
SELECT AVG(balance) FROM users
WHERE age >= 30;
-- 10. 20대인 사람
SELECT COUNT(*) FROM users
WHERE age LIKE '2_';
-- 11. 지역번호가 02인 사람(서울)
SELECT COUNT(*) FROM users
WHERE phone LIKE '02-%';
-- 12. 이름이 '준'으로 끝나는 사람
SELECT COUNT(*) FROM users
WHERE first_name LIKE '%준';
-- 13. 중간 번호 5114
SELECT first_name FROM users
WHERE phone LIKE '%-5114-%';
-- 14. 나이 많은 사람 10명
SELECT first_name, last_name, age FROM users
ORDER BY age DESC LIMIT 10;
-- 15. 나이, 성순으로 오름차순 10명
SELECT first_name, last_name, age FROM users
ORDER BY age, last_name ASC LIMIT 10;
-- 16. 
SELECT first_name, last_name, age FROM users
ORDER BY age, last_name ASC LIMIT 1 OFFSET 9;