select YEAR(sale.sales_date) as y, MONTH(sale.sales_date) as m, us.gender as g, count(distinct(us.user_id)) as users
from online_sale as sale
left join user_info as us
on us.user_id = sale.user_id
where us.gender is not null
group by y,m,g
order by y,m,g

# select * from online_sale order by sales_date
