-- Creates the table unique_id where id is unique
CREATE TABLE
    IF NOT EXISTS unique_id (
        `id` INT DEFAULT 1 UNIQUE,
        `name` VARCHAR(256)
    );
