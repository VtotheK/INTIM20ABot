CREATE TABLE leaderboard (
      userid bigint NOT NULL,
      postcount int DEFAULT NULL,
      lastpost datetime DEFAULT NULL,
      FOREIGN KEY (userid) REFERENCES users(userid))
