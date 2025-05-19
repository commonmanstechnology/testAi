```python
import sqlite3
from typing import Tuple, Optional

def get_highest_paid_employee(db_path: str) -> Optional[Tuple[int, str, float]]:
    """Queries a SQLite database for the highest-paid employee.

    Args:
        db_path: Path to the SQLite database file.  Must contain a table named 'employees' with columns 'id' (INTEGER), 'name' (TEXT), and 'salary' (REAL).

    Returns:
        A tuple containing (employee_id, employee_name, salary) of the highest-paid employee, or None if the table is empty or there's an error.
    """
    if not db_path or not isinstance(db_path, str):
        raise ValueError("Invalid database path provided.")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, salary FROM employees ORDER BY salary DESC LIMIT 1")
        result = cursor.fetchone()

        conn.close()
        return result

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

```