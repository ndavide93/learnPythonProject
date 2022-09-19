class WeekDayError(Exception):
    pass
class Weeker:

    __nomegiorni = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    
    def __init__(self, day):
        
        __valoregiorni=self.index(day)
        
    def __str__(self):
        
        return str(self.day)
  
    def add_days(self, n):
        
        self.__nomegiorni += n
        if self.__nomegiorni - 7 <= 0 :
            while True:
                self.__nomegiorni +=7
                return self.__nomegiorni
        else:
            return self.__nomegiorni
            
    def subtract_days(self, n):
        self.__nomegiorni -= n
        if self.__nomegiorni + 7 <= 0 :
            while True:
                self.__nomegiorni +=7
                return self.__nomegiorni
        else:
            return self.__nomegiorni
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
