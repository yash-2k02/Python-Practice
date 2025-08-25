import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass",
)
 

cur = db.cursor()

cur.execute("create database if not exists db_crud")
cur.execute("show databases")

for i in cur:
    print(i)

cur.execute("use db_crud")    

cur.execute("drop table if exists tblemployees1")


def create_table():
    cur.execute("""
            create table if not exists tblemployees1 (
                empid int,
                empname varchar(20),
                deptid int
            )
            """)

    cur.execute("show tables")

    for i in cur:
        print("Tables is: ",i)






# user accessible functions

def insert_employee(empid, ename, deptid):
    try:
        query = "insert into tblemployees1 values (%s, %s, %s)"
        cur.execute(query, (empid,ename,deptid))
    except mysql.connector.Error as e:
        print(f"Error occurred while inserting: ", e)
    

def update_employee(id, name, deptid):
    try:
        query = """update tblemployees1 
                    set empname = %s, deptid = %s
                    where empid = %s
                """
        cur.execute(query, (name, deptid, id))
    except mysql.connector.Error as e:
        print(f"Error occurred while updating employee: {e}")
    
    
def view_all_employees():
    try:
        cur.execute("select *from tblemployees1")
        for emp in cur:
            print(emp)
    except mysql.connector.Error as e:
        print(f"Error occurred while fetching employees: {e}")
  
      
def view_single_employee(id):
    try:
        query = "select *from tblemployees1 where empid = %s"
        cur.execute(query, (id,))
        for emp in cur:
            print(emp)
    except mysql.connector.Error as e:
        print(f"Error occurred while fetching employee by id: {e}")
        
        
def delete_employee(id):
    try:
        query = "delete from tblemployees1 where empid = %s"
        cur.execute(query, (id,))
        for emp in cur:
            print(emp)
    except mysql.connector.Error as e:
        print(f"Error occurred while deleting: {e}")
        

create_table()


insert_employee(1, "Alice", 101)
insert_employee(4, "David", 103)
insert_employee(9, "Irene", 102)
insert_employee(12,"Leo", 102)
insert_employee(14,"Noah", 103)
insert_employee(15,"Olivia", 101)
insert_employee(8, "Henry", 103)


print("All employees are:\n")
view_all_employees()

print("Employee by id 9 is: \n")
view_single_employee(9)

print("Update")
update_employee(12, "Oliver", 101)

print("After update")
view_all_employees()

print("Deleting")
delete_employee(8)

print("After delete")
view_all_employees()

db.commit()

cur.close()
db.close()
