'''
Created on 28 Nov 2017

@author: metz
'''

class RuleCondition:
    
    def __init__(self, name, evaluator):
        
        if name == "" or name is None:
            raise ValueError("RuleCondition name cannot be empty or None")
 
        if evaluator == None:
            raise ValueError("RuleCondition evaluator cannot be None")

        self.name = name
        self.evaluator = evaluator
        self.evaluator.setCondition(self)
        
        
    
        
        