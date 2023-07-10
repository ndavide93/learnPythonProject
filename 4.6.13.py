import calendar
class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        contagiorni = 0
        for mese in range(1, 13):
            for gg in calendar.Calendar.monthdays2calendar(self, year, mese):
                for a,b in gg:
                    if b == weekday and a != 0:
                        contagiorni += 1
        return contagiorni
My_Calendar = MyCalendar()
print(My_Calendar.count_weekday_in_year(year=2019, weekday=0))



#dato l'anno e il giorno [0 lunedi]
##fin tanto che il mese è >=12   --> for
# per ogni giorno nel year , se weekday = 0 aumenta il contatore

 