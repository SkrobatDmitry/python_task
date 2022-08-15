SELECT rooms.name FROM rooms
INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.name
ORDER BY TIMESTAMPDIFF(DAY, MIN(birthday), MAX(birthday)) DESC
LIMIT 5;