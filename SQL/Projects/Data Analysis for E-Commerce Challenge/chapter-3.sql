-- 10 Transaksi terbesar user 12476
SELECT seller_id, buyer_id, total AS nilai_transaksi, created_at AS tanggal_transaksi
FROM orders
WHERE buyer_id = 12476
ORDER BY 3 DESC
LIMIT 10;

-- Transaksi per bulan
SELECT EXTRACT(YEAR_MONTH FROM created_at) AS tahun_bulan, COUNT(1) AS jumlah_transaksi, sum(total) AS total_nilai_transaksi
FROM orders
WHERE created_at >= '2020-01-01'
GROUP BY 1
ORDER BY 1;

-- Pengguna dengan rata-rata transaksi terbesar di Januari 2020
SELECT buyer_id, COUNT(1) AS jumlah_transaksi, avg(total) AS avg_nilai_transaksi
FROM orders
WHERE created_at>='2020-01-01' AND created_at<'2020-02-01'
GROUP BY 1
HAVING COUNT(1)>= 2 
ORDER BY 3 DESC
LIMIT 10;

-- Transaksi besar di Desember 2019
SELECT nama_user AS nama_pembeli, total AS nilai_transaksi, created_at AS tanggal_transaksi
FROM orders
INNER JOIN users ON buyer_id = user_id
WHERE created_at>='2019-12-01' AND created_at<'2020-01-01'
AND total >= 20000000
ORDER BY 1;

-- Kategori Produk Terlaris di 2020
SELECT category, sum(quantity) AS total_quantity, sum(price) AS total_price
FROM orders
INNER JOIN order_details USING(order_id)
INNER JOIN products USING(product_id)
WHERE created_at>='2020-01-01'
AND delivery_at IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;
