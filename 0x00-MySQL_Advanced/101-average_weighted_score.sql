DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE weighted_avg FLOAT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate weighted average score for the current user
        SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Update user's average_score
        UPDATE users
        SET average_score = COALESCE(weighted_avg, 0)
        WHERE id = user_id;
    END LOOP;

    CLOSE cur;
END;//

DELIMITER ;
