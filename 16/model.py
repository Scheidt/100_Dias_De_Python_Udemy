class Question():
    def __init__(self, text, answer) -> None:
        self.__text = text
        self.__answer = answer

    @property
    def text(self):
        return self.__text
    
    @property
    def answer(self):
        return self.__answer
    
    @text.setter
    def text(self, text):
        self.__text = text

    @answer.setter
    def answer(self, answer):
        self.__answer = answer
