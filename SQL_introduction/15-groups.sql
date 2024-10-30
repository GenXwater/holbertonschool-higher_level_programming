-- select score by groupe
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;