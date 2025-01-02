select author.author_id, author_name, category, sum(sales * price) total_sales
from book
join 
author on book.author_id = author.author_id
join book_sales on book.book_id = book_sales.book_id
where left(sales_date,7) = '2022-01'
group by author.author_id, author_name, category
order by author_id asc, category desc