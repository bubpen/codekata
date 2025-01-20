-- 코드를 입력하세요
select year(sales_date) year, month(sales_date) month,  count(distinct s.user_id) as purchased_users, round(count(distinct s.user_id)/cnt, 1) puchased_ratio
from
online_sale s join
(
select *
from user_info
where joined like '2021%'
) u
on s.user_id = u.user_id
join
(
select count(*) cnt
from user_info
where joined like '2021%'
) c
group by 1, 2

