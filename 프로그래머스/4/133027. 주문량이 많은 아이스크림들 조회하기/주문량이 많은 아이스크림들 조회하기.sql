-- 코드를 입력하세요
SELECT f.flavor
from first_half f join 
(
select flavor, sum(total_order) total_order
from july
group by flavor
) j
on f.flavor = j.flavor
order by (j.total_order + f.total_order) desc
limit 3