set @entire_cnt = 0;

select count(*) into @entire_cnt
from user_info
where YEAR(joined) = '2021';
            


select YEAR(sales_date) as YEAR, MONTH(sales_date) as MONTH, COUNT(DISTINCT(user_id)) as PUCHASED_USERS, ROUND(COUNT(DISTINCT(user_id))/@entire_cnt, 1) as PUCHASED_RATIO
from online_sale
where user_id in (
    select user_id
    from user_info
    where YEAR(joined) = '2021')
group by YEAR, MONTH
order by YEAR,MONTH