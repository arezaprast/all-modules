SELECT tanggal_catat, REGEXP_REPLACE(tanggal_catat, '([0-9]{2})-([0-9]{2})-([0-9]{4})', '\\2/\\1/\\3') AS tanggal_pencatatan
FROM dqlabregex
