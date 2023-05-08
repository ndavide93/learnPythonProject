class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()#list [0] sum[0]

for i in range(5): #[0 1 2 3 4 5]
    stack_object.push(i)
    #AddingStack list [0 1 2 3 4 5] sum [1+2+3+4+5=15]
print(stack_object.get_sum())
  #15
for i in range(5):#[0 1 2 3 4 5]
    print(stack_object.pop())
    #5 [sum 10]
    #4 [sum 6]
    