SELECT h.history_id, TRUNCATE(c.daily_fee * (DATEDIFF(h.end_date, h.start_date)+1) *(100-IFNULL(p.discount_rate, 0)) / 100, 0) as FEE
                                                        
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
JOIN CAR_RENTAL_COMPANY_CAR as c
ON c.car_id = h.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
ON p.car_type = c.car_type and (CASE 
                                WHEN DATEDIFF(h.end_date, h.start_date)+1 >= 90
                                THEN '90일 이상'
                                WHEN DATEDIFF(h.end_date, h.start_date)+1 >= 30
                                THEN '30일 이상'
                                WHEN DATEDIFF(h.end_date, h.start_date)+1 >= 7
                                THEN '7일 이상'
                                END)
                                = p.duration_type
WHERE c.car_type = '트럭'                           
ORDER BY FEE desc, h.history_id desc
