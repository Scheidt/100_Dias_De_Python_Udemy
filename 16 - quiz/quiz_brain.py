from data import question_data
from model import Question
from random import randint

class Game:
    def __init__(self) -> None:
        self.__questions = []
        self.__points = 0
        for element in question_data:
            self.__questions.append(Question(element['text'], element['answer']))
            print(element)
        
    def play(self):
        question = randint(0, len(self.__questions)-1)
        question = self.__questions[question]
        print(question.text) #I admit this way of writing might be confusing, but it is what it is.
        answer = input("Answer True/False: ").capitalize()
        while answer not in ("True", "False"):
            answer = input("You answer may be only True/False, please, try again. ")
        if answer == question.answer:
            self.__points += 1
            print(f"You got it right! Current points: {self.__points}")
        else:
            print("That's not right. You didn't get a point.")
        print('\n'*3)
