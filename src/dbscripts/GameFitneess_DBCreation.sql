PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: USERS
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    user_name     TEXT PRIMARY KEY,
	passsord	  TEXT NOT NULL,
    first_name    TEXT NOT NULL,
    last_name     TEXT NOT NULL,
    user_type     TEXT NOT NULL,
	email_address TEXT UNIQUE NOT NULL,
	height        REAL NOT NULL,
	weight		  REAL NOT NULL,
	gender 		  INTEGER NOT NULL,
	game_id       TEXT NOT NULL
);

-- Table: LEVELS
DROP TABLE IF EXISTS levels;

CREATE TABLE IF NOT EXISTS levels (
    level_id	 TEXT PRIMARY KEY,
	level_name   TEXT NOT NULL,
	level 

-- Table: GAMES
DROP TABLE IF EXISTS games;

CREATE TABLE IF NOT EXISTS games (
    game_id       TEXT PRIMARY KEY,
	game_name	  TEXT NOT NULL,
    description   TEXT,
    body_parts    TEXT NOT NULL
);

-- Table: INJURIES
DROP TABLE IF EXISTS injuries;

CREATE TABLE IF NOT EXISTS injuries (
    injury_id    TEXT, 
	injury_name  TEXT, 
	game_id	     TEXT,
    description  TEXT,
    body_part    TEXT NOT NULL
	PRIMARY_KEY (injury_id,game_id)
);

-- Table: EXERCISES
DROP TABLE IF EXISTS exercises;

CREATE TABLE IF NOT EXISTS exercises (
    exercise_id     TEXT PRIMARY_KEY, 
	body_category   TEXT, 
	weight_level_id	TEXT,
    description     TEXT,
    body_part       TEXT NOT NULL
);

-- Table: WEIGHT_LEVELS
DROP TABLE IF EXISTS weight_levels;

CREATE TABLE IF NOT EXISTS weight_levels (
    weight_level_id TEXT, 
	weights_percentage TEXT, 
	level_id        TEXT,
    description     TEXT,
    body_part    TEXT NOT NULL
	PRIMARY_KEY (weight_level_id,level_id)
);

PRAGMA foreign_keys = on;
