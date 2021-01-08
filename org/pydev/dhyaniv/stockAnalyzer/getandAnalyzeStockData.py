#Author: Vikas Dhyani
#This is the code to extract the stock price from IEX API (need to take the subscription for it)
#
import requests
import json
import org.pydev.dhyaniv.mediaPlayer.alertSounds as alertSounds
import org.pydev.dhyaniv.constants.constants as constants
import org.pydev.dhyaniv.dbfetch.loadStalkerSubjects as loadStalkerSubjects
import pync
from datetime import datetime

from os import path

def getStockData(url, nameOfStock):
     
    filepath = path.relpath(constants.APISECRETPATH)  
    
    with open(filepath) as f:
        data = f.read()
        
    hdrs = json.loads(data)   
    
    response = requests.request("GET", url, headers=hdrs)
    x = json.loads(response.text)
    latestPrice = x[constants.QUOTE][constants.LATESTPRICE]
    openingPrice = x[constants.QUOTE][constants.OPEN] 
    
    diff = latestPrice - openingPrice
    
    # Here We find the %age difference from the opening price
    percentDiff = (diff/openingPrice)*100
    
    #print("opening price of "+nameOfStock+" was:--> "+str(openingPrice))
    #print("Latest Price of "+nameOfStock+" is:--> " + str(latestPrice))
    #print("difference from opening for "+nameOfStock+" is:--> "+str(round(diff,2)))
    print("% open, curr, %diff for "+nameOfStock+":-> "+str(openingPrice)+" ,"+str(latestPrice)+", "+str(round(percentDiff,2))+ "%")
    
    #Play the alert Media File
    #TODO: In future raise alarm only when conditions to buy a stock are met
    #alertSounds.playMSFTAlert()
    #pync.notify(str(latestPrice), title='Alert!! New Microsoft Stock Price')
    
def sellNotification(url, nameOfStock, qty, targetPrice,buyPrice):
     
    filepath = path.relpath(constants.APISECRETPATH)  
    
    with open(filepath) as f:
        data = f.read()
        
    hdrs = json.loads(data)   
    
    response = requests.request("GET", url, headers=hdrs)
    x = json.loads(response.text)
    latestPrice = x[constants.QUOTE][constants.LATESTPRICE]
    diff = round(((latestPrice-buyPrice)/buyPrice)*100, 2) 
    #if (latestPrice > targetPrice*.75):
    print("% Please consider selling "+str(qty) + " of "+nameOfStock+" at:-> "+str(latestPrice)+ " with "+ str(diff) +"% profit")
    #if (latestPrice > buyPrice):    
     #   print("% Please consider selling "+str(qty) + " of "+nameOfStock+" at:-> "+str(latestPrice)+ " with "+ str(diff) +"% profit")
        
    
    #Play the alert Media File
    #TODO: In future raise alarm only when conditions to buy a stock are met
    #alertSounds.playMSFTAlert()
    #pync.notify(str(latestPrice), title='Alert!! New Microsoft Stock Price')    
    
def getStalkedStocksData():
    stockToTrack = loadStalkerSubjects.getStockSubjectsList()
    print("****************")
    for x in stockToTrack:
        IEXendpoint = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/"+str(x[1])+"/book"
        #print(IEXendpoint) # Printing the symbol
        #stockName = str(x[2])
        stockName = str(x[1])
        getStockData(IEXendpoint, stockName)
        
    print("****************\n")
    
def getSellNotificationData():
    stockToTrack = loadStalkerSubjects.getSellTargets()
    print("****************")
    for x in stockToTrack:
        IEXendpoint = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/"+str(x[0])+"/book"
        #stock_symbol = x[0]
        stock_name = x[1]
        qty = x[2]
        min_target_price = x[3]
        buy_price = x[4]
        #print(IEXendpoint) # Printing the symbol
        #stockName = str(x[2])
        
        #getStockData(IEXendpoint, stockName)
        sellNotification(IEXendpoint, stock_name, qty, min_target_price, buy_price)
        
    print("****************\n")      
    
    
def harvestOpenPrice():
    stockToHarvest = loadStalkerSubjects.getOpenPriceSubjectsList()
    
    print("*****Going to Register open prices now*****")
    for x in stockToHarvest:
        IEXendpoint = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/"+str(x[1])+"/book"
        filepath = path.relpath(constants.APISECRETPATH)  
    
        with open(filepath) as f:
            data = f.read()
        
        hdrs = json.loads(data)   
    
        response = requests.request("GET", IEXendpoint, headers=hdrs)
        y = json.loads(response.text)
        openingPrice = y[constants.QUOTE][constants.OPEN]
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d')
        #print (x[1]+"***"+formatted_date+"***"+str(openingPrice))
        #print(x[1]+"***"+"***"+str(openingPrice))
        loadStalkerSubjects.insertIntoOpenPriceTracker(x[1], formatted_date, round(openingPrice,2)) 
              
            