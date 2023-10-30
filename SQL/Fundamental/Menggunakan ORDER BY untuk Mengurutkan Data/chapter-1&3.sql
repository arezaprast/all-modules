-- [Chapter - 1]
-- Melakukan Pengurutan Data
SELECT DISTINCT
	Customer_ID, 
  COUNT(DISTINCT Product) jenis_barang,
  avg(Average_Transaction_Amount) rata_rata_transaksi,
  sum(Count_Transaction) total_transaksi
FROM 
  data_retail
GROUP BY 1
ORDER by 4 DESC;

-- Praktikum 1
SELECT DISTINCT
    Customer_ID, 
    sum(Count_Transaction) total_transaksi
FROM 
  data_retail
GROUP BY 1
ORDER BY 2 DESC;

-- Praktikum 2
SELECT DISTINCT
    Customer_ID, 
    sum(Count_Transaction) total_transaksi
FROM 
  data_retail
GROUP BY 1
ORDER BY 2 ASC;

-- Praktikum 3
SELECT DISTINCT
    Product, 
    SUM(Count_Transaction) total_transaksi
FROM data_retail
GROUP BY 1
ORDER BY 2 DESC;

-- [Chapter - 3]
-- Praktikum
SELECT
	Customer_ID,
  Product,
  SUM(Count_Transaction) total_pembelian_produk
FROM
	data_retail
GROUP BY
	Customer_ID, Product
ORDER BY 1, 3 DESC;
