-- [Chapter - 1]
-- Melakukan Pengurutan Data
SELECT DISTINCT
	Customer_ID,
	COUNT(DISTINCT Product) jenis_barang,
	AVG(Average_Transaction_Amount) rata_rata_transaksi,
	SUM(Count_Transaction) total_transaksi
FROM 
	data_retail
GROUP BY 1
ORDER by 4 DESC;

-- Praktikum 1
SELECT DISTINCT
	Customer_ID,
	SUM(Count_Transaction) total_transaksi
FROM 
	data_retail
GROUP BY 1
ORDER BY 2 DESC;

-- Praktikum 2
SELECT DISTINCT 
	Customer_ID, 
	SUM(Count_Transaction) total_transaksi
FROM 
	data_retail
GROUP BY 1
ORDER BY 2 ASC;

-- Praktikum 3
SELECT DISTINCT
	Product, 
	SUM(Count_Transaction) total_transaksi
FROM
	data_retail
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

-- [Chapter - 4]
-- Penggunaan ORDER BY dengan Fungsi Bulan
SELECT
	EXTRACT(YEAR_MONTH from (from_unixtime(Last_Transaction/1000))) month_transaction,
	Customer_ID,
	Product,
	SUM(Count_Transaction) total_pembelian_produk
FROM
	data_retail
GROUP BY 1,2,3
ORDER BY 1 DESC;

-- Praktikum
SELECT
	EXTRACT(YEAR_MONTH from (from_unixtime(Last_Transaction/1000))) month_transaction,
	Customer_ID,
	Product,
	SUM(Count_Transaction) total_pembelian_produk
FROM
	data_retail
GROUP BY 1,2,3
ORDER BY 1 DESC;

-- [Chapter - 5]
-- Mendapatkan 3 Penjualan Tertinggi
SELECT 
	EXTRACT(YEAR_MONTH FROM (from_unixtime(Last_Transaction/1000))) year_month_transaction,
   	SUM(Count_Transaction) total_pembelian_produk
FROM
	data_retail
WHERE 
	Product = 'Sepatu' AND EXTRACT(YEAR from (from_unixtime(Last_Transaction/1000))) in (2018,2019)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3;

-- Mendapatkan 3 Penjualan Terendah
SELECT 
	EXTRACT(YEAR_MONTH FROM (from_unixtime(Last_Transaction/1000))) year_month_transaction,
   	sum(Count_Transaction) total_pembelian_produk
FROM
	data_retail
WHERE 
	Product = 'Sepatu' AND EXTRACT(YEAR from (from_unixtime(Last_Transaction/1000))) in (2018,2019)
GROUP BY 1
ORDER BY 2 ASC
LIMIT 3;
