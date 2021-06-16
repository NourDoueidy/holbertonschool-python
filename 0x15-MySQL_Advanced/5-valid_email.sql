-- Valid email
-- Creat a trigger that Resets valid_email if the email is changed
CREATE TRIGGER res_email BEFORE INSERT ON users
FOR EACH ROW SET valid_email = NEW.email
