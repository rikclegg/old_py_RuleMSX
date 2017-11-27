'''
Created on 27 Nov 2017

@author: metz
'''
class RuleSet:
    
    def __init__(self,name):
        
        self.name = name
        self.rules = {}
        
    def stop(self):
        return True