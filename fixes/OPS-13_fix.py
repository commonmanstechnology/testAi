```sql
SELECT
    d.name,
    AVG(e.salary) AS average_salary
FROM
    departments d
JOIN
    employees e ON d.id = e.department_id
GROUP BY
    d.name
ORDER BY
    average_salary DESC
LIMIT 5;
```