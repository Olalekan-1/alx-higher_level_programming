-- grouped average temaperatures by city

SELECT city, AVG(value) AS avg_temp
FROM temaperatures
GROUP BY city
ORDER BY avg_temp DESC;
