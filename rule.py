'''
Created on 28 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''
import logging

class Rule:
    
    def __init__(self, ruleSet, name):
        
        logging.info("Initializing Rule: " + name + " for RuleSet: " + ruleSet.name)
        
        self.ruleSet = ruleSet
        self.name = name
        self.ruleConditions = []
        self.actions = []
        
        logging.info("Initialized Rule: " + name)

    
    def addRuleCondition(self, ruleCondition):
        
        logging.info("Adding RuleCondition: " + ruleCondition.name + " for Rule: " + self.name)

        if ruleCondition == None:
            raise ValueError("RuleCondition cannot be none")
        
        self.ruleConditions.append(ruleCondition)
        
    
    def evaluate(self):
        
        logging.info("Evaluating Rule: " + self.name + " in RuleSet: " + self.ruleSet.name)

        for rc in self.ruleConditions:
            
            if not rc.evaluate():
                return False
            
        return True
    
    def addAction(self,ruleAction):
        
        logging.info("Add Action: " + ruleAction.name + " to Rule: " + self.name + " in RuleSet: " + self.ruleSet.name)

        if ruleAction is None:
            raise ValueError("RuleAction cannot be None")
        
        self.actions.append(ruleAction)
        
    