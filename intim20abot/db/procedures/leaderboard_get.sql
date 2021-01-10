DELIMITER $$;
/*drop procedure if exists leaderboard_get;
*/
CREATE PROCEDURE leaderboard_get(
	IN 	arg_userid bigint,
		arg_topusers int
)

leaderboard_get:BEGIN

IF arg_topusers NOT BETWEEN 1 AND 10
THEN 
	LEAVE leaderboard_get;
END IF;

IF arg_userid IS NULL
THEN
	SELECT username, postcount FROM leaderboard l
    	JOIN users u on u.userid = l.userid
    	ORDER BY postcount DESC
    	LIMIT arg_topusers;
ELSE
	SELECT username , postcount FROM leaderboard l
    	JOIN Users u on u.userid = l.userid
    	WHERE u.userid = arg_userid
    	LIMIT 1;
END IF;
END$$;

DELIMITER ;
