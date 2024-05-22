-- Script that computes the score average of all records in the table
-- Execute: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
