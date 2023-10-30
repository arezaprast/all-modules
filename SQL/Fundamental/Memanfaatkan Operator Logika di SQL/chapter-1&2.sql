-- [Chapter - 1] 
-- Praktikum
SELECT DISTINCT
	Customer_ID, Product,
  Average_transaction,
  Average_transaction >= 1000000 is_eligible
FROM 
  summary_transaction;

-- [Chapter - 2]
-- Logika AND
SELECT
	Customer_ID, Product, average_transaction_amount,
  product = 'Jaket' AND average_transaction_amount >= 1000000 loyal_buyer_jaket
FROM 
  data_retail
WHERE 
  product = 'Jaket';

-- Logika OR
SELECT 
     customer_id, 
     product, 
     average_transaction_amount,
     product = 'Jaket' OR product = 'Baju' buyer_fashion
FROM 
  data_retail;

-- Logika NOT
SELECT *
FROM 
  data_retail
WHERE NOT 
  product = 'Jaket';

-- Logika XOR
SELECT 
    customer_id,
    product,
    average_transaction_amount,
    product = 'Jaket' XOR average_transaction_amount > 1000000 logika_xor
FROM 
  data_retail;

-- Praktikum
-- Praktikum
-- Praktikum
-- Praktikum
