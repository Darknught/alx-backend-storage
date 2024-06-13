-- A script that creates a stored procedure that computes abd store the average score of a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    -- Declare a variable to store the average score
    DECLARE v_average_score DECIMAL(5,2);

    -- Compute the average score for the given user_id
    SELECT AVG(score) INTO v_average_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = v_average_score
    WHERE id = p_user_id;
END //

DELIMITER ;
