-- [Chapter - 3]
-- Pemanfaatan Operator Logika dalam Perintah Where
SELECT DISTINCT *
FROM 
  data_retail
WHERE 
  Product = 'Jaket' AND Average_Transaction_Amount >= 1000000;

-- Pemanfaatan Operator Logika dalam Konstruksi Case When
SELECT DISTINCT
Customer_ID,
Product,
Average_Transaction,
Count_Transaction,
CASE
	WHEN Average_Transaction > 2000000 AND Count_Transaction > 30 THEN 'Platinum Member'
    WHEN Average_Transaction BETWEEN 1000000 AND 2000000 AND Count_Transaction BETWEEN 20 AND 30 THEN 'Gold Member'
    WHEN Average_Transaction < 1000000 AND Count_Transaction < 20 THEN 'Silver Member'
    	ELSE 'Other Membership' end as Membership
FROM 
  summary_transaction;

-- Praktikum
SELECT DISTINCT
Customer_ID,
Product,
Average_transaction,
Count_Transaction,
CASE
	WHEN Average_transaction < 1000000 then '4-5x Email dalam seminggu'
    WHEN Average_transaction > 1000000 then '1-2x Email dalam seminggu'
END AS frekuensi_email
FROM 
  summary_transaction;

-- Perintah Where dan Logika And
SELECT DISTINCT
customer_id
FROM 
  summary_transaction
WHERE 
  Average_transaction < 1000000 and product =  'Sepatu';

-- Menyiapkan Report Penjualan
SELECT DISTINCT
product produk,
avg(average_transaction) 'Jumlah transaksi (Rupiah)',
sum(count_transaction) 'Barang terjual'
FROM 
  summary_transaction
GROUP BY 
  product;

-- [Chapter - 4]
-- Tugas Pertamaku
SELECT DISTINCT
	Customer_ID
FROM 
  data_retail_undian
WHERE 
  Unik_produk >= 3 AND Rata_rata_transaksi > 1500000;

-- Tugas Keduaku
SELECT DISTINCT
	Customer_ID
FROM 
  data_retail_undian
WHERE NOT 
  (Unik_produk >= 3 and Rata_rata_transaksi >= 1500000);
