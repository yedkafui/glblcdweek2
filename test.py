# def is_even(number):
#       if  not (number % 2) == 0:
#              return True
#       else:
#              return False
      
# number = int(input('Enter Number: '))
# numbers = [1,56,234,87,4,76,24,69,90,135]
# is_even(number)

# print(list(filter(is_even,numbers)))

# numbers = [1,56,234,87,4,76,24,69,90,135]
# # even_num = lambda y: y % 2 == 0
# # print(f"{'Even numbers:'} {list(filter(even_num,numbers))}")

# odd_num = lambda y:y % 2 != 0
# print(f"{'Odd numbers:'} {list(filter(odd_num,numbers))}")
# print(list((filter(odd_num,numbers))))

# Question 4
from functools import reduce
# total = reduce(lambda item, running_total: item + ' '+ running_total, ["hi", "hos", 'df', 'e', 'df'])
# print(total)
# def join_strings(words, b ):
#     result = words +" "+ b 
#     print(result)
#     return result

# words = ['Joshua','is','good']

# reduce(join_strings,words)

# Question 5
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# print(words)

# new = [len(words) for word in words if word != 'the']
# print(new)
# numbers = [34.6, -203.4,44.9,68.3,-12.2,44.6,12.7]

# positiveNum = [num for num in numbers if num >0 ]
# print(positiveNum)

# words = ['hello','my','name','is','Sam']
# wordLen = [(word.upper(),len(word)) for word in words]
# print(wordLen)

#Modules
#Classes

# class Person:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def speak():
#         print("hello")

#     def walk():
#         print('Walking away')

#     def get_name(self):
#         return self.name
    
#     def get_age(self,age):
#         return self.age


#     def myfunction(self):
#         print("Hello " + self.name) 

# class Student(Person):
#     def __init__(self,courses):  
#         super().__init__(name,age)      
#         self.courses = courses

#     def get_courses(courses):
#         return courses

#     def speak():
#         print("I'm so tired!")

# Student.speak()
# per1 = Person("Joshua",8)
# per1.myfunction()