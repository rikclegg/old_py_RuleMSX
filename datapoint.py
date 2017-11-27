'''
Created on 27 Nov 2017

@author: metz
'''
class DataPoint:
    
    def __init__(self,name):
        
        self.name = name
        self.dataPointSource = None
    
    def setDataPointSource(self, dataPointSource):
        self.dataPointSource = dataPointSource