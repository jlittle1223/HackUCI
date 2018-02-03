'''
A course is a combination of prerequisites represented 
in the form of a sum of products (product of sums)
'''

class Course:
    
    def __init__(self, name):
        self.name = name
        self.localPrerequisites = set()
        self.totalPrerequisites = set()
        self.sumOfProducts = True
        self.sumOfProductsList = []
        self.numTotalPrerequisites = 0
        self.numLocalPrerequisites = 0
        
        
        
    def addPrerequisite(self, prerequisite):
        '''
        Adds a prerequisite to the current course by making the
        Sum of Products a logical conjunction of the current
        Sum of Products and the Sum of Products of the prerequisites
        '''
        self.sumOfProducts = self.sumOfProducts and prerequisite.sumOfProducts
        self.sumOfProductsList.append(prerequisite)
        self.localPrerequisites.add(prerequisite)
        self.numLocalPrerequisites += 1
        
        
        
    def addPrerequisiteDisjunction(self, prerequisiteDisjunction:list):
        self.sumOfProductsList.append(prerequisiteDisjunction)
        #self.localPrerequisites.add(prerequisiteDisjunction)
        self.numLocalPrerequisites += len(prerequisiteDisjunction)
        
        
        
    def printPrerequisites(self):
        sumOfProductsList = self.sumOfProductsList
        print("Prerequisites for {} = ".format(self.name), end = "")
        for i in range(len(sumOfProductsList)):
            if type(sumOfProductsList[i]) == list:
                print("(", end = "")
                for j in range(len(sumOfProductsList[i])):
                    if j < len(sumOfProductsList[i]) - 1:
                        print("{} or ".format(sumOfProductsList[i][j].name), end = "")
                    else:
                        print(sumOfProductsList[i][j].name, end = "")
                print(")", end = "")
                if i < len(sumOfProductsList) - 1:
                    print(" and ", end = "")
            else:
                if i < len(sumOfProductsList) - 1:
                    print("{} and ".format(sumOfProductsList[i].name), end = "")
                else:
                    print(sumOfProductsList[i].name)
                    
                    
    def __str__(self):
        return self.name
                
        
        
    



if __name__ == "__main__":
    ics51 = Course("ICS51")
    ics31 = Course("ICS33")
    ics6b = Course("ICS6B")
    ics6n = Course("ICS6N")
    math3a = Course("MATH3A")
    
    
    ics51.addPrerequisite(ics31)
    ics51.addPrerequisiteDisjunction([ics6n, math3a])
    ics51.addPrerequisite(ics6b)


    
    ics51.printPrerequisites()
    
    
    
    
    
    
    
    



