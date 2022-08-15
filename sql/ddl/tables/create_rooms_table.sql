CREATE TABLE rooms
(
    id      BIGINT          NOT NULL,
    name    VARCHAR(255)    NOT NULL,

    CONSTRAINT pk_rooms PRIMARY KEY (id)
);