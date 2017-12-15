'''
Created on 27 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''

from rule import Rule
from executionagent import ExecutionAgent
import logging

class RuleSet:
    
    def __init__(self,name):
        
        logging.info("Initializing RuleSet: " + name)
        
        self.name = name
        self.rules = {}
        self.executionAgent = None

        logging.info("Initialized RuleSet: " + name)

    def stop(self):

        logging.info("Stopping  executionAgent for RuleSet: " + self.name)

        if not self.executionAgent == None:
            self.executionAgent.stop()
            
        return True
        
    def addRule(self,name):
        
        logging.info("Adding Rule: " + name + " to RuleSet: " + self.name)

        if(name is None or name == ""):
            raise ValueError("Rule name cannot be none or empty")
        
        r = Rule(self, name)
        
        self.rules[name] = r
        return r

    def execute(self,dataSet):
        
        if self.executionAgent == None:

            logging.info("Execute RuleSet: " + self.name + " with DataSet: " + dataSet.name)

            self.executionAgent = ExecutionAgent(self, dataSet)
        
        else:
            
            logging.info("Add DataSet: " + dataSet.name + " to ExecutionAgent for RuleSet: " + self.name)

            self.executionAgent.addDataSet(dataSet)
        