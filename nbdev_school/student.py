# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/student.ipynb.

# %% auto 0
__all__ = ['Student']

# %% ../nbs/student.ipynb 4
class Student:
    def __init__(self, 
                name: str, # name of the student
                age: int): # age of the student
        self.name = name
        self.age = age

    def introduce(self) -> None:
        print(f"Hello, I'm {self.name} and {self.age}-years old.")
