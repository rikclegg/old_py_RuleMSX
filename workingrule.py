'''
Created on 28 Nov 2017

@author: metz
'''

class WorkingRule:
    
    def __init__(self, rule, dataSet, execAgent):
        
        self.rule = rule
        self.dataSet = dataSet
        self.execAgent = execAgent
        self.executors = []
        self.evaluators = []
        self.dereference()
        
    
    def dereference(self):
        
        if not self.rule.actions == []:         
            for action in self.rule.actions:
                self.executors.append(action.actionExecutor)
            
        if not self.rule.ruleConditions == []:         
            for condition in self.rule.ruleConditions:
                self.evaluators.append(condition.evaluator)
                for dpn in condition.evaluator.dependentDataPointNames:
                    dp = self.dataSet.dataPoints[dpn]
                    dp.dataPointSource.associateWorkingRule(self)
                    
        
        
            
    def enqueueWorkingRule(self):
        self.execAgent.enqueueWorkingRule(self)
            
    