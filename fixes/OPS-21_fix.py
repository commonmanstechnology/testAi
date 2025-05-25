```sql
SELECT e.id, e.name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE d.id = 101;
```