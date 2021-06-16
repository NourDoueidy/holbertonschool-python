-- Valid email
-- Creat a trigger that Resets valid_email if the email is changed
CREATE TRIGGER res_email BEFORE UPDATE ON users
FOR EACH ROW 
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
