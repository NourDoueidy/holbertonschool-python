-- Overall score
-- Create procedure to compute overall score
DELIMITER $$

CREATE PROCEDURE ComputeOverallScoreForUser (IN user_id INT)
BEGIN
      UPDATE users
      SET overall_score = (SELECT SUM(score) FROM corrections WHERE corrections.user_id = user_id)
      WHERE id = user_id;
    
END $$

DELIMITER ;
