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
      return True if super(Quiz, self).administer() > 50 else False     # Quiz returns T or F instead of a score. Exam does the scoring.


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