'''
Created on 27 Nov 2017

@author: RCLEGG2@BLOOMBERG.NET
'''
from datapointsource import DataPointSource
import logging

class DataPoint:
    
    def __init__(self, dataSet, name, dataPointSource=None):
        
        logging.info("Initializing DataPoint: " + name)
        
        self.name = name
        
        self._dataSet = dataSet
        
        if not dataPointSource == None:
            self.setDataPointSource(dataPointSource)

        logging.info("Initialized DataPoint: " + name)
            
    def setDataPointSource(self, dataPointSource):

        logging.info("Set DataPointSource for DataPoint: " + self.name)

        if dataPointSource == None:
            raise ValueError("Invalid dataPointSource")

        if not isinstance(dataPointSource, DataPointSource) :
            raise TypeError("Not a valid DataPointSource")
        
        dataPointSource.setDataPoint(self)
        self.dataPointSource = dataPointSource

        logging.info("DataPointSource Set for DataPoint: " + self.name)
    
    def getValue(self):

        logging.info("Getting value for DataPoint: " + self.name)
        
        return self.dataPointSource.getValue()
        
    