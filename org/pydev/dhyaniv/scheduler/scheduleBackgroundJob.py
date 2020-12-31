import org.pydev.dhyaniv.stockAnalyzer.getandAnalyzeStockData as stockAnalyzer
import org.pydev.dhyaniv.constants.constants as constants
import time
import schedule



if __name__ == "__main__":
    print("Hello guys!")
    #schedule.every(20).seconds.do(stockAnalyzer.getStockData)
    schedule.every(constants.CHECKFREQUENCY).seconds.do(stockAnalyzer.getStockData)

    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)