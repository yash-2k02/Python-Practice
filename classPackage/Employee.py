from classPackage import Person
class Employee:
    def __init__(self, person_obj, emp_id):
        self.person = person_obj
        self.emp_id = emp_id

    def show_details(self):
        print(f"Name: {self.person.name}, Age: {self.person.age}, ID: {self.emp_id}")


def main():
    p1 = Person("Yash", 23)

    e1 = Employee(p1, "101")
    e1.show_details()


if __name__ == "__main__":
    main()


# main()
