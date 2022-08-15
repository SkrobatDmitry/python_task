SELECT rooms.name, COUNT(*) AS students_count FROM rooms
INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.name;