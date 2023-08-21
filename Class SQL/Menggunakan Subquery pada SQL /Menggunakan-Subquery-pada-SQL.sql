--Subquery dalam klausa WHERE
#Menghitung customer yang membeli Sepatu dan Jaket
SELECT COUNT(DISTINCT customer_id) total_buyer_Sepatu_Jaket
FROM data_retail
WHERE product = 'Sepatu' 
AND customer_id IN (SELECT distinct Customer_ID FROM data_retail WHERE product = 'Jaket');
#Menghitung customer yang membeli Sepatu dan Baju
SELECT COUNT(DISTINCT customer_id) total_buyer_Sepatu_Baju
FROM data_retail
WHERE product = 'Sepatu' 
AND customer_id IN (SELECT distinct Customer_ID FROM data_retail WHERE product = 'Baju');
#Menghitung customer yang membeli Sepatu dan Tas
SELECT COUNT(DISTINCT customer_id) total_buyer_Sepatu_Tas
FROM data_retail
WHERE product = 'Sepatu' 
AND customer_id IN (SELECT DISTINCT customer_id FROM data_retail WHERE product = 'Tas');

--Subquery dalam klausa JOIN
SELECT a.Customer_ID, a.Transaksi_Sepatu, b.Transaksi_Jaket
FROM (SELECT customer_id, sum(count_transaction) transaksi_sepatu
      FROM data_retail
      WHERE product = 'Sepatu'
      GROUP BY 1) A
JOIN (SELECT Customer_ID, sum(Count_Transaction) transaksi_jaket
      FROM data_retail
      WHERE product = 'Jaket'
      GROUP BY 1) B ON a.Customer_ID = b.Customer_ID
ORDER BY 2 DESC,3 DESC;

--Mencari Rata-Rata Total Transaksi untuk Produk Sepatu
SELECT AVG(count_transaction) avg_transaksi FROM data_retail WHERE product = 'Sepatu';

--Subquery untuk menghasilkan nilai kolom pada konstruksi SELECT
SELECT customer_id, count_transaction, (SELECT AVG(count_transaction) FROM data_retail WHERE product = 'Sepatu') Avg_Transaction
FROM data_retail
WHERE product = 'Sepatu';

--Mini Project - Analisis penjualan DQ-Shop
SELECT 
A.Product, 
A.total_buyer, 
D.loyal_customer
FROM (
   SELECT Product, COUNT(DISTINCT Customer_ID) total_buyer
   FROM data_retail
   GROUP BY 1) A
JOIN (
   SELECT B.Product, COUNT(DISTINCT Customer_ID) loyal_customer
   FROM data_retail B
   JOIN (
    SELECT Product, AVG(Count_Transaction) AS Count_Transaction
    FROM data_retail 
    GROUP BY 1
   ) C ON C.Product = B.Product AND B.Count_Transaction > C.Count_Transaction
   GROUP BY 1
   ) D ON A.Product = D.Product;
