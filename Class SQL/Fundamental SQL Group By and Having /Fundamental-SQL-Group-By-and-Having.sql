# Menampilkan detail konsumen
SELECT b.name, b.address, b.phone, a.product_id, a.subscription_date 
FROM subscription a 
JOIN customer b 
ON a.customer_id = b.id
WHERE b.id IN 
(
	SELECT customer_id 
  FROM Subscription 
  GROUP BY customer_id 
  HAVING COUNT(customer_id) > 1
) 
ORDER BY b.id ASC;

# Penggunaan Fungsi MAX
select product_id, max(total_price) total
from invoice
group by product_id;
select product_id, max(total_price) total
from invoice
group by product_id
having max(total_price) > 1000000;
select product_id, max(pinalty) total
from invoice
group by product_id
having max(pinalty) > 30000;

# Penggunaan Fungsi MIN
select product_id, min(total_price) total
from invoice
group by product_id;
select product_id, min(total_price) total
from invoice
group by product_id
having min(total_price) < 500000;
select product_id, min(pinalty) total
from invoice
group by product_id
having min(pinalty) < 50000;

# Penggunaan Fungsi AVG
select product_id, avg(total_price) total
from invoice
group by product_id;
select product_id, avg(total_price) total
from invoice
group by product_id
having min(total_price) > 100000;
select product_id, avg(pinalty) total
from invoice
group by product_id
having avg(pinalty) > 30000;

# Mini Quiz
select product_id, AVG(pinalty), count(customer_id) total
from invoice
group by product_id
having count(customer_id) > 20;
