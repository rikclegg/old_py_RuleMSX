'''
Created on 28 Nov 2017

@author: metz
'''

class WorkingRule:
    
    def __init__(self, rule, dataSet):
        
        self.rule = rule
        self.dataSet = dataSet
        self.executors = []
        self.evaluators = []
        self.dereference()
        
    
    def dereference(self):
        
        for action in self.rule.actions:
            self.executors.append(action.actionExecutor)
            
        for condition in self.rule.ruleConditions:
            self.evaluators.append(condition.evaluator)
            
            
    