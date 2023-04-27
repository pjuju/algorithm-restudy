-- 코드를 입력하세요
SELECT c.car_id, c.car_type, TRUNCATE(c.daily_fee * (100-d.discount_rate) * 0.3,-1) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as r
JOIN CAR_RENTAL_COMPANY_CAR as c ON c.car_id = r.car_id
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN as d ON c.car_type = d.car_type
WHERE d.duration_type = '30일 이상' and  c.car_id not in (SELECT car_id 
                                                      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                                      WHERE '2022-11' BETWEEN DATE_FORMAT(start_date, '%Y-%m')
                                                                    AND DATE_FORMAT(end_date, '%Y-%m')) 
GROUP BY c.car_id HAVING FEE >= 500000 and FEE < 2000000
ORDER BY FEE DESC, car_type, car_id DESC
