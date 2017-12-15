'''
Created on 27 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''

from datapoint import DataPoint
import logging

class DataSet:
    
    def __init__(self,name):
        
        logging.info("Initializing DataSet: " + name)
        self.name = name
        self.dataPoints = {}
        logging.info("Initialized DataSet: " + name)
        
    def addDataPoint(self,name, dataPointSource=None):
        
        logging.info("Add DataPoint: " + name + " to DataSet: " + self.name)

        if(name is None or name == ""):
            raise ValueError("DataPoint name cannot be none or empty")
        
        dp = DataPoint(self, name)
        
        if not dataPointSource == None:
            dp.setDataPointSource(dataPointSource)
        
        self.dataPoints[name] = dp

        logging.info("Added DataPoint: " + name + " to DataSet: " + self.name)

        return dp
