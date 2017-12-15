'''
Created on 27 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''

import logging

class Action:
    
    def __init__(self, name, executor=None):
        
        logging.info("Initializing Action: " + name)
        
        self.name = name
        self.actionExecutor = executor

        logging.info("Initialized Action: " + name)
        
    def execute(self, dataSet):

        logging.info("Executing Action: " + self.name + " with dataSet: " + dataSet.name)

        if not self.actionExecutor == None:
            logging.info("Calling Action executor")
            self.actionExecutor.execute(dataSet)
            logging.info("Called Action executor")
            

        
    