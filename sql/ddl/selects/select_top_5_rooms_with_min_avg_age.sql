SELECT rooms.name FROM rooms
INNER JOIN students ON rooms.id = students.room
GROUP BY rooms.name
ORDER BY AVG(TIMESTAMPDIFF(YEAR, birthday, CURDATE()))
LIMIT 5;