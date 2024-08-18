"""
Simple Person class using dataclasses.

Defines a Person with name, age, and job attributes.
Demonstrates dataclass usage for easy object creation and string representation.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    job: str


person = Person(name="Alice", age=30, job="Engineer")
print(person)
