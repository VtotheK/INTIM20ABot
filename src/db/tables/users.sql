CREATE TABLE users (
      userid bigint NOT NULL,
      username varchar(100) NOT NULL,
      changetimestamp datetime DEFAULT NULL,
      PRIMARY KEY (userid))
