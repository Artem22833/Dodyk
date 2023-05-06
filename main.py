# class Humen:
#     height = 180
#     
# class Student(Humen):
#     pass
# 
# class Workr(Humen):
#     pass
# 
# s1 = Student()
# w1 =

# class Humen:
#     def __init__(self):
#         print("Hello")
#         
# class Student

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# a = Class2


# class Animal:
# #         def __init__(self, name, age, species):
# #             self.name = name
# #             self.age = age
# #             self.species = species
# #
# #         def make_sound(self):
# #             print("The animal makes a sound!")
# #
# # class Dog(Animal):
# #         def __init__(self, name, age):
# #             super().__init__(name, age, species="Dog")
# #
# #         def make_sound(self):
# #             print("Woof")
# #
# # class Cat(Animal):
# #         def __init__(self, name, age):
# #             super().__init__(name, age, species="Cat")
# #
# #         def make_sound(self):
# #             print("Meow")
# #
# # cat = Cat("Fluffy", 2)
# # dog = Dog("Buddy", 4)
# #
# # print(cat.name)
# # print(cat.species)
# #
# # print(dog.name)
# # print(dog.species)
# # cat.make_sound()
# # dog.make_sound()
#
# class Humen:
#     def __init__(self, name, age, species):
#             self.name = name
#             self.age = age
#             self.species = species
# class Student(Humen):
#     def __init__(self, name, age, species):
#         super().__init__(name, age, species)
#
# class Teacher(Humen):
#     def __init__(self, name, age, subject, species):
#         super().__init__(name, age, species)
#         self.subject = subject
#
# class Engineer(Humen):
#     def __init__(self, name, age, compani, species):
#         super().__init__(name, age, species)
#         self.compani = compani
#
# s1 = Student('Igor', 16, 'Men')
# print(s1.name)
# print(s1.age)
# print(s1.species)
#
# t1 = Teacher('Mark', 60, 'Men', 'Math')
# print(t1.name)
# print(t1.age)
# print(t1.species)
# print(t1.subject)
#
# e1 = Engineer('Ford', 21, 'Man', 'Tesla')
# print(e1.name)
# print(e1.age)
# print(e1.species)
# print(e1.compani)

# class Car:
#     def __init__(self, mark, year):
#         self.mark = mark
#         self.year = year
# class ElectricCar(Car):
#     def __init__(self, batari, probig):
#         self.batari = batari
#         self.probig = probig
# class Tesla(ElectricCar):
#     def __init__(self,):