-- A script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score DECIMAL(5,2)
)
BEGIN
    DECLARE p_project_id INT;

    -- Check if project exists, if not, insert it
    SELECT id INTO p_project_id FROM projects WHERE name = p_project_name;
    IF p_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET p_project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, p_project_id, p_score);
END //

DELIMITER ;
