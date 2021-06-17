-- Overall weighted score
-- Create a procedure ComputeOverallWeightedScoreForUser that computes and store the overall weighted score for a student.
CREATE PROCEDURE computeOverallWeightedScoreForUser (IN user_id INT)
UPDATE users set overall_score = (SELECT 
SUN(corrections.score * projects.weight)
FROM corrections
INNER JOIN projects
ON projects.id = corctions.project_id
WHERE corrections.user_id = user_id)
WHERE users.id = user_id;
