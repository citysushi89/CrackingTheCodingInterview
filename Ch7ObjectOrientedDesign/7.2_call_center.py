"""
Call center with 3 employees, respondent, manager, and director
calls go in above order
design the classes and data structures for this problem
Implement a method dispatchCall() which assigns a call to the first avaliable employee
"""


class Employee:
    def __init__(self, name, id_num, is_available=True):
        self.name = name
        self.id_num = id_num
        self.is_available = is_available


class Respondent(Employee):
    respondents = []
    def __init__(self, name, id_num, is_available=True):
        super().__init__(name, id_num, is_available)
        # self.is_available = is_available
        Respondent.respondents.append(self)


class Manager(Employee):
    managers = []
    def __init__(self, name, id_num, is_available=True):
        super().__init__(name, id_num, is_available)
        # self.is_available = is_available
        Manager.managers.append(self)


class Director(Employee):
    directors = []
    def __init__(self, name, id_num, is_available=True):
        super().__init__(name, id_num, is_available)
        # self.is_available = is_available
        Director.directors.append(self)


res = Respondent("Person R", 15)
man = Manager("Person Man", 20)
direc = Director("Person Direc", 25) 

res.is_available = False

def dispatchCall():
    for respondent in Respondent.respondents:
        if respondent.is_available:
            return respondent.name

    for manager in Manager.managers:
        if manager.is_available:
            return manager.name

    for director in Director.directors:
        if director.is_available:
            return director.name
        
    return "No avaliable employees, please try again later"


print(dispatchCall())