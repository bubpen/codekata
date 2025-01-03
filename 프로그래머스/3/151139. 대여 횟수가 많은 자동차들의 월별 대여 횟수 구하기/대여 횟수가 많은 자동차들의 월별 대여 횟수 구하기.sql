-- 코드를 입력하세요
SELECT month(start_date) month, b.car_id, count(*) records
from car_rental_company_rental_history a join
(select car_id, count(*) count
from car_rental_company_rental_history
where left(start_date,7) between '2022-08' and '2022-10'
group by car_id
having count(*) >= 5) b on a.car_id = b.car_id
where left(start_date,7) between '2022-08' and '2022-10'
group by month(start_date),car_id
having count(*) != 0
order by month, car_id desc