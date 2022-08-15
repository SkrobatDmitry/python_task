CREATE TABLE students
(
    id          BIGINT          NOT NULL,
    name        VARCHAR(255)    NOT NULL,
    room        BIGINT          NOT NULL,
    sex         VARCHAR(1)      NOT NULL,
    birthday    DATE            NOT NULL,

    CONSTRAINT pk_students PRIMARY KEY (id),
    FOREIGN KEY fk_students_rooms (room) REFERENCES rooms (id)
);