from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name: str, age: int, address: str,):
        self.name = name
        self.age = age
        self.address = address

    def Getname(self):
        return self.name

    @abstractmethod
    def SelectDataForPrint(self):
        pass

    def Print(self):
        print(self.SelectDataForPrint())

class Test(Student):
    def SelectDataForPrint(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

test = Test("Hoa", 22, "654 Lac Long Quan")

print(test.Getname())
test.Print()
