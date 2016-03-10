CREATE TABLE players(
	player_id 			INT(8) NOT NULL AUTO_INCREMENT,
	player_name 		VARCHAR(255) NOT NULL,
	is_current 			BIT NOT NULL,
	GP					INT(8),
	AB					INT(8),
	PA					INT(8),
	K					INT(8),
	BB					INT(8),
	1B					INT(8),
	2B					INT(8),
	3B					INT(8),
	HR					INT(8),
	HBP					INT(8),
	SB					INT(8),
	RBI					INT(8),
	R					INT(8),
	SAC					INT(8),
	GDIP				INT(8),
	A					INT(8),
	PO					INT(8),
	E					INT(8),
	TC					INT(8),
	SO					INT(8),
	W					INT(8),
	IP					INT(8),
	HA					INT(8),
	ER					INT(8),
	RA					INT(8),
	PI					INT(8),
	WP					INT(8),
	W					INT(8),
	L					INT(8),
	G					INT(8),
	GS					INT(8),
	SV					INT(8),
	HOLD				INT(8),
	PRIMARY KEY (player_id),
) TYPE = INNODB;

CREATE TABLE Game_Info(
	game_id				INT(8) NOT NULL AUTO_INCREMENT,
	opponent			VARCHAR(255) NOT NULL,
	Game_Date			DATETIME NOTNULL,
	is_home				BIT NOT NULL,
	is_win				BIT NOT NULL,
	score				INT(8),
	opponent_score		INT(8),
	hits				INT(8),
	errors				INT(8),
	opponent_errors		INT(8),
	PRIMARY KEY(game_id),
) TYPE = INNODB;

CREATE TABLE innings(
	inn_id				INT(8) NOT NULL AUTO_INCREMENT,
	inn1				INT(8),
	inn2				INT(8),
	game 				INT(8) NOT NULL,
	PRIMARY KEY(inn_id),
) TYPE = INNODB;

CREATE TABLE articles(
	article_id			INT(8) NOT NULL AUTO_INCREMENT,
	title				VARCHAR(255) NOT NULL,
	article_date		DATETIME,
	body				VARCHAR(255) NOT NULL,
	PRIMARY KEY(article_id),
) TYPE = INNODB;

CREATE TABLE images(
	image_id			INT(8) NOT NULL AUTO_INCREMENT,
	title				VARCHAR(255),
	image_date			DATETIME,
	article 			INT(8),
	PRIMARY KEY(image_id),
) TYPE = INNODB;

ALTER TABLE innings ADD FOREIGN KEY(game) REFERENCES Game_Info(game_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE images ADD FOREIGN KEY(article) REFERENCES articles(article_id) ON DELETE CASCADE ON UPDATE CASCADE;
