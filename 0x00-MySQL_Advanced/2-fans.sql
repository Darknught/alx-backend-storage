-- A SQL script that ranks country origins of bands, ordered by the number
-- of non-unique fans. Column must be origin and nb_fans
-- Create a view to rank country origins by the number of fans
USE holberton;

SELECT
  origin,
  COUNT(*) AS nb_fans
FROM
  bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC;
