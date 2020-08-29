class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l_num = []
        self.minval = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.l_num) == 0 or len(self.minval) == 0:
            self.minval.append([x,1])
        else:
            if x < self.getMin():
                self.minval.append([x,1])
            elif x == self.getMin():
                self.minval[-1][1] += 1
        self.l_num.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.l_num[-1] == self.minval[-1][0]:
            self.l_num.pop(-1)
            if (self.minval[-1][1]>1):
                self.minval[-1][1] -= 1
            else:
                self.minval.pop(-1)
        else:
            self.l_num.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.l_num[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minval[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()