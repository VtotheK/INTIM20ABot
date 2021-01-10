DELIMITER $;
/*
DROP PROCEDURE IF EXISTS users_set;
 */
CREATE PROCEDURE users_set(
	in arg_userid bigint,
	arg_username varchar(100)
)

BEGIN

	DECLARE var_userid bigint;
	DECLARE var_username varchar(100);

	SELECT userid INTO var_userid FROM users WHERE userid = arg_userid;

	IF var_userid is NULL THEN
		INSERT INTO users (userid,username,changetimestamp)
		VALUES (arg_userid,arg_username,now());
	ELSE
		SELECT username INTO var_username FROM users WHERE userid = var_userid LIMIT 1;
		IF arg_username <> var_username THEN
			UPDATE users SET username = arg_username ,changetimestamp = now() WHERE userid = var_userid;
		END IF;
	END IF;

END $;
DELIMITER ;
