-- Chapter - 1
-- Pengenalan Table - Customer
select * from customer;
-- Pengenalan Table - Product
select * from product;
-- Pengenalan Table - Subscription
SELECT * FROM subscription;
-- Pengenalan Table - Invoice
select * from invoice;
-- Pengenalan Table - Payment
SELECT * FROM payment;

-- Chapter - 2
-- Contoh penggunaan HAVING
SELECT customer_id FROM Subscription GROUP BY customer_id HAVING COUNT(customer_id) > 1
-- Menampilkan Konsumen yang berubah berlangganan
SELECT customer_id, product_id, subscription_date
FROM Subscription 
WHERE customer_id IN (
  SELECT customer_id 
  FROM Subscription 
  GROUP BY customer_id 
  HAVING COUNT(customer_id) > 1
  ) 
ORDER BY customer_id ASC;
-- Menampilkan detail konsumen
SELECT b.name, b.address, b.phone, a.product_id, a.subscription_date 
FROM subscription a 
JOIN customer b 
ON a.customer_id=b.id
WHERE b.id IN (
  SELECT customer_id 
  FROM Subscription 
  GROUP BY customer_id 
  HAVING COUNT(customer_id) > 1
  ) 
ORDER BY b.id ASC;

-- Chapter - 3
-- Penggunaan Fungsi MAX pada Having
SELECT product_id, max(total_price) total
FROM invoice
GROUP BY product_id;
SELECT product_id, max(total_price) total
FROM invoice
GROUP BY product_id
HAVING max(total_price) > 1000000;
SELECT product_id, max(pinalty) pinalty
FROM invoice
GROUP BY product_id
HAVING max(pinalty) > 30000;
-- Penggunaan Fungsi MIN pada Having
SELECT product_id, min(total_price) total
FROM invoice
GROUP BY product_id;
SELECT product_id, min(total_price) total
FROM invoice
GROUP BY product_id
HAVING min(total_price) < 500000;
SELECT product_id, min(pinalty) total
FROM invoice
GROUP BY product_id
HAVING min(pinalty) < 50000;
-- Penggunaan Fungsi AVG di Having
SELECT product_id, avg(total_price) total
FROM invoice
GROUP BY product_id;
SELECT product_id, avg(total_price) total
FROM invoice
GROUP BY product_id
HAVING min(total_price) > 100000;
SELECT product_id, avg(pinalty) total
FROM invoice
GROUP BY product_id
HAVING avg(pinalty) > 30000;
-- Mini Quiz
SELECT product_id, AVG(pinalty), COUNT(customer_id) total
FROM invoice
GROUP BY product_id
HAVING COUNT(customer_id) > 20;

