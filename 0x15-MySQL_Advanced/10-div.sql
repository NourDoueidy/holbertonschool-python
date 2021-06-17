-- Safe divide
-- Create a function SafeDiv that divides the first by the second number or returns 0 if the second number is equal to 0.
CREATE FUNCTION safeDiv (a INT, b INT)
RETURN (IF (b = 0, 0, a / b));
