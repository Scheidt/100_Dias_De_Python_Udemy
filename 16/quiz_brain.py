import data
from model import Question
from random import randint

class Game:
    def __init__(self) -> None:
        self.__questions = []
        for element in data:
            self.__questions.append(Question(element['text'], element['answer']))
        
    def play(self):
        question = randint(0, len(self.__questions))
        question = self.__questions[question]
        print(question['question']) #I admit this way of writing might be confusing, but it is what it is.
        answer = input("Answer True/False: ").capitalize()
        while answer not in ("True", "False"):
            answer = input("You answer may be only True/False, please, try again. ")
        answer = bool(answer)
        if answer == question['answer']:
            pass