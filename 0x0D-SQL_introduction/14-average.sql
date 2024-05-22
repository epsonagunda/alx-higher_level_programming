-- Script that computes the score average of all records in the table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
