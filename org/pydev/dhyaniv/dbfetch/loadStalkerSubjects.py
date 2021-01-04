'''
Created on Jan 3, 2021

@author: dhyaniv
'''

import mysql.connector
import org.pydev.dhyaniv.dbfetch.getDBConnection as dbConn



def getStockSubjectsList(): #no error method
    dbConnection = dbConn.getconnection()
    cur = dbConnection.cursor()
    cur.execute("select id, stock_symbol, stock_name from stocks_watch_list")
    stockStalkerSubjects = cur.fetchall()
    return stockStalkerSubjects


getStockSubjectsList()
