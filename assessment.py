"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   Abstraction: Generalization of things, categorizing, abstract ideas. Like, here are all the animals. 
   Encapsulation: Hiding all the inner workings of an  object. Giving only the minimum necesary interface for user to operate such object.
   Polimorphism: When given an order of the same kind to different kinds of objects, an object provides its own unique behavior according to its nature.
   Inheritance: I would argue that inheritance is also a main advantage for design in object orientation. Though not mentioned in class as a pilar, it
               would be hard to have abstraccion without inheritance.

2. What is a class?
   A collection of members that share behaviors and attributes.
   
   
3. What is an instance attribute?
   When one of the members of a class, an instance, has an specific attribute that is not shared necessarily amongst the other members 
of the same class.

4. What is a method?
   It is a function that belongs to a class. Performs a certain behavior that will be shared amongs members of the same class.

5. What is an instance in object orientation?
   Once a class is defined, we can construct a new object base on the class 'blue print'. This object is the actual running code with specific
   attributes.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   Class attribute MUST be shared by all instances of said class, and has the same value in all instances. Instance attributse may or may 
   not be shared by all, but its value is tied only to said instance. Different instances may have same attribute, but it will most likely be
   different in all of them. Some attibutes might exits in one instance and not in another.
   Example: 
      Fox class      -> food_type      (all foxes in the wild have the same type of food)          Class attribute
      A fox instance -> qty_of_food    (but not all foxes can eat the same amount of that food)    Instance attribute
      Another fox    -> broken_leg     (This fox has an extra attibute because of broken leg)      Instance attribute


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
   """ Class that handles the student information including score """
   
   def __init__(self, first_name, last_name, address):
      self.first_name = first_name
      self.last_name = last_name
      self.address = address
      self.score = 0
      
   def update_score(self, score):
      self.score = score

   
class Question(object):
   """ Class with question-answer pair that can ba added to an Exam class. Self-evaluate."""
   
   def __init__(self, question, correct_answer):
      self.question = question
      self.correct_answer = correct_answer
      
   def ask_and_evaluate(self):
      answer = raw_input(self.question + ' >>> ')                 # Ask user this instance question.
      return True if answer == self.correct_answer else False     # Evaluate result and return it.


class Exam(object):
   """ Class that contains a list of Questions. Administering and scoring capabilities """
   
   def __init__(self,name):
      self.name = name
      self.questions = []
      
   def add_question(self, question):
      self.questions.append(question)
      
   def administer(self):
      score = 0
      for question in self.questions:
         if question.ask_and_evaluate():                 # If anser was right add 1 to the score
            score += 1
      return (float(score) / len(self.questions)) * 100  # Total of right answers / total number of questions in percentage format.


def Quiz(Exam):
   
   def administer(self):             # Inheriting from Exam, but overriding administer(). Otherwise behaves the same.
      return True if super(Quiz, self).administer() > 50 else False     # Quiz returns T or F if score >50 %. Exam does the scoring.


def take_test(exam, student):
   """ Function for an specific student to take an specific exam. Score at screen"""
   
   student.update_score(exam.administer())
   print 'Hello %s, you had a score of %.2f %%' % (student.first_name, student.score)

   
def example():
   """ Sample Student and Exam instances to test the classes """
   
   # Creating exam an questions to add to the exam.
   exam = Exam("Feeling checkup")
   q1 = Question("How are you feeling ? (good/bad)", "good")
   q2 = Question("Are you happy ? (yes/no)", "yes")
   q3 = Question("Do you feel lonely ? (yes/no)", "no")
   exam.add_question(q1)
   exam.add_question(q2)
   exam.add_question(q3)
   
   # Creating Student and administering the test
   student = Student("Angelina", "Jolie", "Hollywood, CA")
   
   take_test(exam, student)



###############################################################################
# TESTING: Running the example.

if __name__ == "__main__":
   
   example()
   
   