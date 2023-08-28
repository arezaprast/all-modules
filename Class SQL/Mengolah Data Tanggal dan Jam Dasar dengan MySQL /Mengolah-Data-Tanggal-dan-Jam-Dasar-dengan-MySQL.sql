--Latihan 1
SELECT * FROM dqlab_retail;

--Latihan 2
SELECT *, (jumlah*harga) AS subtotal FROM dqlab_retail;

--Latihan 3
SELECT * FROM dqlab_retail WHERE tanggal BETWEEN '2020-04-01' AND '2020-04-30';

--Latihan 4
SELECT SUM(jumlah*harga) as total FROM dqlab_retail;

--Latihan 5
SELECT tanggal, SUM(jumlah*harga) as total FROM dqlab_retail GROUP BY tanggal;

--Latihan 6
SELECT YEAR(tanggal) as tahun, SUM(jumlah*harga) as total FROM dqlab_retail GROUP BY YEAR(tanggal);

--Latihan 7
SELECT YEAR(tanggal) as tahun, MONTH(tanggal) as bulan, SUM(jumlah*harga) as total FROM dqlab_retail GROUP BY YEAR(tanggal), MONTH(tanggal);

--Latihan 8
SELECT kode_produk, nama_produk, SUM(jumlah*harga) as total FROM dqlab_retail GROUP BY kode_produk,nama_produk;

--Latihan 9
SELECT tanggal, kode_produk, nama_produk, SUM(jumlah) AS totaljumlah, harga, SUM(jumlah*harga) AS total 
FROM dqlab_retail 
GROUP BY tanggal,kode_produk,nama_produk,harga;

--Latihan 10
SELECT YEAR(tanggal) AS tahun, kode_produk, nama_produk, SUM(jumlah) AS totaljumlah, harga, SUM(jumlah*harga) AS total
FROM dqlab_retail
GROUP BY YEAR(tanggal),kode_produk, nama_produk, harga;

--Latihan 11
SELECT YEAR(tanggal) AS tahun, MONTH(tanggal) AS bulan, kode_produk, nama_produk, SUM(jumlah) AS totaljumlah, harga, SUM(jumlah*harga) AS total
FROM dqlab_retail
GROUP BY YEAR(tanggal), MONTH(tanggal),kode_produk, nama_produk, harga;
