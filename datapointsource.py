'''
Created on 27 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''
import logging

class DataPointSource:
    
    def __init__(self):
        
        logging.info("Initializing DataPointSource")

        self.dataPoint  = None
        self.associatedWorkingRules = []
        self.isStale = True
    
        logging.info("Initialized DataPointSource")
    
    def setDataPoint(self,dataPoint):
        
        logging.info("Setting DataPoint for DataPointSource: " + dataPoint.name)

        self.dataPoint = dataPoint
        
    
    def getDataPoint(self):

        logging.info("Get DataPointSource DataPoint for : " + self.dataPoint.name)

        try:
            return self.dataPoint
        except:
            self.dataPoint=None
            return self.dataPoint
    
    def getValue(self):
        
        logging.info("Get Value for DataPointSource of DataPoint: " + self.dataPoint.name)
        
        raise NotImplementedError()
        
    
    def setStale(self):
        
        logging.info("Set DataPointSource stale for DataPoint: " + self.dataPoint.name)
        
        self.isStale = True
        try:
            logging.info("Checking DataPointSource associated working rule for DataPoint: " + self.dataPoint.name)

            for ar in self.associatedWorkingRules:
                logging.info("Call to enqueue WorkingRule for RuleSet: " + ar.ruleSet.name + " and DataSet: " + ar.dataSet.name)
                ar.enqueueWorkingRule()
        except:
            #ignore
            self.associatedWorkingRules = []

        logging.info("Set DataPointSource stale for DataPoint: " + self.dataPoint.name + " complete")
    
    def associateWorkingRule(self,workingRule):

        logging.info("Associate WorkingRule for Rule: " + workingRule.rule.name + " of RuleSet: " + workingRule.rule.ruleSet.name + " and DataSet: " + workingRule.dataSet.name)

        try:
            self.associatedWorkingRules.append(workingRule)
        except:
            self.associatedWorkingRules = []
            self.associatedWorkingRules.append(workingRule)
