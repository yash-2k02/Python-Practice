# MySQL CRUD Operations with Python

This branch demonstrates **CRUD operations** in MySQL using the `mysql-connector-python` library.

---

## Project Files
- **CRUD-connector.py** → Main Python script containing database setup and CRUD functions.  
- **requirements.txt** → Python dependencies list.   

---

## Features
- Connects to MySQL database using `mysql.connector`.
- Creates database `db_crud` if it does not exist.
- Creates a table `tblemployees1` with columns:
  - `empid` (INT)
  - `empname` (VARCHAR)
  - `deptid` (INT)
- Provides functions to:
  - `insert_employee(empid, ename, deptid)` → Insert a new employee.
  - `update_employee(id, name, deptid)` → Update employee details.
  - `view_all_employees()` → Fetch and display all employees.
  - `view_single_employee(id)` → Fetch a single employee by ID.
  - `delete_employee(id)` → Delete an employee by ID.

---
