#def doppiadigitazione

class Timer:
    def __init__(self,hh = 0,mm = 0,ss = 0):
        self.hour= hh
        self.minute= mm
        self.seconds = ss
        #
        # Write code here
        #

    def __str__(self):
        return str(self.hour)  + ":" + str(self.minute)  + ":" + str(self.seconds)  
        #
        # Write code here
        #

    def next_second(self):
        self.seconds +=1
        if self.seconds > 59:
            self.seconds =0
            self.minute +=1
            if self.minute > 59:
                self.minute = 0
                self.hour +=1
                if self.hour > 23 :
                    self.hour = 0
        #
        # Write code here
        #

    def prev_second(self):
        self.seconds -=1
        if self.seconds < 0:
            self.seconds = 59
            self.minute -=1
            if self.minute < 0:
                self.minute = 59
                self.hour -=1
                if self.hour < 0 :
                    self.hour = 23
        #
        # Write code here
        #


timer = Timer(0,0,0)
print(timer)
timer.prev_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)