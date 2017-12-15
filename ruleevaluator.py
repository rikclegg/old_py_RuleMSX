'''
Created on 28 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''

import logging

class RuleEvaluator:
    
    def evaluate(self,dataSet):
        raise NotImplementedError("The evaluate function of a RuleEvaluator must be overridden")
    
    def setCondition(self, condition):
        self.condition = condition
        
    def addDependentDataPointName(self,dataPointName):
        
        try:
            logging.info("Add dependent DataPoint name: " + dataPointName + " for RuleCondition: " + self.condition.name)
        except:
            logging.info("Add dependent DataPoint name: " + dataPointName + " for RuleCondition: unknown")
            
        try:
            self.dependentDataPointNames.append(dataPointName)
        except:
            self.dependentDataPointNames = []
            self.dependentDataPointNames.append(dataPointName)
