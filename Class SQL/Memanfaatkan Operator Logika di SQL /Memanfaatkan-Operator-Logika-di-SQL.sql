--Mengenal Data Boolean Dalam SQL
SELECT DISTINCT customer_ID, product, average_transaction, average_transaction >= 1000000 AS is_eligible FROM summary_transaction;

--Pengenalan Operator Logika dalam SQL
--Logika AND
SELECT customer_ID, product, average_transaction_amount, product = 'Jaket' AND average_transaction_amount >= 1000000 AS loyal_buyer_jaket
FROM data_retail
WHERE product = 'Jaket';

--Logika OR
SELECT customer_id, product, average_transaction_amount, product = 'Jaket' OR product = 'Baju' AS buyer_fashion
FROM data_retail;

--Logika NOT
SELECT * FROM data_retail WHERE NOT product = 'Jaket';

--Logika XOR
SELECT customer_id, product, average_transaction_amount, product = 'Jaket' XOR average_transaction_amount > 1000000 AS logika_xor
FROM data_retail;

--Pemanfaatan Operator Logika dalam SQL
--Pemanfaatan Operator Logika dalam Perintah Where
SELECT DISTINCT * FROM data_retail WHERE Product = 'Jaket' AND Average_Transaction_Amount >= 1000000;

--Pemanfaatan Operator Logika dalam Konstruksi Case When
SELECT DISTINCT customer_ID, product, average_transaction, count_transaction,
CASE
WHEN Average_Transaction > 2000000 AND Count_Transaction > 30 THEN 'Platinum Member'
WHEN Average_Transaction BETWEEN 1000000 AND 2000000 AND Count_Transaction BETWEEN 20 AND 30 THEN 'Gold Member'
WHEN Average_Transaction < 1000000 AND Count_Transaction < 20 THEN 'Silver Member'
ELSE 'Other Membership' end as Membership
FROM summary_transaction;

--Praktikum
SELECT DISTINCT customer_ID, product, average_transaction, count_transaction,
CASE
WHEN Average_transaction < 1000000 then '4-5x Email dalam seminggu'
WHEN Average_transaction > 1000000 then '1-2x Email dalam seminggu'
END AS frekuensi_email
FROM summary_transaction;

--Perintah Where dan Logika And
SELECT DISTINCT customer_id FROM summary_transaction WHERE Average_transaction < 1000000 and product =  'Sepatu';

--Menyiapkan Report Penjualan
SELECT DISTINCT product AS produk, AVG(average_transaction) AS 'Jumlah transaksi (Rupiah)', SUM(count_transaction) AS 'Barang terjual'
FROM summary_transaction
GROUP BY product;

--Mini Project
--Tugas Pertamaku
SELECT DISTINCT customer_ID FROM data_retail_undian WHERE Unik_produk >= 3 AND Rata_rata_transaksi > 1500000;

--Tugas Keduaku
SELECT DISTINCT customer_ID FROM data_retail_undian WHERE NOT (Unik_produk >= 3 and Rata_rata_transaksi >= 1500000);
