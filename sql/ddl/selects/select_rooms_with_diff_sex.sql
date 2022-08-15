SELECT rooms.name FROM rooms
WHERE EXISTS (
	SELECT r.id, students.sex FROM rooms AS r
    INNER JOIN students ON r.id = students.room
    WHERE rooms.id = r.id AND students.sex = 'M'
) AND EXISTS (
	SELECT r.id, students.sex FROM rooms AS r
    INNER JOIN students ON r.id = students.room
    WHERE rooms.id = r.id AND students.sex = 'F'
);