CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    instagram_nickname VARCHAR,
    created_at TIMESTAMP NOT NULL,
    telegram_id INTEGER NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT false,
    chat_id INTEGER NOT NULL
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    booking_datetime TIMESTAMP NOT NULL,
    service VARCHAR NOT NULL,
    price NUMERIC(5, 2) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);