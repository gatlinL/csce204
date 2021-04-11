# Author: Gatlin Lawson
from person import Person

"""
friend1 = Person("Zach", "Young", "803-427-5533")
friend1.display()

friend2 = Person("Parker", "Howard", "764-456-9872")
friend2.display()
"""

people = (
    Person("Zach", "Young", "803-427-5533"),
    Person("Tammy", "Lawson", "843-386-5483"),
    Person("Parker", "Howard", "764-456-9872"),
    Person("Brad", "Lawson", "678-348-1287")
)

for person in people:
    person.display()