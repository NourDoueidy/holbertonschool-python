-- Overall weighted score
-- Create a procedure ComputeOverallWeightedScoreForUser that computes and store the overall weighted score for a student.
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeOverallWeightedScoreForUser;
CREATE PROCEDURE ComputeOverallWeightedScoreForUser (IN user_id INT)
BEGIN
    UPDATE users set overall_score = (SELECT
    SUM(corrections.score * projects.weight)
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    where corrections.user_id = user_id)
    where users.id = user_id;
END $$
DELIMITER ;
