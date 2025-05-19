```python
def find_high_salary_employees(employees):
    if not isinstance(employees, list):
        raise TypeError("Input must be a list of dictionaries.")
    for employee in employees:
        if not isinstance(employee, dict) or 'salary' not in employee or not isinstance(employee['salary'], (int, float)):
            raise ValueError("Invalid employee data. Each employee must be a dictionary with a numeric 'salary' key.")
    return [emp for emp in employees if emp['salary'] > 500]

```