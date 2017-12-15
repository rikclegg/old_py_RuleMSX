'''
Created on 25 Nov 2017

@author: Rik Clegg

'''
import logging
from dataset import DataSet
from ruleset import RuleSet
from action import Action

class RuleMSX:
    
    def __init__(self,lvl=logging.CRITICAL):
        self.setLogLevel(lvl)
        self.logger = logging.getLogger(__name__)

        self.logger.info("Initializing sets")
        
        self.ruleSets = {}
        self.dataSets = {}
        self.actions = {}
    
    def setLogLevel(self,lvl):
        logging.basicConfig(level=lvl)

    def createDataSet(self,name):
        
        self.logger.info("Creating DataSet: " + name)

        if(name is None or name == ""):
            raise ValueError("DataSet name cannot be none or empty")
        
        ds = DataSet(name)
        self.dataSets[name] = ds
        return ds
        
        
    def createRuleSet(self,name):
    
        self.logger.info("Creating RuleSet: " + name)

        if(name is None or name == ""):
            raise ValueError("RuleSet name cannot be none or empty")
        
        rs = RuleSet(name)
        self.ruleSets[name] = rs
        return rs

    
    def createAction(self,name, executor):
        
        self.logger.info("Creating Action: " + name)
        
        if(name is None or name == ""):
            raise ValueError("Action name cannot be none or empty")
        
        a = Action(name,executor)
        self.actions[name] = a
        return a
    
    
    def stop(self):
        
        self.logger.info("Stopping RuleMSX")
        
        result = True
        
        for rs in self.ruleSets:
            if not rs.stop(): result = False
            
        return result
        