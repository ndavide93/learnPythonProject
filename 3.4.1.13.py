from operator import truediv


class WeekDayError(Exception):
    pass
class Weeker:
    __name = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    __valore = 0
    def __init__(self, day):
        try:
            __valore=self.__name.index(day)
        except:
            raise WeekDayError

    def add_days(self, n):
        self.__valore += n
        if self.__valore  > 8:
            while self.__valore >7:
                self.__valore -=7
            else:
                return self.__valore
        else:
            return self.__valore
    def subtract_days(self, n):
        self.__valore -= n
        if self.__valore  < 0:
            while self.__valore <0 :
                self.__valore +=7
        else:
            return self.__valore
        #
        # Write code here.
        #
    def __str__(self):

        return str(self.__name[self.__valore])
        # Write code here.
    

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
#lavora solo con __valore
#reverse dell'index solo nella str