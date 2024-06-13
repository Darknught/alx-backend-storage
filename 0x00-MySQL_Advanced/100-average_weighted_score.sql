-- This stored procedure computes and stores the average weighted score for a student.
-- It takes one input parameter, user_id, which is the ID of the user whose average weighted score will be computed.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare local variables
    DECLARE total_weighted_score FLOAT;
    DECLARE total_projects INT;
    DECLARE avg_weighted_score FLOAT;

    -- Calculate the total weighted score for the user
    SELECT SUM(score) INTO total_weighted_score
    FROM corrections
    WHERE user_id = ComputeAverageWeightedScoreForUser.user_id;

    -- Calculate the total weight for the user
    SELECT COUNT(DISTINCT project_id) INTO total_projects
    FROM corrections
    WHERE user_id = ComputeAverageWeightedScoreForUser.user_id;

    -- Calculate the average weighted score
    SET avg_weighted_score = total_weighted_score / total_projects;

    -- Update the average_score column in the users table for the given user_id
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = ComputeAverageWeightedScoreForUser.user_id;
END$$
DELIMITER ;
