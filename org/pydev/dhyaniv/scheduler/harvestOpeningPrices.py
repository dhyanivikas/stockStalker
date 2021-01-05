'''
Created on Jan 4, 2021

@author: dhyaniv
'''
import org.pydev.dhyaniv.stockAnalyzer.getandAnalyzeStockData as stockAnalyzer
import org.pydev.dhyaniv.constants.constants as constants

if __name__ == "__main__":
    
    print("****Going to Harvest Opening Prices Now****")
    stockAnalyzer.harvestOpenPrice()
    print("****Stored the opening prices for today****")