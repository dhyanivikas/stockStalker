#Author: Vikas Dhyani
#This is the code to extract the stock price from IEX API (need to take the subscription for it)
#
import requests
import json
import org.pydev.dhyaniv.mediaPlayer.alertSounds as alertSounds
import org.pydev.dhyaniv.constants.constants as constants
import pync

from os import path

def getStockData():
    
    url = constants.IEXENPOINT 
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
    
    print("opening price was:--> "+str(openingPrice))
    print("Latest Price is:--> " + str(latestPrice))
    print("difference from opening is:--> "+str(diff))
    print("% difference from opening is:--> "+str(percentDiff))
    
    #Play the alert Media File
    #TODO: In future raise alarm only when conditions to buy a stock are met
    alertSounds.playMSFTAlert()
    pync.notify(str(latestPrice), title='Alert!! New Microsoft Stock Price')