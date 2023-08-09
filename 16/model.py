class Question():
    def __init__(self, question, answer) -> None:
        self.__question = question
        self.__answer = answer

    @property
    def question(self):
        return self.__question
    
    @property
    def answer(self):
        return self.__answer
    
    @question.setter
    def question(self, question):
        self.__question = question

    @answer.setter
    def answer(self, answer):
        self.__answer = answer