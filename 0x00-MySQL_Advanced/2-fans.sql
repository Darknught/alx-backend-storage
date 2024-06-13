-- A SQL script that ranks country origins of bands, ordered by the number
-- of non-unique fans. Column must be origin and nb_fans
-- Create a view to rank country origins by the number of fans
USE holberton;

SELECT
  origin,
  SUM(fans) AS nb_fans
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC;
