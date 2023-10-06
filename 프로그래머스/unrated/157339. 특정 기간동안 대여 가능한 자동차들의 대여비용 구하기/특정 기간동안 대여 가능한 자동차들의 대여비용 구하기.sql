select c.car_id, c.car_type, truncate((c.daily_fee * 30 * (100-p.discount_rate) / 100),0) as FEE
from CAR_RENTAL_COMPANY_CAR as c

left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as p
on p.car_type = c.car_type and p.duration_type = '30일 이상'


WHERE car_id not in (
                SELECT car_id
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
                WHERE '2022-11-01' BETWEEN h.start_date and h.end_date or '2022-11-30' BETWEEN h.start_date and h.end_date)
and
c.car_type in ('세단', 'SUV')

group by c.car_id
having fee between 500000 and 2000000
order by fee desc, car_type asc, car_id desc

