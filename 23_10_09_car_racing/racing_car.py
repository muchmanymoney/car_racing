# 게터, 세터를 추가했을 뿐, 이 클래스는 과제글에서 제시한 그대로 입니다.


class Car:
    __name: str
    __position: int = 0
    def __init__(self, name: str):
        self.__name = name
        self.__position = 0

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

