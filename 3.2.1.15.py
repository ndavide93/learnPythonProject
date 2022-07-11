class QueueError(IndexError):  # Choose base class for the new exception.
    pass

    #  Write code here
    #
class Queue:
    def __init__(self):
        self.Queue=[]
        #
        # Write code here
        #
    def put(self, elem):
        self.Queue.append(elem)
        
        #
        # Write code here
        #
    def get(self):
        try :
            val=self.Queue[0]
            del self.Queue[0]
            return val
        except: 
            raise QueueError     
        
        #

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
