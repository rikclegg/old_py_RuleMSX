'''
Created on 28 Nov 2017

@author: metz
'''

class RuleEvaluator:
    
    def __init__(self):
        self.dependentDataPointNames = []

    def evaluate(self,dataSet):
        raise NotImplementedError("The evaluate function of a RuleEvaluator must be overridden")
    
    def setCondition(self, condition):
        self.condition = condition
        
    def addDependentDataPointName(self,dataPointName):
        self.dependentDataPointNames.append(dataPointName)
