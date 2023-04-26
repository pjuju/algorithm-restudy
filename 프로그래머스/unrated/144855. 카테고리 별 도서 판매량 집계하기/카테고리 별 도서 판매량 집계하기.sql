-- 코드를 입력하세요
SELECT book.category as CATEGORY, sum(sale.sales) as TOTAL_SALES
FROM BOOK_SALES as sale
LEFT JOIN BOOK as book
ON sale.book_id = book.book_id
WHERE DATE_FORMAT(sale.sales_date, '%Y-%m') = '2022-01'
group by CATEGORY
order by CATEGORY