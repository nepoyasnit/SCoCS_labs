from controller import Controller
from constants import JSON_DATA_TYPE
import supportive

serializer = Controller(JSON_DATA_TYPE).serializer

class Counter:
    value: int
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print('ALL employees amount: %d' % Employee.emp_count)

    def display_employee(self):
        print('Name: {}. Salary: {}'.format(self.name, self.salary))

f = serializer.loads(serializer.dumps(Counter))
a = f()
a.inc()
