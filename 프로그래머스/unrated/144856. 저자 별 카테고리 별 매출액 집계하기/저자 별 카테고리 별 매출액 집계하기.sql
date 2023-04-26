-- 코드를 입력하세요
SELECT author.AUTHOR_ID, author.AUTHOR_NAME,	book.CATEGORY,	sum(book.price*sale.sales) AS TOTAL_SALES
FROM BOOK_SALES as sale
LEFT JOIN BOOK as book
ON sale.BOOK_ID = book.BOOK_ID
LEFT JOIN AUTHOR as author
ON book.AUTHOR_ID = author.AUTHOR_ID
WHERE DATE_FORMAT(sales_date,'%Y-%m') = '2022-01'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC


# SELECT *
# FROM BOOK_SALES as sale
# LEFT JOIN BOOK as book
# ON sale.BOOK_ID = book.BOOK_ID
# LEFT JOIN AUTHOR as author
# ON book.AUTHOR_ID = author.AUTHOR_ID
# WHERE DATE_FORMAT(sales_date,'%Y-%m') = '2022-01'