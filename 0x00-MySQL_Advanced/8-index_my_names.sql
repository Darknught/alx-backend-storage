-- script that creates ab index idx_name_first on the table names and the first letter of name
-- Assuming the 'names.sql.zip' file has been imported and the 'names' table exists

-- Create the index on the first letter of the 'name' column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
