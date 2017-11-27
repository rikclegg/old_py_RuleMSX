'''
Created on 25 Nov 2017

@author: Rik Clegg
'''
import unittest
import rulemsx


class TestRuleMSX(unittest.TestCase):

    def test_InstantiateRuleMSXEmptyConstGivesEmptyRuleandDataSets(self):

        rmsx = rulemsx.RuleMSX()
        self.assertEqual(len(rmsx.dataSets),0)
        self.assertEqual(len(rmsx.ruleSets),0)
        
        
    def test_CreateDataSetReturnsNewDataSet(self):
        
        rmsx = rulemsx.RuleMSX()
        newDataSetName = "NewDataSet"
        ds = rmsx.createDataSet(newDataSetName)
        self.assertEqual(ds.name, newDataSetName)
        
        
    def test_CreateRuleSetReturnsNewRuleSet(self):
        
        rmsx = rulemsx.RuleMSX()
        newRuleSetName = "NewRuleSet"
        rs = rmsx.createRuleSet(newRuleSetName)
        self.assertEqual(rs.name, newRuleSetName)
        
    
    def test_CreateDataSetWithEmptyNameFails(self):
        
        rmsx = rulemsx.RuleMSX()
        newDataSetName = ""
        self.assertRaises(ValueError, rmsx.createDataSet,newDataSetName)
        
    
    def test_CreateRuleSetWithEmptyNameFails(self):
        
        rmsx = rulemsx.RuleMSX()
        newRuleSetName = ""
        self.assertRaises(ValueError, rmsx.createRuleSet,newRuleSetName)

    
    def test_CreateDataSetWithNameAsNone(self):
        
        rmsx = rulemsx.RuleMSX()
        newDataSetName = None
        self.assertRaises(ValueError, rmsx.createDataSet,newDataSetName)
        
    
    def test_CreateRuleSetWithNameAsNone(self):
        
        rmsx = rulemsx.RuleMSX()
        newRuleSetName = None
        self.assertRaises(ValueError, rmsx.createRuleSet,newRuleSetName)
        
    
    def test_RuleMSXStopShouldReturnTrueWithNoRuleSets(self):
        
        rmsx = rulemsx.RuleMSX()
        self.assertTrue(rmsx.stop())

    
    def test_RuleMSXStopShouldReturnTrueWithActiveRuleSet(self):
        
        rmsx = rulemsx.RuleMSX()
        ruleSetName = "NewRuleSet"
        rs = rmsx.createRuleSet(ruleSetName)
        self.assertTrue(rs.stop())
        
        
    def test_RuleSetGetNameShouldReturnName(self):
        
        rmsx = rulemsx.RuleMSX()
        ruleSetName = "NewRuleSet"
        rs = rmsx.createRuleSet(ruleSetName)
        self.assertEqual(rs.name, ruleSetName)

    
    def test_CreateDataPointNoSourceCheckName(self):
        
        rmsx = rulemsx.RuleMSX()
        dataSetName = "NewDataSet"
        dataPointName = "NewDataPoint"
        ds = rmsx.createDataSet(dataSetName)
        ds.addDataPoint(dataPointName)
        self.assertEqual(ds.dataPoints[dataPointName].name, dataPointName)


    def test_CreateDataPointNoNameFail(self):
        
        rmsx = rulemsx.RuleMSX()
        dataSetName = "NewDataSet"
        dataPointName = None
        ds = rmsx.createDataSet(dataSetName)
        self.assertRaises(ValueError, ds.addDataPoint, dataPointName)
        

    def test_CreateDataPointEmptyNameFail(self):
        
        rmsx = rulemsx.RuleMSX()
        dataSetName = "NewDataSet"
        dataPointName = ""
        ds = rmsx.createDataSet(dataSetName)
        self.assertRaises(ValueError, ds.addDataPoint, dataPointName)
