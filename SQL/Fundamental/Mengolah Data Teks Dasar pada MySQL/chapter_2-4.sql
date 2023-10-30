-- [Chapter - 2]
-- Membaca Data
SELECT * FROM dqlabdatateks;

-- Latihan 1
SELECT LOCATE('|||', isi) as posisi_1
FROM dqlabdatateks;

-- Latihan 2
SELECT LOCATE('|||', isi, LOCATE('|||',isi) + 1) as posisi_2
FROM dqlabdatateks;

-- Latihan 3
SELECT LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) as posisi_3
FROM dqlabdatateks;

-- Latihan 4
SELECT LEFT(isi, LOCATE('|||', isi) -1) as Nama
FROM dqlabdatateks;

-- Latihan 5
SELECT SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 3) as KotaLahir
FROM dqlabdatateks;

-- Latihan 6
SELECT SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3) as TanggalLahir
FROM dqlabdatateks;

-- Latihan 7
SELECT RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 3 + 1) as Propinsi
FROM dqlabdatateks;

-- [Chapter - 3]
-- Latihan 1
SELECT CONCAT_WS(' - ',
SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 3),
RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 3 + 1)) AS TempatLahir
FROM dqlabdatateks;

-- Latihan 2
SELECT LEFT(
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 2) AS DD
FROM dqlabdatateks;

-- Latihan 3
SELECT RIGHT(
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4) AS YYYY
FROM dqlabdatateks;

-- Latihan 4
SELECT SUBSTR(
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 
4, 
LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) AS Bulan
FROM dqlabdatateks;

-- Latihan 5
SELECT CASE
WHEN
  SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Januari' THEN '01'
WHEN
SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Februari'
THEN '02'
ELSE '00'
END AS MM 
FROM dqlabdatateks;

-- [Chapter - 4]
-- Mini Project - Bagian Pertama
SELECT 
LEFT(isi, LOCATE('|||', isi) - 1) as Nama,
SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 3) as KotaLahir,
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3) as TanggalLahir,
RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 3 + 1) as Propinsi
FROM dqlabdatateks;

-- Mini Project - Bagian Kedua
SELECT 
LEFT(isi, LOCATE('|||', isi) - 1) as Nama, 
CONCAT_WS(' - ', SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 3),
RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 3 + 1)) AS TempatLahir,
CONCAT_WS('-', LEFT(
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 2),
CASE
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Januari' THEN '01'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Februari' THEN '02'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Maret' THEN '03'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'April' THEN '04'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Mei' THEN '05'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Juni' THEN '06'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Juli' THEN '07'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Agustus' THEN '08'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'September' THEN '09'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Oktober' THEN '10'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'November' THEN '11'
WHEN SUBSTR(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4, LENGTH(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3)) - 8) = 'Desember' THEN '12'
ELSE '00'
END, 
RIGHT(SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3), 4)) as TanggalLahir
FROM dqlabdatateks;
