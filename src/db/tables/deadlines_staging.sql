CREATE TABLE deadlines_staging (
      id int NOT NULL AUTO_INCREMENT,
      module varchar(50) DEFAULT NULL,
      course varchar(50) DEFAULT NULL,
      title varchar(1000) DEFAULT NULL,
      summary varchar(1000) DEFAULT NULL,
      userid bigint DEFAULT NULL,
      deadline datetime NOT NULL,
      notifyfrom datetime NOT NULL,
      PRIMARY KEY (id),
      FOREIGN KEY (userid) REFERENCES users(userid))
