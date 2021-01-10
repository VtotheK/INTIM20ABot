DELIMITER $;
/*DROP PROCEDURE IF EXISTS Leaderboard_Upd;
*/

CREATE PROCEDURE leaderboard_upd(
	in 	arg_userid bigint,
		arg_username varchar(100)
)

BEGIN
DECLARE var_userid bigint DEFAULT NULL;
CALL users_set(arg_userid, arg_username);


SELECT userid INTO var_userid FROM leaderboard WHERE arg_userid = userid LIMIT 1;

IF var_userid is NULL
THEN
	INSERT INTO leaderboard (userid,postcount,lastpost)
    VALUES (arg_userid, 1, NOW());
ELSE
	UPDATE leaderboard SET postcount = postcount + 1, lastpost= now() WHERE userid = var_userid;
END IF; 
END$;

DELIMITER ;
