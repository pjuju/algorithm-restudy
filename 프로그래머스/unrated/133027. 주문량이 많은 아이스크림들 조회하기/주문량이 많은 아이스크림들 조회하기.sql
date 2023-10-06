SELECT flavor FROM (SELECT * FROM FIRST_HALF
                        UNION ALL
                        SELECT * FROM JULY) as t
group by flavor
order by sum(total_order) desc limit 3


