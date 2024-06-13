-- A SQL script that ranks country origins of bands, ordered by the number
-- of non-unique fans. Column must be origin and nb_fans
-- Create a view to rank country origins by the number of fans
CREATE VIEW country_rankings AS
SELECT
    origin,
    SUM(nb_fans) AS total_fans
FROM
    bands
GROUP BY
    origin
ORDER BY
    total_fans DESC;

-- Select from the view to get the rankings
SELECT
    origin,
    total_fans
FROM
    country_rankings;
