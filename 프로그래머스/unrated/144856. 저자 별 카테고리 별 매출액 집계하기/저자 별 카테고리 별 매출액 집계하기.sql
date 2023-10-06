select a.author_id, a.author_name, b.category, sum(b.price * s.sales)
from book_sales as s
left join book as b
on s.book_id = b.book_id
left join author as a
on a.author_id = b.author_id
where date_format(s.sales_date, '%Y-%m') = '2022-01'
group by a.author_id, b.category 
order by a.author_id, b.category desc

