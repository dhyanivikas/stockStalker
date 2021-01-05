'''
Created on Jan 3, 2021

@author: dhyaniv
'''

import mysql.connector
import org.pydev.dhyaniv.dbfetch.getDBConnection as dbConn



def getStockSubjectsList(): #no error method
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    cur.execute("select id, stock_symbol, stock_name from stocks_watch_list where track_intra_day = 'Y'")
    stockStalkerSubjects = cur.fetchall()
    return stockStalkerSubjects



def getOpenPriceSubjectsList():
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    cur.execute("select id, stock_symbol, stock_name from stocks_watch_list where track_open_price = 'Y'")
    openPriceStalkerSubjects = cur.fetchall()
    return openPriceStalkerSubjects    

#getStockSubjectsList()

def insertIntoOpenPriceTracker(stock_symbol, trading_date, open_price):
    
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    #query = 'INSERT INTO stocks_opening_prices1(stock_symbol, trading_date, open_price) values(%s,%s,%d) '
    query = 'INSERT INTO stocks_opening_prices(stock_symbol, trading_date, open_price) values(%s,%s,%s) '
    args = (stock_symbol, trading_date, round(open_price,2))
    print(stock_symbol+"***"+trading_date+"***"+str(open_price))
    cur.execute(query, args)
    dbConnection.commit()