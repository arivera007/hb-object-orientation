"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction: Get all the behavior in 
   Encapsulation:
   Polimorphism:

2. What is a class?
   
   
3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
   
   def __init__(first_name, last_name, address):
      self.first_name = first_name
      self.last_name = last_name
      self.address = address
      
   
class Question(object):
   
   def __init__(question, correct_answer):
      self.question = question
      self.question = question
      
      
class Exam(object):
   
   def __init__(name):
      self.name = name
      self.questions = []
      


