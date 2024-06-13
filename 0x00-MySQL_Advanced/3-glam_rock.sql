-- A script that list all bands with Glam rock as their main style ranked by longevity
USE holberton;

-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT
  band_name,
  CASE
    WHEN formed IS NULL THEN 'Unknown'
    ELSE TIMESTAMPDIFF(YEAR, formed, 2022)
  END AS lifespan
FROM
  metal_bands
WHERE
  style = 'Glam rock'
ORDER BY
  lifespan DESC;
