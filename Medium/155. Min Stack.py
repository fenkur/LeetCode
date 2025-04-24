class MinStack(object):

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val):
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(val, self.min_stk[-1]))

    def pop(self):
        self.stk.pop()
        self.min_stk.pop()

    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.min_stk[-1]


