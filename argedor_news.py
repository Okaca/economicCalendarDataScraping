from investing_news_db_process import addInvestingNewsData, getInvestingNewsData
from investpy_trial import get_event_time_investing
import schedule
import time


#print(get_event_time_investing(None, None))
def job():
    obtained_data = get_event_time_investing(None, None)

    for element in obtained_data:
        #print(element[2])
        addInvestingNewsData(element[0], element[1], element[2], element[3])

schedule.every().day.at("00:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(3659)
