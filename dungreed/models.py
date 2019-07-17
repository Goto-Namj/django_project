from django.db import models


class IO():     # 얘가 원래 MVC Control이니까 지워야함
    def __init__(self):
        self.Calc = Calc()

    def inputs(self, element):
        self.Calc.add(element)

    def output(self):
        return self.Calc.give_answer()


class Calc():       # 얘는 MVC의 Model
    def __init__(self):
        self.elements = 0

    def add(self, element):
        self.elements += element
    
    def give_answer(self):
        return self.elements