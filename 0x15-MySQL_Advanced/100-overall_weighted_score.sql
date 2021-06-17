-- Overall weighted score
-- Create a procedure ComputeOverallWeightedScoreForUser that computes and store the overall weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeOverallWeightedScoreForUser(user_id INT)
BEGIN
    DECLARE sum_score FLOAT;
    SET sum_score = (SELECT SUM(score * weight)
                        FROM users AS U 
                        JOIN corrections as C ON U.id=C.user_id 
                        JOIN projects AS P ON C.project_id=P.id 
                        WHERE U.id=user_id);
    UPDATE users SET overall_score = sum_score WHERE id=user_id;
END
$$
DELIMITER ;
