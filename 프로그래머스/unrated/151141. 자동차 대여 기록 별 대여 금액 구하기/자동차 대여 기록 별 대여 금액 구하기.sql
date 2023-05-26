-- 코드를 입력하세요

SELECT h.history_id, TRUNCATE((DATEDIFF(h.end_date,h.start_date)+1) * c.daily_fee,0) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
LEFT JOIN CAR_RENTAL_COMPANY_CAR as c
ON h.car_id = c.car_id
WHERE DATEDIFF(h.end_date,h.start_date)+1 < 7 and c.car_type = '트럭'
UNION ALL

SELECT h.history_id, TRUNCATE(((DATEDIFF(h.end_date,h.start_date)+1) * c.daily_fee * (100-p.discount_rate) / 100),0) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
LEFT JOIN CAR_RENTAL_COMPANY_CAR as c
ON h.car_id = c.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
ON p.car_type = c.car_type and p.duration_type ='7일 이상'
WHERE 7 <= DATEDIFF(h.end_date,h.start_date)+1 and DATEDIFF(h.end_date,h.start_date)+1 < 30  and c.car_type = '트럭'

UNION ALL

SELECT h.history_id, TRUNCATE(((DATEDIFF(h.end_date,h.start_date)+1) * c.daily_fee * (100-p.discount_rate) / 100),0) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
LEFT JOIN CAR_RENTAL_COMPANY_CAR as c
ON h.car_id = c.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
ON p.car_type = c.car_type and p.duration_type ='30일 이상'
WHERE 30 <= DATEDIFF(h.end_date,h.start_date)+1 and DATEDIFF(h.end_date,h.start_date)+1 < 90 and c.car_type = '트럭'

UNION ALL

SELECT h.history_id, TRUNCATE(((DATEDIFF(h.end_date,h.start_date)+1) * c.daily_fee * (100-p.discount_rate) / 100),0) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
LEFT JOIN CAR_RENTAL_COMPANY_CAR as c
ON h.car_id = c.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
ON p.car_type = c.car_type and p.duration_type ='90일 이상'
WHERE 90 <= DATEDIFF(h.end_date,h.start_date)+1 and c.car_type = '트럭'


ORDER BY FEE DESC, history_id DESC