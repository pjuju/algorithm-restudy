select food.product_id as PRODUCT_ID, food.product_name as PRODUCT_NAME, sum(food.price * ord.amount) as TOTAL_SALES

from food_order as ord
left join food_product as food
on ord.product_id = food.product_id
where DATE_FORMAT(ord.produce_date, '%Y-%m') = '2022-05'
group by PRODUCT_ID, PRODUCT_NAME
order by TOTAL_SALES DESC, PRODUCT_ID