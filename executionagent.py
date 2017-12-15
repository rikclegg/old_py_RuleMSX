'''
Created on 28 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''

import threading
import queue
from workingrule import WorkingRule
import logging

class ExecutionAgent:
    
    class WorkingSetAgent(threading.Thread):
        
        def __init__(self,execAgent):

            logging.info("Initializing WorkingSetAgent for RuleSet: " + execAgent.ruleSet.name)

            self.running = True
            self.openSetQueue = []
            self.openSet = []
            self.execAgent= execAgent
            self.workingSet = []
            self.lock = threading.Lock()
            threading.Thread.__init__(self)
            
            logging.info("Initialized WorkingSetAgent for RuleSet: " + execAgent.ruleSet.name)

        def run(self):
            
            logging.info("Running WorkingSetAgent for RuleSet: " + self.execAgent.ruleSet.name)

            iterationCount = 0
            while(self.running):
                
                iterationCount=iterationCount+1
                
                with self.lock:
                    while self.execAgent.dataSetQueue.qsize() >0:
                        ds = self.execAgent.dataSetQueue.get()
                        self.ingestDataSet(ds)
            
                    
                while len(self.openSetQueue) > 0:
                    
                    logging.info("WorkingAgent for: " + self.execAgent.ruleSet.name + " iteration count: " + str(iterationCount))
                    
                    with self.lock:

                        logging.info("Migrate OpenSetQueue to OpenSet in WorkingAgent for: " + self.execAgent.ruleSet.name)
                        
                        self.openSet = list(self.openSetQueue)
                        self.openSetQueue = []
                    
                    for wr in self.openSet:

                        logging.info("Traverse OpenSet[" + str(len(self.openSet)) + "] in WorkingAgent for: " + self.execAgent.ruleSet.name)

                        res = True
                        for e in wr.evaluators:
                            if not e.evaluate(wr.dataSet): 
                                res = False
                                break
                            
                        if res:
                            for x in wr.executors:
                                x.execute(wr.dataSet)
                        
                
        def ingestDataSet(self,dataSet):
                
            logging.info("Ingest DataSet: " + dataSet.name + " for " + self.execAgent.ruleSet.name)

            for r in self.execAgent.ruleSet.rules.values():

                logging.info("Build WorkingRule for Rule: " + r.name)

                wr = WorkingRule(r,dataSet, self)
                self.workingSet.append(wr)
                self.enqueueWorkingRule(wr)
            
    
        def enqueueWorkingRule(self,wr):

            # only insert if not already in the queue
            if wr not in self.openSetQueue:
                logging.info("Enqueue WorkingRule for Rule: " + wr.rule.name + " of RuleSet: " + wr.rule.ruleSet.name + " and DataSet: " + wr.dataSet.name)
                self.openSetQueue.append(wr)
            else:
                logging.info("Not Enqueuing WorkingRule for RuleSet: " + wr.ruleSet.name + " and DataSet: " + wr.dataSet.name + " as it is already in queue")
                

    def __init__(self,ruleSet, dataSet=None):
        
        logging.info("Initializing ExecutionAgent for: " + ruleSet.name)
        
        self.ruleSet = ruleSet
        
        self.dataSetQueue = queue.Queue()

        if not dataSet == None:
            self.addDataSet(dataSet)
        
        self.workingSetAgent = self.WorkingSetAgent(self)
        self.workingSetAgent.start()

        logging.info("Initialized ExecutionAgent for: " + ruleSet.name)
        
    def stop(self):

        logging.info("Stopping ExecutionAgent for: " + self.ruleSet.name)

        self.workingSetAgent.running=False
        try:
            self.workingSetAgent.join()
        except:
            return False

        return True
            
    def addDataSet(self,dataSet):
        
        logging.info("Adding DataSet: " + dataSet.name + " to dataSetQueue in ExecutionAgent for: " + self.ruleSet.name)

        self.dataSetQueue.put(dataSet)
        
        