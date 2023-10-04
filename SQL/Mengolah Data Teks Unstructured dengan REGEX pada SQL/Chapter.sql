-- Chapter - 2
-- Mengenal Penggunaan Operator REGEXP pada MySQL
SELECT * FROM dqlabregex WHERE kota REGEXP 'ng$'
-- Praktikum 1
SELECT * FROM dqlabregex WHERE staf_pencatat REGEXP 'Sen.?ja'
-- Praktikum 2
SELECT * FROM dqlabregex WHERE jumlah_member REGEXP '[^0-9]+'

-- Chapter - 3
-- Tugas Praktek
SELECT * FROM dqlabregex WHERE REGEXP_LIKE(staf_pencatat, '^an')
-- Praktikum 3
SELECT * FROM dqlabregex WHERE REGEXP_LIKE ( staf_pencatat, 'sen.?ja', 'i')
-- Praktikum 4
SELECT * FROM dqlabregex WHERE REGEXP_LIKE( jumlah_member, '[^0-9]+', 'i')

-- Chapter - 4
-- Tugas Praktek
SELECT REGEXP_REPLACE(staf_pencatat, 'Sen.?ja', 'Senja') AS pencatat 
FROM dqlabregex
-- Praktikum 5
SELECT no_pencatatan, tanggal_catat, kota, REGEXP_REPLACE(jumlah_member, '[^0-9]+', '') AS jumlah_member, staf_pencatat
FROM dqlabregex
-- Praktikum 6
SELECT tanggal_catat, REGEXP_REPLACE(tanggal_catat, '([0-9]{2})-([0-9]{2})-([0-9]{4})', '([0-9]{2})/([0-9]{2})/([0-9]{4})') AS tanggal_pencatatan
FROM dqlabregex

-- Chapter - 6
-- Clean All Columns
SELECT 
  no_pencatatan,
  REGEXP_REPLACE(tanggal_catat, '([0-9]{2})-([0-9]{2})-([0-9]{4})')
  OR REGEXP_REPLACE(tanggal_catat, '([0-9]{2})-([0-9]{2})-([0-9]{4})', '$3-$2-$1')
  OR REGEXP_REPLACE(tanggal_catat, '([0-9]{2})/([0-9]{2})/([0-9]{4})', '$3-$1-$2')
END AS tanggal_catat,
kota,
REGEXP_REPLACE(jumlah_member, '[^0-9]', '') AS jumlah_member,
REGEXP_REPLACE(staf_pencatat, 'Sen.?ja','Senja') AS staf_pencatat
FROM dqlabregex;
-- Aggregasi
SELECT 
	SUM(REGEXP_REPLACE(jumlah_member, '[^0-9]', '')) AS total_member, 
	REGEXP_REPLACE(staf_pencatat, 'Sen.?ja', 'Senja') AS staf_pencatat 
FROM dqlabregex 
GROUP BY 2 ORDER BY 1;
