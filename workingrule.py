'''
Created on 28 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''
import logging

class WorkingRule:
    
    def __init__(self, rule, dataSet, execAgent):
        
        logging.info("Initializing WorkingRule for Rule: " + rule.name + " in RuleSet: " + rule.ruleSet.name + " with DataSet: " + dataSet.name)
        
        self.rule = rule
        self.dataSet = dataSet
        self.execAgent = execAgent
        self.executors = []
        self.evaluators = []
        self.dereference()
        
    
    def dereference(self):
        
        logging.info("Dereference WorkingRule for Rule: " + self.rule.name + " in RuleSet: " + self.rule.ruleSet.name + " with DataSet: " + self.dataSet.name)

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
        logging.info("Call to enqueue WorkingRule for Rule: " + self.rule.name + " in RuleSet: " + self.rule.ruleSet.name + " with DataSet: " + self.dataSet.name)
        self.execAgent.enqueueWorkingRule(self)
            
    