'''
Created on Jan 3, 2021

@author: dhyaniv
'''
import mysql.connector
  
def getconnection():

    config = {
        "host":"localhost",
        "user":"root",
        "password":"H1cke$$1nk",
        "database":"stocks",
        "auth_plugin":'mysql_native_password'
    }
    try:
        c = mysql.connector.connect(**config)
        return c
    except:
        print("connection error")
        exit(1)  
                  