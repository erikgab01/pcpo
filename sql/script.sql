CREATE TABLE queries (
	id integer PRIMARY KEY autoincrement,
	processed datetime
);

CREATE TABLE goodweather_goodday (
	id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	date1 varchar(40) NOT NULL, 
	weather varchar(20) NOT NULL, 
	date_millisecs real NOT NULL, 
	temp_min real NULL, 
	temp_max real NULL, 
	feels_like_day real NULL, 
	pressure integer NULL, 
	humidity integer NULL, 
	dew_point real NULL, 
	wind_speed real NULL, 
	uvi real NULL, 
	pop integer NULL,
	query1 integer NOT NULL,
	CONSTRAINT query_num
	FOREIGN KEY (query1)
	REFERENCES queries(id)
);

CREATE TABLE auth_user (
	id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	password varchar(128) NOT NULL, 
	username varchar(150) NOT NULL UNIQUE, 
	email varchar(254) NOT NULL,
	last_login datetime NULL, 
	is_superuser bool NOT NULL,
	date_joined datetime NOT NULL
);