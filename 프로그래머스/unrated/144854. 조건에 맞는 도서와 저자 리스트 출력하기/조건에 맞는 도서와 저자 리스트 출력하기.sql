-- 코드를 입력하세요
SELECT b.book_id as BOOK_ID, a.author_name as AUTHOR_NAME, DATE_FORMAT(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK as b
JOIN AUTHOR as a ON b.author_id = a.author_id 
WHERE b.CATEGORY = '경제'
order by b.published_date ASC;