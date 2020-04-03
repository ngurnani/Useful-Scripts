import sys

print(sys.executable)
print(sys.version)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


for num in [1, 2, 3]:
    print(num)

emp_1 = Employee("John", "Smith")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
