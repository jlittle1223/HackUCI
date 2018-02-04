class Course():
    def __init__(self, name, preq):
        self.name = name
        self.preq = preq

    def return_info(self):
        self.name = self.name.replace(' ', '')
        self.preq = self.preq[14:]
        count = 0
        for i in reversed(self.preq):
            count += 1
            if i == '.':
                self.preq = self.preq[:-count]
                count = 0
##        self.preq.rstrip('\n')
##        self.preq.rstrip('\n')
        self.preq += '\n'
        return(self.name + ':' + self.preq)
    
