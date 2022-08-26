DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS schedule;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    instagram_nickname VARCHAR,
    created_at TIMESTAMP NOT NULL,
    telegram_id INTEGER NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR,
    username VARCHAR
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    booking_datetime TIMESTAMP NOT NULL,
    service VARCHAR NOT NULL,
    price NUMERIC(5, 2) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE schedule (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    time JSON NOT NULL
);